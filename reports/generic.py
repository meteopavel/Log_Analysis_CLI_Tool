from collections import defaultdict

from config.constants import LOG_LEVELS
from reports.base import (
    BaseLogParser, BaseReportCalculator, BaseReportFormatter, BaseReport
)
from utils.log_parser import parse_log_file, get_row_format_template


class GenericLogParser(BaseLogParser):
    def __init__(self, report_type: str):
        super().__init__(report_type)

    def parse_file(
        self, file_path: str
    ) -> defaultdict[str, defaultdict[str, int]]:
        stats: defaultdict[str, defaultdict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )
        for key, level in parse_log_file(file_path, self.report_type):
            stats[key][level] += 1
        return stats

    def combine_results(
            self, results: list[defaultdict[str, defaultdict[str, int]]]
    ) -> defaultdict[str, defaultdict[str, int]]:
        combined: defaultdict[str, defaultdict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )
        for result in results:
            for key, levels in result.items():
                for level, count in levels.items():
                    combined[key][level] += count
        return combined


class GenericReportCalculator(BaseReportCalculator):
    def calculate_totals(
            self, data: defaultdict[str, defaultdict[str, int]]
    ) -> tuple[int, defaultdict[str, int]]:
        total_counts: defaultdict[str, int] = defaultdict(int)
        total_requests = 0

        for key in sorted(data.keys()):
            counts = [data[key].get(level, 0) for level in LOG_LEVELS]
            total_requests += sum(counts)
            for level, count in zip(LOG_LEVELS, counts):
                total_counts[level] += count

        return total_requests, total_counts

    def calculate_key_width(
        self, data: defaultdict[str, defaultdict[str, int]]
    ) -> int:
        max_key_length = max(len(key) for key in data.keys()) if data else 0
        return max_key_length + 5


class GenericReportFormatter(BaseReportFormatter):
    def __init__(self, calculator, header_name: str):
        self.calculator = calculator
        self.header_name = header_name

    def format_report(
        self, data: defaultdict[str, defaultdict[str, int]]
    ) -> str:
        total_requests, total_counts = self.calculator.calculate_totals(data)
        key_width = self.calculator.calculate_key_width(data)
        row_format = get_row_format_template(key_width)

        rows = [
            f'Total requests: {total_requests}\n',
            row_format.format(self.header_name, *LOG_LEVELS),
            *[row_format.format(key, *[data[key].get(level, 0)
                                       for level in LOG_LEVELS])
              for key in sorted(data.keys())],
            row_format.format('TOTAL', *[total_counts[level]
                                         for level in LOG_LEVELS])
        ]
        return '\n'.join(rows)


class GenericReport(BaseReport):
    def __init__(self, report_type: str, header_name: str):
        super().__init__(report_type, header_name)
        self.parser = GenericLogParser(report_type)
        self.calculator = GenericReportCalculator()
        self.formatter = GenericReportFormatter(self.calculator, header_name)

    def process_file(
        self, file_path: str
    ) -> defaultdict[str, defaultdict[str, int]]:
        return self.parser.parse_file(file_path)

    def combine_results(
        self, results: list[defaultdict[str, defaultdict[str, int]]]
    ) -> defaultdict[str, defaultdict[str, int]]:
        return self.parser.combine_results(results)

    def generate_report(
        self, data: defaultdict[str, defaultdict[str, int]]
    ) -> str:
        return self.formatter.format_report(data)

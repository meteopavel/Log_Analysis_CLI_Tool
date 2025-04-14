from collections import defaultdict

from config.constants import LOG_LEVELS, ROW_FORMAT
from reports.base import (
    BaseLogParser, BaseReportCalculator, BaseReportFormatter
)
from utils.log_parser import parse_log_file


class HandlersLogParser(BaseLogParser):
    def parse_file(self, file_path: str) -> dict[str, dict[str, int]]:
        stats = defaultdict(lambda: defaultdict(int))
        for handler, level in parse_log_file(file_path):
            stats[handler][level] += 1
        return stats

    def combine_results(
            self, results: list[dict[str, dict[str, int]]]
    ) -> dict[str, dict[str, int]]:
        combined = defaultdict(lambda: defaultdict(int))
        for result in results:
            for handler, levels in result.items():
                for level, count in levels.items():
                    combined[handler][level] += count
        return combined


class HandlersReportCalculator(BaseReportCalculator):
    def calculate_totals(
            self, data: dict[str, dict[str, int]]
    ) -> tuple[int, dict[str, int]]:
        total_counts = defaultdict(int)
        total_requests = 0

        for handler in sorted(data.keys()):
            counts = [data[handler].get(level, 0) for level in LOG_LEVELS]
            total_requests += sum(counts)
            for level, count in zip(LOG_LEVELS, counts):
                total_counts[level] += count

        return total_requests, total_counts


class HandlersReportFormatter(BaseReportFormatter):
    def __init__(self, calculator: BaseReportCalculator):
        self.calculator = calculator

    def format_report(self, data: dict[str, dict[str, int]]) -> str:
        total_requests, total_counts = self.calculator.calculate_totals(data)

        rows = [
            f'Total requests: {total_requests}\n',
            ROW_FORMAT.format('HANDLER', *LOG_LEVELS),
            *[ROW_FORMAT.format(handler, *[data[handler].get(level, 0)
                                           for level in LOG_LEVELS])
              for handler in sorted(data.keys())],
            ROW_FORMAT.format('TOTAL', *[total_counts[level]
                                         for level in LOG_LEVELS])
        ]

        return '\n'.join(rows)


class HandlersReport:
    def __init__(self):
        self.parser = HandlersLogParser()
        self.calculator = HandlersReportCalculator()
        self.formatter = HandlersReportFormatter(self.calculator)

    def process_file(self, file_path: str) -> dict[str, dict[str, int]]:
        return self.parser.parse_file(file_path)

    def combine_results(
            self, results: list[dict[str, dict[str, int]]]
    ) -> dict[str, dict[str, int]]:
        return self.parser.combine_results(results)

    def generate_report(self, data: dict[str, dict[str, int]]) -> str:
        return self.formatter.format_report(data)

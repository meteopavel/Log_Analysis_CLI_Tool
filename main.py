import argparse
from concurrent.futures import ThreadPoolExecutor
from reports.factory import ReportFactory
from utils.file_validator import validate_files_exist


def parse_args():
    parser = argparse.ArgumentParser(description='Log Analyzer')
    parser.add_argument('files', nargs='+', help='Paths to log files')
    parser.add_argument('--report', required=True,
                        help='Report type to generate')
    return parser.parse_args()


def main():
    args = parse_args()
    validate_files_exist(args.files)
    report_generator = ReportFactory.create_report(args.report.lower())
    with ThreadPoolExecutor() as executor:
        processed_data = list(
            executor.map(report_generator.process_file, args.files)
        )
    combined_data = report_generator.combine_results(processed_data)
    print(report_generator.generate_report(combined_data))


if __name__ == '__main__':
    main()

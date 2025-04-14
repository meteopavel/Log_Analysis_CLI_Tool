from importlib import import_module
from config.constants import REPORT_TYPES


class ReportFactory:
    @staticmethod
    def create_report(report_type: str):
        if report_type not in REPORT_TYPES:
            raise ValueError(f'Unknown report type: {report_type}')
        module_path, class_name = REPORT_TYPES[report_type].rsplit('.', 1)
        module = import_module(module_path)
        report_class = getattr(module, class_name)
        return report_class()

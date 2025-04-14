import pytest

from reports.factory import ReportFactory
from reports.registry import HandlersReport


def test_create_report_success():
    """
    Тестирует успешное создание отчета для зарегистрированного типа.
    """
    report_type = 'handlers'
    report = ReportFactory.create_report(report_type)

    assert isinstance(report, HandlersReport)
    assert report.report_type == 'handlers'


def test_create_report_unknown_type():
    """
    Тестирует обработку неизвестного типа отчета.
    """
    unknown_report_type = 'unknown_report'
    with pytest.raises(ValueError) as exc_info:
        ReportFactory.create_report(unknown_report_type)

    assert str(exc_info.value) == f'Unknown report type: {unknown_report_type}'

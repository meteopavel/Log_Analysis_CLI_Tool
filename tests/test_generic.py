from collections import defaultdict

from reports.generic import GenericLogParser


def test_parse_file(temp_log_file):
    """
    Тестирует парсинг логов из файла.
    """
    parser = GenericLogParser(report_type='handlers')
    stats = parser.parse_file(temp_log_file)

    assert isinstance(stats, defaultdict)
    assert stats['/api/v1/reviews/']['INFO'] == 1
    assert stats['/admin/dashboard/']['ERROR'] == 1


def test_combine_results():
    """
    Тестирует объединение результатов из нескольких источников.
    """
    parser = GenericLogParser(report_type='handlers')
    results = [
        {'/api/v1/reviews/': {'INFO': 1}},
        {'/admin/dashboard/': {'ERROR': 1}},
        {'/api/v1/reviews/': {'INFO': 2}},
    ]
    combined = parser.combine_results(results)

    assert combined['/api/v1/reviews/']['INFO'] == 3
    assert combined['/admin/dashboard/']['ERROR'] == 1


def test_calculate_totals():
    """
    Тестирует подсчет общего количества запросов и уровней логирования.
    """
    from reports.generic import GenericReportCalculator
    calculator = GenericReportCalculator()

    data = {
        '/api/v1/reviews/': {'INFO': 2, 'ERROR': 1},
        '/admin/dashboard/': {'ERROR': 1},
    }
    total_requests, total_counts = calculator.calculate_totals(data)

    assert total_requests == 4
    assert total_counts['INFO'] == 2
    assert total_counts['ERROR'] == 2


def test_calculate_key_width():
    """
    Тестирует расчет максимальной ширины ключа.
    """
    from reports.generic import GenericReportCalculator
    calculator = GenericReportCalculator()

    data = {
        '/api/v1/reviews/': {'INFO': 2},
        '/admin/dashboard/': {'ERROR': 1},
    }
    key_width = calculator.calculate_key_width(data)

    assert key_width == len('/admin/dashboard/') + 5


def test_format_report():
    """
    Тестирует форматирование отчета.
    """
    from reports.generic import GenericReportCalculator, GenericReportFormatter
    calculator = GenericReportCalculator()
    formatter = GenericReportFormatter(calculator, header_name='Handler')

    data = {
        '/api/v1/reviews/': {'INFO': 2, 'ERROR': 1},
        '/admin/dashboard/': {'ERROR': 1},
    }
    report = formatter.format_report(data)

    assert 'Total requests: 4' in report
    assert '/api/v1/reviews/' in report
    assert '/admin/dashboard/' in report
    assert 'TOTAL' in report


def test_process_file(temp_log_file):
    """
    Тестирует обработку файла.
    """
    from reports.generic import GenericReport
    report = GenericReport(report_type='handlers', header_name='Handler')
    stats = report.process_file(temp_log_file)

    assert isinstance(stats, defaultdict)
    assert stats['/api/v1/reviews/']['INFO'] == 1


def test_generate_report():
    """
    Тестирует генерацию отчета.
    """
    from reports.generic import GenericReport
    report = GenericReport(report_type='handlers', header_name="Handler")

    data = {
        '/api/v1/reviews/': {'INFO': 2, 'ERROR': 1},
        '/admin/dashboard/': {'ERROR': 1},
    }
    formatted_report = report.generate_report(data)

    assert 'Total requests: 4' in formatted_report
    assert '/api/v1/reviews/' in formatted_report
    assert '/admin/dashboard/' in formatted_report
    assert 'TOTAL' in formatted_report

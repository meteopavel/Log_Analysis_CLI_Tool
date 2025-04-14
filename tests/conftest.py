import pytest


@pytest.fixture
def log_data():
    """
    Фикстура с общими тестовыми данными для логов.
    """
    return {
        'valid': [
            '2025-03-28 12:44:46,000 INFO django.request: GET \
             /api/v1/reviews/ 204 OK [192.168.1.59]',
            '2025-03-28 12:21:51,000 ERROR django.request: \
             Internal Server Error: /admin/dashboard/ \
             [192.168.1.29] - ValueError: Invalid input data',
        ],
        'invalid': [
            'Invalid log line',
            'This is not a valid log entry',
        ],
    }


@pytest.fixture
def valid_log_lines(log_data):
    """
    Фикстура с валидными тестовыми строками логов.
    """
    return log_data['valid']


@pytest.fixture
def invalid_log_lines(log_data):
    """
    Фикстура с невалидными тестовыми строками логов.
    """
    return log_data['invalid']


@pytest.fixture
def log_line_fixture(request, log_data):
    """
    Фикстура для выбора строк логов (валидных или невалидных).
    """
    param, index = request.param
    if param in log_data:
        return log_data[param][index]
    else:
        raise ValueError("Unsupported parameter for log_line_fixture")


@pytest.fixture
def temp_log_file(tmp_path, log_data):
    """
    Фикстура для создания временного файла логов.
    """
    file_path = tmp_path / 'temp.log'
    file_path.write_text('\n'.join(log_data['valid']))
    return file_path

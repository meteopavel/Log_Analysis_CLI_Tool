import pytest
from config.constants import LOG_PATTERNS


@pytest.mark.parametrize(
    'log_line_fixture, expected_handler',
    [
        (('valid', 0), '/api/v1/reviews/'),
        (('valid', 1), '/admin/dashboard/'),
    ],
    indirect=['log_line_fixture']
)
def test_parse_valid_log_line(log_line_fixture, expected_handler):
    """
    Тестирует успешный парсинг валидных строк логов.
    """
    pattern = LOG_PATTERNS['handlers']
    match = pattern.match(log_line_fixture)

    assert match is not None
    assert match.group('handler') == expected_handler


@pytest.mark.parametrize(
    'log_line_fixture',
    [
        ('invalid', 0),
        ('invalid', 1),
    ],
    indirect=True
)
def test_parse_invalid_log_line(log_line_fixture):
    """
    Тестирует обработку невалидных строк логов.
    """
    pattern = LOG_PATTERNS['handlers']
    match = pattern.match(log_line_fixture)

    assert match is None

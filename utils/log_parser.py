from config.constants import HANDLERS_LOG_PATTERN


def parse_log_line(line: str) -> tuple[str | None, str | None]:
    """
    Парсит строку лога и возвращает уровень логирования и путь к API-ручке.
    Если строка не соответствует формату, возвращает (None, None).
    """
    match = HANDLERS_LOG_PATTERN.match(line)
    if not match:
        return None, None
    level = match.group('level').upper()
    handler = match.group('handler')
    return level, handler


def parse_log_file(file_path: str) -> list[tuple[str, str]]:
    """
    Читает файл логов и возвращает пары (handler, level).
    """
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            level, handler = parse_log_line(line)
            if level and handler:
                result.append((handler, level))
    return result
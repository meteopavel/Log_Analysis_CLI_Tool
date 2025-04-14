from config.constants import LOG_PATTERNS, LOG_LEVELS


def parse_log_line(
        line: str, report_type: str
        ) -> tuple[str | None, str | None]:
    """
    Парсит строку лога и возвращает уровень логирования
    и дополнительную информацию.
    Если строка не соответствует формату, возвращает (None, None).
    """
    pattern = LOG_PATTERNS.get(report_type)
    if not pattern:
        raise ValueError(f'Unknown report type: {report_type}')
    match = pattern.match(line)
    if not match:
        return None, None

    groups = match.groupdict()
    level = groups.get('level').upper()
    info_groups = [key for key in groups.keys()
                   if key not in ('timestamp', 'level')]
    info = next((groups[key] for key in info_groups if groups[key]), None)

    return level, info


def parse_log_file(
        file_path: str, report_type: str
        ) -> list[tuple[str, str]]:
    """
    Читает файл логов и возвращает пары (handler, level).
    """
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            level, handler = parse_log_line(line, report_type)
            if level and handler:
                result.append((handler, level))
    return result


def get_row_format_template(key_width: int) -> str:
    """
    Возвращает формат строки с учетом динамической ширины ключа.
    """
    return f'{{:<{key_width}}}' + ' '.join('{:<10}' for _ in LOG_LEVELS)

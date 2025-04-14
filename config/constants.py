import re

REPORT_TYPES = {
    'handlers': 'reports.handlers.HandlersReport',
}
HANDLERS_LOG_PATTERN = re.compile(
    r'^(?P<timestamp>.+?)\s+'
    r'(?P<level>\w+)\s+'
    r'django\.request:\s+'
    r'.*?(?P<handler>/[^\s\]]+)'
)
LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
ROW_FORMAT = '{:<25}' + ' '.join('{:<10}' for _ in LOG_LEVELS)

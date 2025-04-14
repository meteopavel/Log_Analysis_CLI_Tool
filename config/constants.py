import re

REPORT_TYPES = {
    'handlers': 'reports.registry.HandlersReport',
    # Раскомментируйте для добавления других типов отчета:
    # 'management': 'reports.registry.ManagementReport',
    # 'backends': 'reports.registry.BackendsReport',
}

LOG_PATTERNS = {
    'handlers': re.compile(
        r'^(?P<timestamp>.+?)\s+'
        r'(?P<level>\w+)\s+'
        r'django\.request:\s+'
        r'.*?(?P<handler>/[^\s\]]+)'
    ),
    # Раскомментируйте для добавления регулярного выражения для других
    # типов отчета:
    # 'management': re.compile(
    #     r'^(?P<timestamp>.+?)\s+'
    #     r'(?P<level>\w+)\s+'
    #     r'django\.core\.management:\s+'
    #     r'.*?(?P<message>.+)'
    # ),
    # 'backends': re.compile(
    #     r'^(?P<timestamp>.+?)\s+'
    #     r'(?P<level>\w+)\s+'
    #     r'django\.db\.backends:\s+'
    #     r'.*?(?P<query>.+)'
    # ),
}

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

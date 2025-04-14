from reports.generic import GenericReport


class HandlersReport(GenericReport):
    def __init__(self):
        super().__init__(report_type='handlers', header_name='HANDLER')


class ManagementReport(GenericReport):
    def __init__(self):
        super().__init__(report_type='management', header_name='MESSAGE')


class BackendsReport(GenericReport):
    def __init__(self):
        super().__init__(report_type='backends', header_name='QUERY')

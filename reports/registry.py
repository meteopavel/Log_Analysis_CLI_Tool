from reports.generic import GenericReport


class HandlersReport(GenericReport):
    def __init__(self):
        super().__init__(report_type='handlers', header_name='HANDLER')


# Раскомментируйте эти классы чтобы добавить другие виды отчетов
# class ManagementReport(GenericReport):
#     def __init__(self):
#         super().__init__(report_type='management', header_name='MESSAGE')


# class BackendsReport(GenericReport):
#     def __init__(self):
#         super().__init__(report_type='backends', header_name='QUERY')


# class NewReport(GenericReport):
#     def __init__(self):
#         super().__init__(report_type='new_report', header_name='NEW')

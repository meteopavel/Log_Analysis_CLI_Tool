from abc import ABC, abstractmethod
from collections import defaultdict


class BaseLogParser(ABC):
    def __init__(self, report_type: str):
        """
        Инициализирует парсер с указанным типом отчета.
        :param report_type: Тип отчета (например, 'handlers', 'levels').
        """
        self.report_type = report_type

    @abstractmethod
    def parse_file(
        self, file_path: str
    ) -> defaultdict[str, defaultdict[str, int]]:
        """
        Парсит файл логов и возвращает статистику.
        :param file_path: Путь к файлу логов.
        :return: defaultdict с статистикой (ключи - строки,
        значения - defaultdict уровней логирования).
        """
        pass

    @abstractmethod
    def combine_results(
            self, results: list[defaultdict[str, defaultdict[str, int]]]
    ) -> defaultdict[str, defaultdict[str, int]]:
        """
        Объединяет статистику из нескольких файлов.
        :param results: Список defaultdict с статистикой.
        :return: Объединенный defaultdict с статистикой.
        """
        pass


class BaseReportCalculator(ABC):
    @abstractmethod
    def calculate_totals(
            self, data: defaultdict[str, defaultdict[str, int]]
    ) -> tuple[int, defaultdict[str, int]]:
        """
        Вычисляет общее количество запросов и итоговые значения для каждого
        уровня логирования.
        :param data: defaultdict с статистикой.
        :return: Кортеж (общее количество запросов, defaultdict с итогами по
        уровням логирования).
        """
        pass

    @abstractmethod
    def calculate_key_width(
        self, data: defaultdict[str, defaultdict[str, int]]
    ) -> int:
        """
        Вычисляет максимальную длину ключей в данных.
        :param data: defaultdict с статистикой.
        :return: Максимальная длина ключей с запасом в 5 символов.
        """
        pass


class BaseReportFormatter(ABC):
    @abstractmethod
    def format_report(
        self, data: defaultdict[str, defaultdict[str, int]]
    ) -> str:
        """
        Форматирует отчет на основе предоставленных данных.
        :param data: defaultdict с статистикой (ключи - строки,
        значения - defaultdict уровней логирования).
        :return: Отформатированный отчет в виде строки.
        """
        pass


class BaseReport(ABC):
    def __init__(self, report_type: str, header_name: str):
        """
        Инициализирует отчет с указанным типом и заголовком.
        :param report_type: Тип отчета (например, 'handlers', 'levels').
        :param header_name: Заголовок для отчета.
        """
        self.report_type = report_type
        self.header_name = header_name

    @abstractmethod
    def process_file(
        self, file_path: str
    ) -> defaultdict[str, defaultdict[str, int]]:
        """
        Обрабатывает один файл и возвращает статистику.
        :param file_path: Путь к файлу логов.
        :return: defaultdict с статистикой.
        """
        pass

    @abstractmethod
    def combine_results(
            self, results: list[defaultdict[str, defaultdict[str, int]]]
    ) -> defaultdict[str, defaultdict[str, int]]:
        """
        Объединяет статистику из нескольких файлов.
        :param results: Список словарей с статистикой.
        :return: Объединенный defaultdict с статистикой.
        """
        pass

    @abstractmethod
    def generate_report(
        self, data: defaultdict[str, defaultdict[str, int]]
    ) -> str:
        """
        Форматирует отчет для вывода в консоль.
        :param data: defaultdict с статистикой.
        :return: Отформатированный отчет в виде строки.
        """
        pass

from abc import ABC, abstractmethod


class BaseLogParser(ABC):
    def __init__(self, report_type: str):
        self.report_type = report_type

    @abstractmethod
    def parse_file(self, file_path: str) -> dict[str, dict[str, int]]:
        """
        Парсит файл логов и возвращает статистику.
        """
        pass

    @abstractmethod
    def combine_results(
            self, results: list[dict[str, dict[str, int]]]
    ) -> dict[str, dict[str, int]]:
        """
        Объединяет статистику из нескольких файлов.
        """
        pass


class BaseReportCalculator(ABC):
    @abstractmethod
    def calculate_totals(
            self, data: dict[str, dict[str, int]]
    ) -> tuple[int, dict[str, int]]:
        """
        Вычисляет общее количество запросов и итоговые значения
        для каждого уровня логирования.
        """
        pass

    @abstractmethod
    def calculate_key_width(self, data: dict[str, dict[str, int]]) -> int:
        """
        Вычисляет максимальную длину ключей в данных.
        Добавляем запас в 5 символов для лучшего визуального восприятия.
        """
        pass


class BaseReportFormatter(ABC):
    @abstractmethod
    def format_report(self, data: dict[str, dict[str, int]]) -> str:
        """
        Форматирует отчет для вывода в консоль.
        """
        pass


class BaseReport(ABC):
    def __init__(self, report_type: str):
        self.report_type = report_type

    @abstractmethod
    def process_file(self, file_path: str) -> dict:
        """
        Обрабатывает один файл и возвращает статистику.
        """
        pass

    @abstractmethod
    def combine_results(self, results: list[dict]) -> dict:
        """
        Объединяет статистику из нескольких файлов.
        """
        pass

    @abstractmethod
    def generate_report(self, data: dict) -> str:
        """
        Форматирует отчет для вывода в консоль.
        """
        pass

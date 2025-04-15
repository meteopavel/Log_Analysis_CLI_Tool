<!-- Pytest --><a href="https://docs.pytest.org/en/stable/contents.html/"><img src="./images/pytest.svg"></a>


<div align="center">
  <a href="https://github.com/meteopavel/Log_Analysis_CLI_Tool">
    <img src="./images/logo.svg" alt="Logo" width="250" height="auto">
  </a>
  <h1 align="center">Log Analysis CLI Tool 📊</h1>
  <p align="center">
    🔧 CLI-приложение для анализа логов Django-приложений. Позволяет формировать отчеты о состоянии API-ручек по уровням логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    <br /><br />
    <a href="https://meteopavel.space">Сайт разработчика</a>
    ·
    <a href="https://github.com/meteopavel/Log_Analysis_CLI_Tool/issues/new?labels=bug">Сообщить об ошибке</a>
    ·
    <a href="https://github.com/meteopavel/Log_Analysis_CLI_Tool/issues/new?labels=enhancement">Предложить улучшение</a>
  </p>
</div>


## Особенности ✨

- Параллельная обработка нескольких файлов 🔀
- Поддержка больших файлов (несколько ГБ) 💾
- Расширяемая архитектура для добавления новых отчетов 🛠️
- Простой интерфейс командной строки 💻

## Требования 📋

- Python 3.9 или выше (протестировано на версии 3.10)

## Установка ⚙️

1. **Склонируйте репозиторий**:
   ```bash
   git clone https://github.com/meteopavel/Log_Analysis_CLI_Tool.git
   cd ./Log_Analysis_CLI_Tool
   ```
2. **Установите виртуальное окружение**:
   ```bash
   # Для Linux/MacOS
   python3 -m venv venv

   # Для Windows
   python -m venv venv
   ```   
3. **Активируйте виртуальное окружение**:
   ```bash
   # Для Linux/MacOS
   source venv/bin/activate

   # Для Windows
   source venv/Scripts/activate
   ```
4. **Обновите pip**:
   ```bash
   python -m pip install --upgrade pip
   ```
5. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Проверьте установку**:
   ```bash
   python main.py --help
   ```

## Использование 🚀
   ```bash
   # Для Linux/MacOS
   python3 main.py logs/app1.log logs/app2.log logs/app3.log --report handlers

   # Для Windows
   python main.py logs/app1.log logs/app2.log logs/app3.log --report handlers
   ```
   ### Аргументы командной строки:
   - `logs/app1.log logs/app2.log`: Пути к файлам логов (можно указать несколько файлов).
   - `--report handlers`: Название отчета для генерации.
   ### Пример вывода:
   ```
   Total requests: 72

   HANDLER                DEBUG   INFO    WARNING ERROR   CRITICAL  
   /admin/dashboard/      0       5       1       2       0        
   /api/v1/auth/login/    0       4       0       0       0        
   /api/v1/cart/          0       3       0       0       0        
   /api/v1/checkout/      0       5       0       1       0        
   /api/v1/orders/        0       3       0       1       0        
   /api/v1/payments/      0       6       0       0       0        
   /api/v1/products/      0       4       0       0       0        
   /api/v1/reviews/       0       4       0       0       0        
   /api/v1/shipping/      0       1       0       1       0        
   /api/v1/support/       0       2       0       2       0        
   /api/v1/users/         0       4       0       0       0        
                          0       41      1       5       0
   ```

## Добавление нового типа отчета 🛠️
Процесс добавления нового типа отчета максимально упрощен благодаря использованию паттернов проектирования. На данный момент реализован только отчет `handlers`. Остальные типы отчетов (например, `management`, `backends`) закомментированы в коде для удобства просмотра и демонстрации того, как можно добавить новые типы.

1. Определите новый тип отчета
   Чтобы добавить новый тип отчета, раскомментируйте соответствующий класс в файле `reports/registry.py` или создайте новый класс на основе существующего шаблона. Например:
   ```bash
      class NewReportType(GenericReport):
         def init (self):
            super().init (report_type='new_report', header_name='NEW_HEADER')

      # Раскомментируйте эти классы чтобы добавить другие виды отчетов
      # class ManagementReport(GenericReport):
      #     def __init__(self):
      #         super().__init__(report_type='management' header_name='MESSAGE')


      # class BackendsReport(GenericReport):
      #     def __init__(self):
      #         super().__init__(report_type='backends', header_name='QUERY')
   ```
2. Зарегистрируйте новый тип в конфигурации
   Обновите словарь REPORT_TYPES в файле config/constants.py:
   ```bash
   REPORT_TYPES = {
      'handlers': 'reports.registry.HandlersReport',
      # Раскомментируйте для добавления других типов отчета:
      # 'management': 'reports.registry.ManagementReport',  
      # 'backends': 'reports.registry.BackendsReport',  
      # 'new_report': 'reports.registry.NewReportType',
   }
   ```

3. Добавьте регулярное выражение для парсинга
   Если новый тип отчета требует уникального формата логов, добавьте соответствующее регулярное выражение в config/patterns.py:
   ```bash
   LOG_PATTERNS = {
      'handlers': re.compile(...),
      # Раскомментируйте для добавления регулярного выражения для других
      # типов отчета:
      # 'management': re.compile(...),  
      # 'backends': re.compile(...),  
      # 'new_report': re.compile(...),
   }
   ```

4. Тестируйте новый тип отчета
   После добавления нового типа отчета протестируйте его, запустив приложение с указанием типа отчета. Например:
   ```bash
   python main.py logs/app1.log --report new_report
   ```

## Используемые паттерны проектирования 🏗️
1. Фабричный метод (Factory Method):
   - Фабрика (`reports/factory.py`) динамически создает экземпляры отчетов на основе входных данных.
   - Это позволяет легко добавлять новые типы отчетов без изменения существующего кода.
2. Реестр (Registry):
   - Все типы отчетов регистрируются в одном месте (`reports/registry.py`).
   - Это упрощает управление и расширение функциональности.
3. Шаблонный метод (Template Method):
   - Базовый класс `GenericReport` определяет общий алгоритм работы с отчетами, а конкретные реализации переопределяют только те части, которые отличаются.
4. DRY (Don't Repeat Yourself):
   - Общая логика (парсинг, подсчет статистики, форматирование) вынесена в базовые классы, что минимизирует дублирование кода.

## Тестирование 🧪
Для тестирования используется pytest. Запустите тесты следующим образом:
```bash
pytest tests/
```

## Архитектура 🏗️
Проект использует только стандартную библиотеку Python. Основные модули:

- `argparse` : Обработка аргументов командной строки.
- `concurrent.futures.ThreadPoolExecutor` : Параллельная обработка файлов.
- `re`: Работа с регулярными выражениями для парсинга логов.
- `collections.defaultdict` : Хранение данных в удобной структуре.
- `pathlib.Path` : Работа с путями к файлам.
- `pytest` (только для тестирования): Работа с юнит-тестами.

## Автор
[Павел Найденов](https://github.com/meteopavel)

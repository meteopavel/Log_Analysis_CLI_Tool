# Log Analysis CLI Tool 📊

CLI-приложение для анализа логов Django-приложений. Позволяет формировать отчеты о состоянии API-ручек по уровням логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL).

## Особенности ✨

- Параллельная обработка нескольких файлов 🔀
- Поддержка больших файлов (несколько ГБ) 💾
- Расширяемая архитектура для добавления новых отчетов 🛠️
- Простой интерфейс командной строки 💻

## Требования 📋

- Python 3.8 или выше (протестировано на версии 3.10)

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
   python3 main.py logs/app1.log logs/app2.log logs/app3.log --report handlers
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
- `pytest` (только для тестирования): работа с юнит-тестами.

## Автор
[Павел Найденов](https://github.com/meteopavel)
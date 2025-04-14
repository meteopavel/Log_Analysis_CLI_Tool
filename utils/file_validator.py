from pathlib import Path


def validate_files_exist(file_paths: list[str]) -> None:
    """Проверяет, что все указанные файлы существуют."""
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists() or not path.is_file():
            raise FileNotFoundError(f'File not found: {file_path}')

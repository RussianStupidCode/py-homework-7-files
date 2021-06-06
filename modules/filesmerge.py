from pathlib import Path
import os


def get_file_content(file_path):
    file_name = os.path.basename(file_path)
    result = ""

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        lines_count = file_content.count('\n') + 1
        result = f'{file_name}\n{lines_count}\n{file_content}\n'

    return result


def files_merge(src_directory, result_file):
    files = Path(src_directory).glob('*.txt')
    files_content = []
    for file in files:
        files_content.append(get_file_content(file))

    files_content.sort(key=lambda item: item.count('\n'))

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write("".join(files_content))
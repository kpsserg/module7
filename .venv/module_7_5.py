# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
#
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.

import os
import time

current_dir = os.getcwd()
print(current_dir)
root = os.path.dirname(current_dir)
print(os.listdir())
files = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]

print(dirs)
print(files)

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = (os.path.join(root, file))
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(root)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {root}')
        # print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}, Родительская директория: {parent_dir}')
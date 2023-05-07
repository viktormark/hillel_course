# Написать скрипт, который подсчитает количество папок и файлов по заданному пути.
# Если такого нет, то по всей системе(/ - для линукс/мак. Диск С - для виндоус).
# Для удобства можно установить граничное значение числа папок(и/или файлов), после которого скрипт не будет продолжать работу.
# Среди найденных файлов показать самый большой и самый маленький по размеру, а так же с самым длинным и коротким именем.
# Если во время работы скрипт был прерван(KeyboardInterrupt),
# то промежуточные результаты сериализуются в файл и при повторном запуске эти пути исключаются из проверки.


import json
import os

max_files = 20
my_path = r"C:\Users\vikto\OneDrive\Робочий стіл\hillel\les7"
progress_file = "progress.json"


def count_all(path):
    count_dis_and_files = 0
    longest_name = ""
    shortest_name = ""
    largest_file = ""
    largest_size = 0
    smallest_file = ""
    smallest_size = float('inf')

    if os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            progress = json.load(f)
            count_dis_and_files = progress.get("count", 0)
            longest_name = progress.get("longest_name", "")
            shortest_name = progress.get("shortest_name", "")
            largest_file = progress.get("largest_file", "")
            largest_size = progress.get("largest_size", 0)
            smallest_file = progress.get("smallest_file", "")
            smallest_size = progress.get("smallest_size", float('inf'))

    try:
        for root, dirs, files in os.walk(path):
            count_dis_and_files += len(dirs) + len(files)

            if count_dis_and_files >= max_files:
                print(f"Достигнуто граничное значение - {max_files}")
                break

            for file_name in files + dirs:
                if len(file_name) > len(longest_name):
                    longest_name = file_name
                if len(shortest_name) == 0 or len(file_name) < len(shortest_name):
                    shortest_name = file_name

                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path)
                    if file_size > largest_size:
                        largest_size = file_size
                        largest_file = file_name
                    if file_size < smallest_size:
                        smallest_size = file_size
                        smallest_file = file_name

                progress = {
                    "count": count_dis_and_files,
                    "longest_name": longest_name,
                    "shortest_name": shortest_name,
                    "largest_file": largest_file,
                    "largest_size": largest_size,
                    "smallest_file": smallest_file,
                    "smallest_size": smallest_size
                }

                with open(progress_file, 'w') as f:
                    json.dump(progress, f)

    except KeyboardInterrupt:
        print("Процесс был прерван пользователем.")

    print("Общее количество папок и файлов:", count_dis_and_files)
    print("Самое длинное имя:", longest_name)
    print("Самое короткое имя:", shortest_name)
    print("Самый большой файл по размеру:", largest_file)
    print("Самый маленький файл по размеру:", smallest_file)

    if os.path.exists(progress_file):
        os.remove(progress_file)

if os.path.exists(my_path):
    count_all(my_path)
else:
    count_all("C:/")
import csv


def all_tables(files):
    all_data = []

    for file in files:
        try:
            with open(file, encoding='utf-8') as f:
                reader = csv.reader(f)
                file_data = list(reader)
                # сохраняем заголовки столбцов из первого файла
                if file == files[0]:
                    all_data.append(file_data[0])
                # далее добавляем только строки с данными
                all_data.extend(file_data[1:])
        except FileNotFoundError:
            print('****************************************')
            print(f'ВНИМАНИЕ! Ошибка: Файл {file} не найден. Проверьте написание и/или расположение файла.')
            print('****************************************')

    # print(all_data)

    return all_data

import argparse, os

from all_tables import all_tables
from average_rating import average_rating
from other_report import other_report


def main(args=None):
    parser = argparse.ArgumentParser(
        description='Обработка CSV файлов и генерация отчетов',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
    Примеры использования:
      python main.py --files data1.csv data2.csv --report average-rating
      python main.py -f products.csv reviews.csv -r average-rating
            '''
    )

    parser.add_argument(
        '--files', '-f',
        nargs='+',
        required=True,
        help='CSV файлы для обработки (можно указать несколько)'
    )

    parser.add_argument(
        '--report', '-r',
        required=True,
        choices=['average-rating', 'other-report'],  # можно добавить другие типы отчетов
        help='Тип отчета для генерации'
    )

    args = parser.parse_args(args)

    files = args.files

    # проверяем наличие пути к файлу иначе берем файл из папки tables/ или корня скрипта
    for i in range(len(files)):
        if '/' not in files[i]:
            if os.path.exists('tables/' + files[i]):
                files[i] = 'tables/' + files[i]
                # print(files[i])
            else:
                files[i] = files[i]
                # print(files[i])

    # собираем данные из таблиц в один список
    all_data = all_tables(files)

    # запускаем отчет в соответствии с аргументом
    if args.report == 'average-rating':
        average_rating(all_data)
    elif args.report == 'other-report':
        other_report(all_data)


if __name__ == "__main__":
    main()

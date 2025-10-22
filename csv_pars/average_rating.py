from tabulate import tabulate
from collections import defaultdict


def average_rating(all_data):
    if not all_data or len(all_data) <= 1:
        print("Нет данных для отчета")
        return

    # сохраняем только нужные столбцы
    selected_col = []

    for row in all_data:
        iter_list = [row[1], row[3]]
        selected_col.append(iter_list)

    headers = selected_col[0]
    rows = selected_col[1:]

    # print(rows)

    # группируем рейтинги по брендам
    brand_ratings = defaultdict(list)

    for row in rows:
        brand = row[0]  # первый столбец - бренд
        rating = float(row[1])  # второй столбец - рейтинг
        brand_ratings[brand].append(rating)

    # print(brand_ratings)
    # print(brand_ratings.items())

    # вычисляем средний рейтинг для каждого бренда
    result = []

    for brand, ratings in brand_ratings.items():
        avg_rating = sum(ratings) / len(ratings)
        # print(avg_rating)
        result.append([brand, round(avg_rating, 2)])

    # print(result)

    # сортируем по названию бренда
    result.sort(key=lambda x: x[1], reverse=True)

    # изменяем нумерацию строк по индексу
    mod_index = range(1, len(result) + 1)

    print('Отчет: средний рейтинг по брендам')
    print(tabulate(result, headers=headers, tablefmt='grid', showindex=mod_index))

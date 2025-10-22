import pytest
import csv
import os


@pytest.fixture
def sample_csv_data():
    # создание тестовых CSV файлов
    # создаем тестовую папку
    os.makedirs('test_data', exist_ok=True)

    # данные для первого файла
    with open('test_data/test1.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows([
            ['product', 'brand', 'price', 'rating'],
            ['Product1', 'BrandA', '1000', '4.5'],
            ['Product2', 'BrandA', '800', '4.2'],
            ['Product3', 'BrandB', '900', '4.0']
        ])

    # данные для второго файла
    with open('test_data/test2.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows([
            ['product', 'brand', 'price', 'rating'],
            ['Product4', 'BrandB', '600', '4.1'],
            ['Product5', 'BrandC', '400', '4.0'],
            ['Product6', 'BrandC', '350', '4.0']
        ])

    yield ['test_data/test1.csv', 'test_data/test2.csv']

    # очистка
    for file in ['test_data/test1.csv', 'test_data/test2.csv']:
        if os.path.exists(file):
            os.remove(file)
    if os.path.exists('test_data'):
        os.rmdir('test_data')


@pytest.fixture
def sample_all_data():
    # тестовые данные в формате all_data
    return [
        ['product', 'brand', 'price', 'rating'],
        ['Product1', 'BrandA', '1000', '4.5'],
        ['Product2', 'BrandA', '800', '4.2'],
        ['Product3', 'BrandB', '900', '4.0'],
        ['Product4', 'BrandB', '600', '4.1'],
        ['Product5', 'BrandC', '400', '4.0'],
        ['Product6', 'BrandC', '350', '4.0']
    ]

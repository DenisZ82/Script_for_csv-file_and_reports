from all_tables import all_tables


def test_all_tables_success(sample_csv_data):
    # тест объединения таблиц
    result = all_tables(sample_csv_data)

    assert len(result) == 7  # 1 заголовок + 6 строк данных
    assert result[0] == ['product', 'brand', 'price', 'rating']
    assert result[1] == ['Product1', 'BrandA', '1000', '4.5']
    assert result[6] == ['Product6', 'BrandC', '350', '4.0']


def test_all_tables_file_not_found(capsys):
    # тест с отсутствующим файлом
    result = all_tables(['nonexistent.csv'])

    captured = capsys.readouterr()
    assert 'не найден' in captured.out
    assert result == []


def test_all_tables_empty_list():
    # тест с пустым списком файлов
    result = all_tables([])
    assert result == []

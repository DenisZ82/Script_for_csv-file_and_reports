from average_rating import average_rating


def test_average_rating_output(sample_all_data, capsys):
    # тест вывода среднего рейтинга
    average_rating(sample_all_data)

    captured = capsys.readouterr()
    output = captured.out

    # проверяем основные элементы отчета
    assert 'Отчет: средний рейтинг по брендам' in output
    assert 'brand' in output
    assert 'rating' in output

    # проверяем что все бренды присутствуют
    assert 'BrandA' in output
    assert 'BrandB' in output
    assert 'BrandC' in output


def test_average_rating_empty_data(capsys):
    # тест с пустыми данными
    empty_data = [['brand', 'rating']]  # только заголовок
    average_rating(empty_data)

    captured = capsys.readouterr()
    assert 'Нет данных для отчета' in captured.out


def test_average_rating_sorting(sample_all_data, capsys):
    # тест правильности сортировки по рейтингу
    average_rating(sample_all_data)

    captured = capsys.readouterr()
    output = captured.out

    # Находим строки с брендами в выводе
    brand_c_index = output.find('BrandC')
    brand_b_index = output.find('BrandB')
    brand_a_index = output.find('BrandA')

    # print('C:', brand_c_index)
    # print('B:', brand_b_index)
    # print('A:', brand_a_index)

    # BrandC должен быть выше BrandB, BrandB выше BrandA
    assert brand_a_index < brand_b_index < brand_c_index

from main import main


def test_main_average_rating(sample_csv_data, capsys):
    # тест main с average-rating
    main(['--files'] + sample_csv_data + ['--report', 'average-rating'])

    captured = capsys.readouterr()
    assert 'Отчет: средний рейтинг по брендам' in captured.out


def test_main_other_report(sample_csv_data, capsys):
    #  тест main с other-report
    main(['-f'] + sample_csv_data + ['-r', 'other-report'])

    captured = capsys.readouterr()
    assert 'Отчет на доработке' in captured.out


def test_main_file_not_found(capsys):
    # тест main с отсутствующим файлом
    main(['--files', 'missing.csv', '--report', 'average-rating'])

    captured = capsys.readouterr()
    assert 'не найден' in captured.out

from other_report import other_report


def test_other_report_output(capsys):
    # тест other_report
    test_data = [['test', 'data']]
    other_report(test_data)

    captured = capsys.readouterr()
    assert 'Отчет на доработке' in captured.out

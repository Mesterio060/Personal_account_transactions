from utils import data_operation, get_filtered_data, get_count_last_operation, get_formatted_data


def test_data_operation():
    data = data_operation()
    assert isinstance(
        data, list
    )


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [
        {'date': '2019-12-05T09:37:15.543590',
         'description': 'Перевод организации',
         'from': 'Visa Platinum 28477438893689665',
         'id': 544872369,
         'operationAmount':
             {'amount': '454332.39',
              'currency':
                  {'code': 'USD',
                   'name': 'USD'}},
         'state': 'EXECUTED',
         'to': 'Счет 96158586384610753655'}]


def test_get_count_last_operation(test_data):
    data = get_count_last_operation(test_data)
    assert [a["date"] for a in data] == ['2019-12-07T06:17:14.634890', '2019-12-05T09:37:15.543590', '2019-12-01T09:11:54.754390', '2019-11-04T07:20:20.611890', '2019-10-05T11:32:11.124320']


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['04.11.2019 Открытие вклада\nОткрытие вклада  -> Счет **3332\n54150.89 USD', '05.12.2019 Перевод организации\nVisa Platinum 2847 74** **** 9665 -> Счет **3655\n454332.39 USD', '05.10.2019 Перевод организации\nMaestro 2842 87** **** 9012 -> Счет **3655\n467443.31 руб.', '01.12.2019 Перевод организации\nVisa Classic 4342 87** **** 4432 -> МИР **5391\n88425.11 USD', '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD']
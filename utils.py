import json
from datetime import datetime


def data_operation():
    """
    :return: Загружает данные из файла 'operations.json',
             и проверяет его на наличие пустых словарей
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    """
    :return: Фильтрация данных по статусу перевода (["state"] == "EXECUTED")
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_count_last_operation(data):
    """
    :param data: Сортирует данные из файла .json по ключу "date",
                 начиная с последней выполненной операции
    :return: Выводит определенное количество списков (count_last_operation),
             отсартированных по самым последним операциям (по дате)
    """
    data = sorted(data, key=lambda a: a["date"], reverse=True)
    data = data[:5]
    return data


def get_formatted_data(data):
    """
    :date_operation: Дата перевода представлена в формате ДД.ММ.ГГГГ
    :description: Добавленно описание перевода
    :getter_masked: Фунсция маскирует номер счета и не отображается целиком
    :operation_amount: Вывод суммы перевода и наименование валюты в которой был выполнен перевод
    :account_number: Фунскция макирует номер карты и не отображается целиком
    :account_info: Вывод наимменование карты отпраавителя
    :return: Вывод форматированных данных
    """
    formatted_data = []
    for a in data:
        date_operation = datetime.strptime(a["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = a["description"]
        getter_masked = f"{a['to'].split()[0]} **{a['to'][-4:]}"
        if "from" in a:
            sender_masked = a["from"].split()
            account_number_masked = sender_masked.pop(-1)
            account_number_masked = f"{account_number_masked [:4]} {account_number_masked [4:6]}** **** {account_number_masked [-4:]}"
            account_info = " ".join(sender_masked)
        else:
            account_info, account_number_masked = description, ""
        operation_amount = f"{a['operationAmount']['amount']} {a['operationAmount']['currency']['name']}"
        formatted_data.append(f"""\
{date_operation} {description}
{account_info} {account_number_masked} -> {getter_masked}
{operation_amount}""")
        print(formatted_data)
    return formatted_data

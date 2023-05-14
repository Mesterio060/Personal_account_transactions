from utils import data_operation, get_filtered_data, get_count_last_operation, get_formatted_data


def main():
    data = data_operation()
    data = get_filtered_data(data)
    data = get_count_last_operation(data)
    data = get_formatted_data(data)
    for a in data:
        print(a, end='\n\n')


if __name__ == "__main__":
    main()

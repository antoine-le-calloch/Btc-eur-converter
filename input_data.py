from datetime import datetime


def get_format(input_format):
    """
    Returns the date format based on the user input.
    :param input_format: Selected format
    :return: Date format string
    """
    if input_format == "1":
        return "%d-%m-%Y"
    elif input_format == "2":
        return "%m-%d-%Y"
    elif input_format == "3":
        return "%Y-%m-%d"
    else:
        print("Invalid date format. Defaulting to DD-MM-YYYY.")
        return "%d-%m-%Y"


def get_input_data():
    """
    Prompts the user to choose a date format, enter a date and Bitcoin quantity.
    :return: Selected format, date and Bitcoin quantity as a tuple
    """
    input_format = input("Select a date format (1: DD-MM-YYYY, 2: MM-DD-YYYY, 3: YYYY-MM-DD): ")
    date_format = get_format(input_format)

    input_date = input("Enter a date in the selected format: ")
    datetime.strptime(input_date, date_format)

    input_quantity = 0
    while input_quantity <= 0:
        input_quantity = float(input("Enter the amount of Bitcoin: "))
        if input_quantity <= 0:
            print("The Bitcoin amount must be a positive number.")

    return date_format, input_date, input_quantity

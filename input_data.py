from datetime import datetime


def get_format():
    """
    Prompts the user to select a date format.
    :return: Date format string
    """
    input_format = input("Select a date format (1: DD-MM-YYYY, 2: MM-DD-YYYY, 3: YYYY-MM-DD): ")
    if input_format == "1":
        return "%d-%m-%Y"
    elif input_format == "2":
        return "%m-%d-%Y"
    elif input_format == "3":
        return "%Y-%m-%d"
    else:
        print("Invalid date format. Defaulting to DD-MM-YYYY.")
        return "%d-%m-%Y"


def get_date_and_quantity(date_format):
    """
    Prompts the user to choose a date and Bitcoin quantity.
    :return: date and Bitcoin quantity as a tuple
    """
    input_date = None
    while input_date is None:
        input_date = input("Enter a date in the selected format: ")
        try:
            datetime.strptime(input_date, date_format)
        except ValueError:
            print("Invalid date format. Please try again.")
            input_date = None

    input_quantity = 0
    while input_quantity <= 0:
        try:
            input_quantity = float(input("Enter the amount of Bitcoin: "))
        except ValueError:
            input_quantity = 0
        if input_quantity <= 0:
            print("The Bitcoin amount must be a positive number.")

    return input_date, input_quantity

from input_data import get_date_and_quantity
from input_data import get_format
from cryptocompare_api import get_bitcoin_price_on_date

if __name__ == "__main__":
    """
    Main function to interact with the user and calculate the value in EUR.
    """
    date_format = get_format()
    while True:
        try:
            input_date, input_quantity = get_date_and_quantity(date_format)
            btc_price = get_bitcoin_price_on_date(input_date, date_format)
            if btc_price is None:
                print("Unable to fetch the Bitcoin price.")
            else:
                value = btc_price * input_quantity
                if value is not None:
                    print(f"The price of {input_quantity} BTC on {input_date} was approximately {value:.2f} EUR.")
                else:
                    print("Unable to calculate the value.")

            is_exit = input("Do you want to exit? (y/n): ")
            if is_exit.lower() == "y":
                break
        except ValueError as e:
            print(f"Error: {e}")

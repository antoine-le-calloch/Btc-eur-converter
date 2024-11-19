import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")


def get_bitcoin_price_on_date(date):
    """
    Fetches the Bitcoin price in EUR on a specific date using the CryptoCompare API.

    :param date: Date in format 'DD-MM-YYYY'
    :return: Bitcoin price in EUR on that date
    """
    

    try:
        
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
    except KeyError:
        print("Failed to parse the price data.")
    return None

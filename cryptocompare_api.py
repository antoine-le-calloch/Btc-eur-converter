import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")


def get_bitcoin_price_on_date(date, date_format):
    """
    Fetches the Bitcoin price in EUR on a specific date using the CryptoCompare API.
    :param date: Date to fetch the Bitcoin price
    :param date_format: Format of the date
    :return: Bitcoin price in EUR on that date
    """
    # Convert date to Unix timestamp
    timestamp = int(time.mktime(time.strptime(date, date_format)))
    url = f"https://min-api.cryptocompare.com/data/v2/histoday"
    params = {
        "fsym": "BTC",
        "tsym": "EUR",
        "limit": 1,
        "toTs": timestamp,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "Data" in data and "Data" in data["Data"]:
            btc_price = data["Data"]["Data"][-1]["close"]
            return btc_price
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    return None

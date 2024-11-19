import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("COINMARKETCAP_API_KEY")


def get_bitcoin_price_on_date(date):
    """
    Fetches the Bitcoin price in EUR on a specific date using the CoinMarketCap API.

    :param date: Date in format 'DD-MM-YYYY'
    :return: Bitcoin price in EUR on that date
    """
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {
        "start": "1",
        "limit": "1",
        "convert": "EUR"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        price = data["data"][0]["quote"]["EUR"]["price"]
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinMarketCap: {e}")
    except KeyError:
        print("Failed to parse the price data.")
    return None

# Bitcoin Value Calculator

## Overview
**BTC EUR converter ** is a Python script that convert a given amount of Bitcoin (BTC) in EUR by fetching historical prices using the CoinMarketCap API.

## Features
- Retrieve real-time Bitcoin prices in EUR.
- Calculate the total value for a specified amount of BTC.
- Simple and easy-to-use command-line interface.

## Requirements
- Python 3.7 or higher
- An API key from [CoinMarketCap](https://coinmarketcap.com/api/)

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/antoine-le-calloch/Btc-eur-converter.git
   cd Btc-eur-converter

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt

4. Create a .env file with CoinMarketCap API key: 
   ```bash
   COINMARKETCAP_API_KEY=your_api_key_here

5. Run the script:
   ```bash
   python main.py

import requests


#token: 1dd1ffb4a145721f140dfceea77036e3da8efb3
def fetch_stock_price():

#URLs for the APIs
    API_URL = "https://api.tiingo.com/tiingo/daily/xom/prices?&token=e1dd1ffb4a145721f140dfceea77036e3da8efb3"
    API_URL2 = "https://api.tiingo.com/tiingo/daily/cvx/prices?&token=e1dd1ffb4a145721f140dfceea77036e3da8efb3"

#Gets Exxon data
    response = requests.get(API_URL)
    xom_data = response.json()
    for a in xom_data:
        opening_price_exxon = a["open"]
        print(f"The opening price for Exxon is: {opening_price_exxon}")

    if response.status_code != 200:
        print("Failed to reach the data")
    
#Gets Chevron data
    response2 = requests.get(API_URL2)
    cvx_data = response2.json()
    for b in cvx_data:
        opening_price_chevron = b["open"]
        print(f"The opening price for Chevron is: {opening_price_chevron}")

    if response2.status_code != 200:
        print("Failed to reach the data")

fetch_stock_price()
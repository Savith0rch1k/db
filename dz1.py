import requests
from bs4 import BeautifulSoup



def get_exchange_rate():
    url = "https://bank.gov.ua/ua/markets/exchangerates"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="exchange-rates")
    rows = table.find_all("tr")

    for row in rows:
        cells = row.find_all("td")
        if cells and "USD" in cells[0].text:
            return float(cells[2].text.replace(',', '.'))

    return None


class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def convert_to_usd(self, amount):
        return round(amount / self.rate, 2)


if __name__ == "__main__":
    rate = get_exchange_rate()
    if rate:
        converter = CurrencyConverter(rate)
        amount = float(input("Введіть кількість валюти вашої країни: "))
        print(f"Сума у доларах США: {converter.convert_to_usd(amount)}")
    else:
        print("Не вдалося отримати курс валют.")
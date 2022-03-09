from datetime import datetime

import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond:
        cur = respond.text.split(currency_code)
        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(",", "."))
        return (value)
    else:
        return None


print((currency_rates("usd")))
print((currency_rates("eur")))
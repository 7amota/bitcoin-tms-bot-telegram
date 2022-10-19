from urllib import request, response
import requests
import time
#var
_apikey = "" #ur api key
_bottoken = "" #ur telegram bot token
_chatid = "" #ur chat id from telegram
_limit = 59000 #limit u wanna when bit be < limit the bot send 
_time = 5*60 #time u wanna loop 
#methods
def getprice():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
  'start':'1',
  'limit':'2',
  'convert':'USD'
    }
    headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': _apikey ,
    }
    response = requests.get(url , headers=headers , params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price
print(getprice())
def on_update(chat_id , msg):
    url = f"https://api.telegram.org/bot{_bottoken}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
def main():
  while True:
    price = getprice()
    if price < _limit:
      on_update(_chatid , f"the bitcoin {price} ")
      time.sleep(_time)
main()

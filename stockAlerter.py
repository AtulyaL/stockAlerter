import requests
import datetime
from twilio.rest import Client
account_sid = ""#Twilio account sid
auth_token  = ""#Twilio authtoken
polygon_API_key="" #Polygon API Key
client = Client(account_sid, auth_token)
stocks_tickers=['AAPL','GOOGL','MSFT','TSLA','AMZN']
url="https://api.polygon.io"
multiplier='1'
timespan='week'
earlier=(datetime.datetime.today()-datetime.timedelta(days=7)).strftime('%Y-%m-%d')
later=datetime.datetime.today().strftime('%Y-%m-%d')
head={
  'Authorization': 'Bearer '
}
head['Authorization']+=polygon_API_key
msg=""
for stock_ticker in stocks_tickers:
  api_call=f'/v2/aggs/ticker/{stock_ticker}/range/{multiplier}/{timespan}/{earlier}/{later}'
  data=requests.get(url+api_call,headers=head).json()
  name=data["ticker"]
  highest_price=data["results"][0]["h"]
  open_price=data["results"][0]["o"]
  if((highest_price-open_price)/highest_price<=.9):
    msg+=name + " has dipped 10 {0} from its highest price! \n".format('%')
if(len(msg)>0):
  message = client.messages.create(
  body=msg,
  from_="",#Twilio number
  to="" #Destination number
  )
from neo_api_client import NeoAPI
import json
def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

clien = NeoAPI(consumer_key="DOXh1uDSMqV4xz7qN7XBflvg6Jga",consumer_secret="7r_34SvKdpkpjfPUIZkhXin1c_sa",environment="prod")

try:
    # Login using password
    clien.login(mobilenumber="8861629545", password="Kotak@ravi1")

	
except Exception as e:
    print("Exception when calling SessionApi->session_2fa: %s\n" % e)

a=input('o:')
a=clien.session_2fa(OTP=a)
print(a)
c=clien.search_scrip(exchange_segment = "nse_cm", symbol = "YESBANK",  expiry = "", option_type = "", strike_price = "")
print(c)
b=clien.place_order(exchange_segment="nse_cm", product="NRML", price="", order_type="MKT", quantity="1", validity="DAY", trading_symbol="YESBANK-EQ",
                       transaction_type="B", amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                       trigger_price="0", tag=None)
print(b)
b=clien.place_order(exchange_segment="nse_cm", product="NRML", price="", order_type="MKT", quantity="1", validity="DAY", trading_symbol="YESBANK-EQ",
                       transaction_type="B", amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                       trigger_price="0", tag=None)
print(b)


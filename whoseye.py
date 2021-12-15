import requests
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier, timezone
import json
print("\033[31;1m WHOSEYE \u001b[0m".center(100),)

def ip_detail():
    print("\u001b[33;1mEnter the ip address \u001b[0m")
    ip=input("")
    response=requests.get("https://ipinfo.io/"+ip+"/json?token=da1626184224b0")
    #print(response.text)
    x=response.text
    y=json.loads(x)
    print(y["ip"])
    print(y["city"])
    print(y["region"])
    print(y["country"])
    print(y["loc"])
    print(y["org"])
    print(y["timezone"])
    
def phone_detail():
    my_number=phonenumbers.parse(input("\u001b[33;1m Enter the number with country code: \
        \n\u001b[0m"))
    print(geocoder.country_name_for_number(my_number,"en"))
    print(carrier.name_for_number(my_number,"en"))
    print(timezone.time_zones_for_number(my_number))
    

    
print("\u001b[33;1mChoose the options \u001b[0m\
      \n\u001b[32;1m[1]IP DETAILS \u001b[0m\
      \n\u001b[32;1m[2]PHONE NUMBER DETAILS \u001b[0m")

op=input("\u001b[32;1m ENTER THE OPTION: \u001b[0m")

if op=="1":
    ip_detail()
elif op=="2":
    phone_detail()
else:
    print("INVALID OPTION")

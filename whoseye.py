import requests

print("\033[31;1m WHOSEYE \u001b[0m".center(100),)

def geo_ip():
    print("\u001b[33;1mEnter the ip address \u001b[0m")
    ip=input("")
    response=requests.get("https://api.hackertarget.com/geoip/?q="+ip)
    print(response.text)

def tcpsc():
    print("\u001b[33;1mEnter the ip address \u001b[0m")
    ip=input("")
    response=requests.get("https://api.hackertarget.com/nmap/?q="+ip)
    print(response.text)

print("\u001b[33;1mChoose the options \u001b[0m\
      \n\u001b[32;1m[1]GEOIP \u001b[0m\
      \n\u001b[32;1m[2]TCPSCAN \u001b[0m")

op=input("\u001b[32;1m ENTER THE OPTION: \u001b[0m")

if op=="1":
    geo_ip()
elif op=="2":
    tcpsc()      
else:
    print("INVALID OPTION")


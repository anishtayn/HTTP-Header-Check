import requests
import os
from colorama import Fore
os.system("cls")
print("")
first = input(Fore.GREEN + "[+] " + Fore.BLUE + "Give Me A Site : ")
check = requests.get(first)
header_items_list=['X-Frame-Options', 'Host', 'X-XSS-Protection', 'Cache-Control', 'Pragma', 'Content-Type', 'Content-Encoding', 'Accept-Encoding', 'X-UA-Compatible', 'IE', 'Date', 'Set-Cooki', 'Dnn_IsMobile', 'HttpOnly', 'Referer', 'Expires', 'User-Agent', 'Content-Length', 'X-Content-Type-Options', 'Content-Type', 'Connection', 'Authorization', 'Accept', 'A-IM', 'Accept-Charset', 'Accept-Datetime', 'Accept-Language', 'Expect', 'Origin', 'Forwarded', 'From', 'If-Match', 'If-Modified-Since', 'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 'Proxy-Authorization', 'Range', 'TE', 'Upgrade', 'Via', 'Warning','Non-Standard-Headers' , 'Dnt', 'X-Requested-With', 'X-CSRF-Token' ]
header_dict={}
for item in header_items_list:
	if item in check.headers.keys():
		header_dict.update({item:'True'})
	else:
		header_dict.update({item:'False'})
print(Fore.YELLOW + "Header Check\n")
print(header_dict)
input()

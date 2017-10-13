#!/usr/bin/env python3
import requests
import argparse
from lxml import html


parser = argparse.ArgumentParser(description = 'Command line utility for signing into 24 Online Client')

# fill out registration no, password, ip address and MAC below:
login_data = {
            'username':'<your registration no.>@lpu.com',
            'password':'<your password>',
            'mode': '191',
            'isAccessDenied': 'false',
            'url': 'null',
            'message': '',
            'checkClose': '0',
            'sessionTimeout': '0',
            'guestmsgreq': 'false',
            'logintype': '2',
            'ipaddress': '<your ip address on the local network>',
            'orgSessionTimeout': '0',
            'chrome': '-1',
            'alerttime': 'null',
            'timeout': '0',
            'popupalert': '0',
            'dtold': '0',
            'mac': '<your mac; example: 01:1a:0e:61:11:1a>',
            'servername': '172.20.2.2'
        }

login_url = 'http://10.10.0.1/24online/servlet/E24onlineHTTPClient'
ref_url_login='http://10.10.0.1/24online/webpages/clientlogin.jsp?loginstatus=null&logoutstatus=null&message=null&liverequesttime=null&livemessage=null&url=null&isAccessDenied=null&fromlogout=true&sessionTimeout=null&ipaddress=null&username=null&formsubmiturlIP=null&alerttime=null&deviceType=COMPUTER&ajaxusername=null&autologin=false'



s = requests.Session()
p = s.post(login_url,data=login_data, headers=dict(referer=ref_url_login))
if 'You+have+successfully' in p.text:
      print('Successful Login!')
else: print('Login attempt failed!')
print(p.status_code)

# def check_connection():
#     try:
#         r = requests.get('http://www.google.com')
#         tree = html.fromstring(r.content)
#         title = tree.xpath('//title/text()')[0]
#         if not (title=='Google'):
#             return False
#     except (requests.exceptions.ConnectionError, IndexError):
#         return False
#     else:
#         return True








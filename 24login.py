#!/usr/bin/env python3
import requests

# fill out registration number and password:
login_data = {
            'username':'REGISTRATION_NUMBER@lpu.com',
            'password':'PASSWORD',
            'mode': '191',
            'isAccessDenied': 'false',
            'url': 'null',
            'message': '',
            'checkClose': '0',
            'sessionTimeout': '0',
            'guestmsgreq': 'false',
            'logintype': '2',
            'orgSessionTimeout': '0',
            'chrome': '-1',
            'alerttime': 'null',
            'timeout': '0',
            'dtold': '0',
        }

login_url = 'http://10.10.0.1/24online/servlet/E24onlineHTTPClient'
ref_url_login='http://10.10.0.1/24online/webpages/clientlogin.jsp?loginstatus=null&logoutstatus=null&message=null&liverequesttime=null&livemessage=null&url=null&isAccessDenied=null&fromlogout=true&sessionTimeout=null&ipaddress=null&username=null&formsubmiturlIP=null&alerttime=null&deviceType=COMPUTER&ajaxusername=null&autologin=false'

try:
      s = requests.Session()
      p = s.post(login_url,data=login_data, headers=dict(referer=ref_url_login))
      if 'You+have+successfully' in p.text:
            print('Login Successful!')
      else: print('Login attempt failed!')
except KeyboardInterrupt:
      print('Terminated!')
except ConnectionError:
      print('Failed to establish connection!')


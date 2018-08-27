#!/usr/bin/env python3
try:
      import requests

      # fill out registration number:
      logout_data = {
                  'username':'REGISTRATION_NUMBER@lpu.com',
                  'alerttime':'null',
                  'checkClose':'1',
                  'chrome':'1',
                  'guestmsgreq':'false',
                  'ipaddress':'',
                  'isAccessDenied':'null',
                  'logintype':'2',
                  'logout':'Logout',
                  'message': '',
                  'mode':'193',
                  'orgSessionTimeout':'0',
                  'popupalert':'1',
                  'saveinfo': '',
                  'sessionTimeout':'-1',
                  'timeout':'0',
                  'url':'null',
              }


      logout_url = 'http://10.10.0.1/24online/servlet/E24onlineHTTPClient'
      ref_url_logout='https://internet.lpu.in/24online/webpages/clientlogin.jsp?loginstatus=null&logoutstatus=null&message=null&liverequesttime=null&livemessage=null&url=null&isAccessDenied=null&fromlogout=null&sessionTimeout=null&ipaddress=null&username=null&formsubmiturlIP=null&alerttime=null&deviceType=COMPUTER&ajaxusername=null&autologin=false'

      s = requests.Session()
      p = s.post(logout_url,data=logout_data, headers=dict(referer=ref_url_logout))
      if 'You+have+successfully+logged+off' in p.text:
            print('Logout Successful!')
      else: print('Logout attempt failed!')
except KeyboardInterrupt:
      print(' Terminated!')
except requests.exceptions.ConnectionError:
      print('Failed to establish connection!')







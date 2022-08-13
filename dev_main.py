# | py -3 -m json.tool
import requests
import json
pinIn=17
pinOut=4
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinIn, GPIO.OUT)

while True:
    try:
        rfidMember = input("RFID = ")
        dataReq = {"rfid": rfidMember}
        response = requests.post("http://dev-web.urbanathletes.co.id/api/turnstile", data=dataReq)
        # print(response.json())
        # print(json.dumps(response.json()))

        memberData = response.json()

        #print(memberData['member']['email'])
        if rfidMember == '^C' or rfidMember == 'exit':
            break
        elif memberData['open'] == OUT:
            GPIO.output(pinOut, False)
            print('on')
            time.sleep(1)
            GPIO.output(pinOut, True)
            print('off')
            time.sleep(0.3)
            print('RFID Terdaftar')
            continue
        elif memberData['open'] == IN:
            GPIO.output(pinIn, False)
            print('on')
            time.sleep(1)
            GPIO.output(pinIn, True)
            print('off')
            time.sleep(0.3)
            print('RFID Terdaftar')
            continue
        else:
            print('RFID Tidak terdaftar')
            continue
    except:
        print("error")
#KeyboardInterrupt(False)
GPIO.cleanup()

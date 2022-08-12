# | py -3 -m json.tool
import requests
import json
pin=4
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while True:
    try:
        rfidMember = input("RFID = ")
        dataReq = {"rfid_card_code": rfidMember}
        response = requests.post("https://api.urbanathletes.co.id/fitness/v1/scanning/gym_attendance", data=dataReq)
        # print(response.json())
        # print(json.dumps(response.json()))

        memberData = response.json()

        #print(memberData['member']['email'])
        if rfidMember == '^C' or rfidMember == 'exit':
            break
        elif memberData['member']:
            GPIO.output(pin, False)
            print('on')
            time.sleep(1)
            GPIO.output(pin, True)
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













club=1  ##> Ganti Code club sesuai club
import requests
import json
pinIn=17
pinOut=4
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinIn, GPIO.OUT)
GPIO.setup(pinOut, GPIO.OUT)

while True:
    try:
        rfidMember = input("RFID = ")
        dataReq = {"rfid": rfidMember, "branch_id": club}
        # response = requests.post("http://dev-web.urbanathletes.co.id/api/turnstile", data=dataReq)
        response = requests.post("https://fwapp.fitnessworks.co.id/api/member/check-in", data=dataReq)
        # print(response.json())
        # print(json.dumps(response.json()))

        memberData = response.json()
#         memberJson = json.load(memberData)

#         print(memberJson["open"])
        if rfidMember == 'EXIT' or rfidMember == 'exit':
            break
        if rfidMember == 'StaffUrban1234':
            GPIO.output(pinIn, False)
            GPIO.output(pinOut, False)
            print('on')
            time.sleep(1)
            GPIO.output(pinIn, True)
            GPIO.output(pinOut, True)
            print('off')
            time.sleep(0.3)
            print('Staff')
            continue
        elif memberData["open"] == "OUT":
            GPIO.output(pinOut, False)
            print('on')
            time.sleep(1)
            GPIO.output(pinOut, True)
            print('off')
            time.sleep(0.3)
            print(memberData)
            continue
        elif memberData["open"] == "IN":
            GPIO.output(pinIn, False)
            print('on')
            time.sleep(1)
            GPIO.output(pinIn, True)
            print('off')
            time.sleep(0.3)
            print(memberData)
            continue
        else:
            print('RFID Tidak terdaftar')
            continue
    except:
        print("error turnstile")
#        print(error)
#        break
#KeyboardInterrupt(False)
GPIO.cleanup()

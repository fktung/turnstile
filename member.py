# | py -3 -m json.tool
import requests
import json

while True:
  rfidMember = input("RFID = ")
  dataReq = {"rfid_card_code": rfidMember}
  response = requests.post("https://api.urbanathletes.co.id/fitness/v1/scanning/gym_attendance", data=dataReq)
  # print(response.json())
  # print(json.dumps(response.json()))

  memberData = response.json()

  # print(memberData['member']['email'])
  if memberData:
    print('RFID Terdaftar')
  else:
    print('RFID Tidak terdaftar')

import cv2
import urllib.request
from pyzbar import pyzbar
import numpy as np
import pyrebase
url=''
im=None
img = cv2.imread("istockphoto-182821556-612x612 copy.jpg")

config = {
  "apiKey": "AIzaSyDZ5BRdnNZGMYexz4e5I5-9eV4pwpvPg1E",
  "authDomain": "fixit-9b84b.firebaseapp.com",
  "databaseURL": "https://fixit-9b84b-default-rtdb.firebaseio.com",
  "projectId": "fixit-9b84b",
  "storageBucket": "fixit-9b84b.appspot.com",
  "messagingSenderId": "794724870742",
  "appId": "1:794724870742:web:529954acde460da716e9f7",
  "databaseURL": "https://fixit-9b84b-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(config)
database = firebase.database()

def vacant_slots(image):
    vacnt = []
    for i in pyzbar.decode(image):
        points = np.array([i.polygon], np.int32)
        data = i.data.decode('utf-8')
        vacnt.append(data)
    return vacnt

def run():
    tmp = None
    while True:
        
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
        cv2.imshow('live transmission',im)
        slots = vacant_slots(im)
        if tmp != slots:
            vacant = {}
            for i in range(0,len(slots)):
                vacant[i] = slots[i]
            database.child("Booking_data").set(vacant)
            print(slots)
        tmp = slots
        
        
#run()
print(vacant_slots(img))
cv2.waitKey(0)
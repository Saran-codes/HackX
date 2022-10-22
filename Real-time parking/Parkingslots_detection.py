import cv2
import urllib.request
from pyzbar import pyzbar
import numpy as np

url=''
im=None
img = cv2.imread("istockphoto-182821556-612x612 copy.jpg")
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
            print(slots)
        tmp = slots
        
#run()
print(vacant_slots(img))
cv2.waitKey(0)
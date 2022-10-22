# HackX
Team Name: Hackers

Problem Statement: Real-Time Parking View
 Approach in steps:
 1.All the parking slots contain a QR code which contains the address(or index) of the parking slot.
 2.An ESP32 with AI Thinker cam module overviews an area where the parking slots are there so as that that qr codes are comfortably visible to camera
 3.This ESP32 creates a webserver where the each frame is uploaded.
 4.Using ullib we can access the web server can get frames into the system.
 5.Using Opencv and pyzbar library we can detect qr codes present in the image and decode them to get the address of parking slots.
 6.If the parking slot is already filled we cannot detect the qr code and hence all the qr codes we detect are of the vacant slots.
 7.Now all the empty parking slots can be communicated to the user by using an appilication in which data of vacant parking slots and their location(address) are updated in real-time.

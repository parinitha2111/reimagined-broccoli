import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin, GPIO.IN)
counter=1
time.sleep(2)
while counter<=2:
    if GPIO.input(pirPin):
        print ("Motion Detected")
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/G1/"+str(counter)+".jpg")
        print("image is captured")
        time.sleep(1)
        counter=counter+1
print("Testing")
exit()

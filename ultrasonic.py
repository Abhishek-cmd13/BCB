import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
trigPins=[25,2,3,24]
echoPins=[14,15,23,18]
for i in range(len(trigPins)):
    TRIG=trigPins[i]
    ECHO=echoPins[i]

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==False:
      start=time.time()

    while GPIO.input(ECHO)==True:
      end=time.time()

    sig_time=end-start

    distance=sig_time/0.000058
    print("Distance from sensor{0}:{1}".format(i,distance))
    time.sleep(2)
GPIO.cleanup()


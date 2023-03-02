import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
TRIG1 = 15
ECHO1 = 14
#TRIG2 = 24
#ECHO2 = 23
TRIG3 = 6
ECHO3 = 5
TRIG4 = 27
ECHO4 = 22

# Set up GPIO pins for each sensor
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
#GPIO.setup(TRIG2, GPIO.OUT)
#GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(TRIG3, GPIO.OUT)
GPIO.setup(ECHO3, GPIO.IN)
GPIO.setup(TRIG4, GPIO.OUT)
GPIO.setup(ECHO4, GPIO.IN)

# Set up variables for each sensor
distance1 = 0
#distance2 = 0
distance3 = 0
distance4 = 0

# Function to measure the distance from each sensor
def measure_distance(TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance
dist1=[]
dist3=[]
dist4=[]
# Main loop
with open('readings.txt', 'w') as f:
    for i in range(10000000):
       distance1 = measure_distance(TRIG1, ECHO1)
       #time.sleep(1)
       print(distance1)
       dist1.append(distance1)
    #distance2 = measure_distance(TRIG2, ECHO2)
    #time.sleep(1)
       distance3 = measure_distance(TRIG3, ECHO3)
       #time.sleep(1)
       print(distance3)
       dist3.append(distance3)
       distance4 = measure_distance(TRIG4, ECHO4)
       #time.sleep(1)
       print(distance4)
       dist4.append(distance4)
       #time.sleep(1)
    #with open ('readings.txt','a') as f:
    f.write(str(dist1))
    f.write(str(dist3))
    f.write(str(dist4))


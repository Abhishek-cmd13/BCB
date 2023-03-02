

#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
TRIG = 14
ECHO = 15

# Set up GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Set trigger to False (Low)
GPIO.output(TRIG, False)

# Allow sensor to settle
time.sleep(2)

# Send 10us pulse to trigger
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

# Start the timer and set the start time
while GPIO.input(ECHO) == 0:
    start = time.time()

# Set the end time and calculate the duration
while GPIO.input(ECHO) == 1:
    end = time.time()

duration = end - start

# Calculate the distance
distance = duration * 17150
distance = round(distance, 2)

# Print the distance
print("Distance:", distance, "cm")

# Reset GPIO settings
GPIO.cleanup()

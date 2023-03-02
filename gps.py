import serial              
import pynmea2
import time 
import string  

while True:
            port =  "/dev/ttyAMA0"
            ser = serial.Serial(port , baudrate = 9600 , timeout = 0.5)
            dataout =pynmea2.NMEAStreamReader() 
            newdata=ser.readline() 
#            print(newdata,"\n")
            if newdata[0:6] == b'$GNRMC':
                
         #   newdata = newdata.decode("utf-8")
#            newmsg=pynmea2.parse(newdata)  
            #lat=newmsg.latitude 
           # lng=newmsg.longitude 
           # gps = "Latitude=" + str(lat) + "and Longitude=" +str(lng) 
              # print("Lat = ",newdata[19:28],"\n")
              # print("Long = ",newdata[34:46],"\n")
               lat = float(newdata[19:28])
               lat = lat/100
               long = float(newdata[32:43])
               long = long/100
               print("Lat = ",lat ,"\n")                                                  
               print("Long = ",long ,"\n")

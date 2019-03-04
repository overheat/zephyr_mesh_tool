#!/usr/bin/env python
import cayenne.client
import time
import logging

import serial
from time import sleep  


# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "1659fa40-393b-11e9-b85b-afa01d2216d6"
MQTT_PASSWORD  = "31b38212a4354b59a4bc5c2a0ed9d86174c5b6c8"
MQTT_CLIENT_ID = "b165a1e0-399c-11e9-a98b-69b394a1794b"


client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)

i=0
timestamp = 0

ser = serial.Serial('COM14', # Device name varies
                    baudrate=115200,
                    bytesize=8,
                    parity='N',
                    stopbits=1,
                    timeout=1)
                    
print (ser.portstr)       # check which port was really used  
        
        
while True:
    client.loop()
    
    if (time.time() > timestamp + 10):
        client.celsiusWrite(1, i)
        client.luxWrite(2, i*10)
        client.hectoPascalWrite(3, i+800)
        timestamp = time.time()
        i = i+1
    
    line = ser.readline()# read a '\n' terminated line
    if(line!=b''):
        print (str(line, encoding = "utf-8"))
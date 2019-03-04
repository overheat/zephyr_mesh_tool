#!/usr/bin/env python
import cayenne.client
import time
import logging
import sys

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
                    
#print (ser.portstr)       # check which port was really used  
print('Please input serial port number:')
serPortNum = input()
serPort = 'COM' + serPortNum

try:
    ser = serial.Serial(serPort, # Device name varies
                        baudrate=115200,
                        bytesize=8,
                        parity='N',
                        stopbits=1,
                        timeout=1)
except serial.serialutil.SerialException:
    print('Wrong serial port number, try again.')
    sys.exit()

        
while True:
    client.loop()
    
    line = ser.readline()# read a '\n' terminated line
    if(line!=b''):
        line_str = line.decode('utf-8')
        #print (line_str,end='')
        if line_str.startswith('src 0x'):
            #print (line_str[6:10])
            i = int(line_str[8:10])
            #print (i)

        
    if (time.time() > timestamp + 10):
        client.celsiusWrite(1, i)
        client.celsiusWrite(2, i)
        client.celsiusWrite(3, i)
        timestamp = time.time()
        i = i+1
    

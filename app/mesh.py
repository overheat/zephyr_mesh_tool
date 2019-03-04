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

timestamp = 0
mesh_dict = {}

                    
# point which port was really used  
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
        if line.startswith(b'src '):
            mesh_node_id = int(str(line[4:10], encoding="utf-8"), 16)
            mesh_dict[mesh_node_id] = time.time()
            #print(mesh_node_id)


        
    if (time.time() > timestamp + 5):
        for mesh_node_id in mesh_dict.keys():
            #print(mesh_node_id)
            if(time.time() > mesh_dict[mesh_node_id] + 10):
                client.celsiusWrite(mesh_node_id, 0)
            else:
                client.celsiusWrite(mesh_node_id, 1)

        timestamp = time.time()
    

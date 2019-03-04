Zephyr mesh demo python tool
****************************
The Zephyr mesh demo python tool provides functions to easily grab data from `zephyr mesh demo <https://github.com/zephyrproject-rtos/zephyr/tree/master/samples/bluetooth/mesh_demo>`_ nodes and connect to the `Cayenne IoT project builder <https://mydevices.com>`_. With it you can send zephyr mesh demo data to Cayenne.

.. image:: img.png

Requirements
============
* `Python 2.7.9+ or 3.4+ <https://www.python.org/downloads/>`_.
* `This library <https://github.com/myDevicesIoT/Cayenne-MQTT-Python/archive/master.zip>`_.
* `Eclipse Paho MQTT Python client library <https://github.com/eclipse/paho.mqtt.python>`_. This is installed as part of the Cayenne library installation.
* `Raspberry Pi <https://www.raspberrypi.org/>`_. or PC
* Running zephyr project mesh demo.



Getting Started
===============
Installation
------------
This library can be installed using pip:
::

On ubuntu:
  pip install cayenne-mqtt
  pip3 install pyserial

It can also be installed from the repository:
::

On ubuntu:
  git clone https://github.com/myDevicesIoT/Cayenne-MQTT-Python
  cd Cayenne-MQTT-Python
  python3 setup.py install
  
Cayenne Setup
-------------
1. Create your Cayenne account at https://mydevices.com.
2. Add a new device using the Bring Your Own Thing API selection.

Demo
-------------
Connect any mesh node's serial port to your PC or Raspberry Pi, then

On ubuntu:
  python3 app/mesh.py

Documentation
-------------
For more detailed info about the Cayenne client API you can use **pydoc**.
::

  pydoc cayenne.client
  

Additional Cayenne MQTT Libraries
=================================
Additional libraries are available for connecting to Cayenne with other languages. These can be found at https://github.com/myDevicesIoT.

Zephyr mesh demo python tool
****************************
The Zephyr mesh demo python tool provides functions to easily connect to the `Cayenne IoT project builder <https://mydevices.com>`_. With it you can send zephyr mesh demo data to Cayenne.

Requirements
============
* `Python 2.7.9+ or 3.4+ <https://www.python.org/downloads/>`_.
* `This library <https://github.com/myDevicesIoT/Cayenne-MQTT-Python/archive/master.zip>`_.
* `Eclipse Paho MQTT Python client library <https://github.com/eclipse/paho.mqtt.python>`_. This is installed as part of the Cayenne library installation.

Getting Started
===============
Installation
------------
This library can be installed using pip:
::

  pip install cayenne-mqtt

It can also be installed from the repository:
::

  git clone https://github.com/myDevicesIoT/Cayenne-MQTT-Python
  cd Cayenne-MQTT-Python
  python setup.py install
  
Cayenne Setup
-------------
1. Create your Cayenne account at https://mydevices.com.
2. Add a new device using the Bring Your Own Thing API selection.

Demo
-------------
On ubuntu:
  cd app
  python3 mesh.py

Documentation
-------------
For more detailed info about the Cayenne client API you can use **pydoc**.
::

  pydoc cayenne.client
  

Additional Cayenne MQTT Libraries
=================================
Additional libraries are available for connecting to Cayenne with other languages. These can be found at https://github.com/myDevicesIoT.

# ABB <---> Teltonika

## Requirements

- Python 3

## Installing Project
`` pip install venv ``

``source venv/bin/activate``

``pip install -r requirements.txt``

## Teltonika Configuration

Make sure that the Teltonika device is configured correctly for each example. An example configuration is included for each example.

The Teltonika device can be configured using the UI or coping the appropriate config file to the ``/etc/config`` directory on the device.


### Gateway Configuration
Config File: `teltonika_config/modbusgateway.example`

### Client Configuration
Config File: `modbus_client.decoded_example`

Config File: `modbus_client.hex_example`


## MQTT Modbus Gateway Example

The modbus gateway example uses the transparent gateway functionality of the Teltonika modem and relays modbus requests and responses back and forth from the modem.

### MQTT broker and topic configurations
The following variables are used to configure the MQTT client
```
mqtt_host = "broker.hivemq.com"
mqtt_username = ""
mqtt_password = ""
mqtt_modbus_request_topic = "m4m-example/request"
mqtt_modbus_response_topic = "m4m-example/response"
```

### Read configuration
Cookie: starts at 1 and increments. 

device_id: used to configure the device on the Teltonika modem. I.e. if you have 2 different types of devices on the RS485 line, you would use this to switch between the device types.

slave_address: Used to talk to a specific slave. This is the modbus address of the device

timeout: How long the Teltonika device should wait for a reply before timing out

read_frequency: How often the register should be read from the device
```
cookie = 1
device_id = 0x01
slave_address = 0x01
timeout = 1 #seconds
read_frequency = 10
```
### Running the service

Running the service should result in a shadow being updated for the device 

``python3 gateway_client.py``

When messages are received by the service they will be decoded and updated in the shadow of the device with some meta data.

```
{
   "ACTIVE_ENERGY_IMPORT":{
      "last_updated":1702825328950,
      "value":2329.61,
      "units":"kWh"
   },
   "ACTIVE_ENERGY_EXPORT":{
      "last_updated":1702825329132,
      "value":0.0,
      "units":"kWh"
   },
   "ACTIVE_ENERGY_NET":{
      "last_updated":1702825329475,
      "value":2329.61,
      "units":"kWh"
   },
   "REACTIVE_ENERGY_IMPORT":{
      "last_updated":1702825329839,
      "value":192.99,
      "units":"kVARh"
   },
   "REACTIVE_ENERGY_EXPORT":{
      "last_updated":1702825330220,
      "value":11.4,
      "units":"kVARh"
   },
   "REACTIVE_ENERGY_NET":{
      "last_updated":1702825330522,
      "value":181.59,
      "units":"kVARh"
   },
   "APPARENT_ENERGY_IMPORT":{
      "last_updated":1702825330523,
      "value":2449.45,
      "units":"kVA"
   },
   "APPARENT_ENERGY_EXPORT":{
      "last_updated":1702825331210,
      "value":0.0,
      "units":"kVA"
   },
   "APPARENT_ENERGY_NET":{
      "last_updated":1702825331210,
      "value":2449.45,
      "units":"kVA"
   },
   "PHASE_VOLTAGE_L1":{
      "last_updated":1702825331374,
      "value":0.0,
      "units":"V"
   },
   "PHASE_VOLTAGE_L2":{
      "last_updated":1702825331569,
      "value":0.0,
      "units":"V"
   },
   "PHASE_VOLTAGE_L3":{
      "last_updated":1702825331908,
      "value":0.0,
      "units":"V"
   },
   "LINE_VOLTAGE_L1_L2":{
      "last_updated":1702825332260,
      "value":0.0,
      "units":"V"
   },
   "LINE_VOLTAGE_L3_L2":{
      "last_updated":1702825332422,
      "value":0.0,
      "units":"V"
   },
   "LINE_VOLTAGE_L1_L3":{
      "last_updated":1702825332621,
      "value":0.0,
      "units":"V"
   },
   "CURRENT_L1":{
      "last_updated":1702825332812,
      "value":0.0,
      "units":"A"
   },
   "CURRENT_L2":{
      "last_updated":1702825333308,
      "value":0.0,
      "units":"A"
   },
   "CURRENT_L3":{
      "last_updated":1702825333669,
      "value":0.0,
      "units":"A"
   },
   "CURRENT_N":{
      "last_updated":1702825333880,
      "value":0.0,
      "units":"A"
   },
   "ACTIVE_POWER_TOTAL":{
      "last_updated":1702825334538,
      "value":0.0,
      "units":"W"
   },
   "ACTIVE_POWER_L1":{
      "last_updated":1702825334539,
      "value":0.0,
      "units":"W"
   },
   "ACTIVE_POWER_L2":{
      "last_updated":1702825334539,
      "value":0.0,
      "units":"W"
   },
   "ACTIVE_POWER_L3":{
      "last_updated":1702825334539,
      "value":0.0,
      "units":"W"
   },
   "REACTIVE_POWER_TOTAL":{
      "last_updated":1702825334889,
      "value":0.0,
      "units":"var"
   },
   "REACTIVE_POWER_L1":{
      "last_updated":1702825335240,
      "value":0.0,
      "units":"var"
   },
   "REACTIVE_POWER_L2":{
      "last_updated":1702825335410,
      "value":0.0,
      "units":"var"
   },
   "REACTIVE_POWER_L3":{
      "last_updated":1702825335762,
      "value":0.0,
      "units":"var"
   },
   "APPARENT_POWER_TOTAL":{
      "last_updated":1702825335982,
      "value":0.0,
      "units":"VA"
   },
   "APPARENT_POWER_L1":{
      "last_updated":1702825336289,
      "value":0.0,
      "units":"VA"
   },
   "APPARENT_POWER_L2":{
      "last_updated":1702825336454,
      "value":0.0,
      "units":"var"
   },
   "APPARENT_POWER_L3":{
      "last_updated":1702825336644,
      "value":0.0,
      "units":"VA"
   },
   "FREQUENCY":{
      "last_updated":1702825337504,
      "value":50.18,
      "units":"Hz"
   },
   "POWER_FACTOR_TOTAL":{
      "last_updated":1702825337668,
      "value":0.0,
      "units":"deg"
   }
}

```


## Data-to-Server MQTT Client Example

The Data-to-Server example subscribes to a topic and decodes messages form Hex as they are received by the python script. In this example the Modbus commands are pre-configured on the Teltonika device.

### MQTT Configuration
```
mqtt_host = "broker.hivemq.com"
mqtt_username = ""
mqtt_password = ""
mqtt_modbus_topic = "m4m-example"
```

### Running the example
``python3 modbus_client.py``



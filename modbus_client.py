# Import necessary libraries
import paho.mqtt.client as mqtt
import time
import json
from  m4m30 import M4M_30_REG_MAP, find_parameter_by_address, decode_hex_str

# MQTT broker and topic configurations
mqtt_host = "broker.hivemq.com"
mqtt_username = ""
mqtt_password = ""
mqtt_modbus_topic = "m4m-example"


# Dictionary to store device data (shadow) and cookie-tracking for requests
shadow = {}
request_stack = {}


# Function to get the current time in milliseconds
def current_milli_time():
    return round(time.time() * 1000)

def decode_unsigned(arr):
    bytes = bytearray()
    for reg in arr:
        bytes = bytes + reg.to_bytes(2, 'big')
    val = int.from_bytes(bytes, byteorder='big')
    return val

# Functions to decode unsigned and signed values from an array of registers
def decode_signed(arr):
    bytes = bytearray()
    for reg in arr:
        bytes = bytes + reg.to_bytes(2, 'big')
    val = int.from_bytes(bytes, byteorder='big')
    return val


# Dictionary to map data types to corresponding decoding functions
decode = {
    'unsigned': decode_unsigned,
    'signed': decode_signed
}

# Function to decode the response received from the server
def decode_response(parameter, response):
    reg = M4M_30_REG_MAP[parameter]
    decoded = decode[reg['data_type']](response)
    value = round(decoded * reg['resolution'], 2)
    return value, reg['units']

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(mqtt_modbus_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    payload = json.loads(str(msg.payload, encoding='utf-8'))['Modbus']
    parameter = find_parameter_by_address(payload['addr'] - 1)
    if parameter != None:
        hex = payload['data'].strip('"')
        value, units = decode_hex_str(hex, parameter)
        shadow[parameter] = { 'last_updated': current_milli_time(),  'value': value, 'units': units}
        print("{}: {} {}".format(parameter, value, units))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_host, 1883, 60)

client.loop_forever()
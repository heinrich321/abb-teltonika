# Import necessary libraries
import paho.mqtt.client as mqtt
import time
import json
from  m4m30 import M4M_30_REG_MAP, find_parameter_by_address, hex_string_to_int

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
        value, units = hex_string_to_int(hex, parameter)
        shadow[parameter] = { 'last_updated': current_milli_time(),  'value': value, 'units': units}
        print("{}: {} {}".format(parameter, value, units))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_host, 1883, 60)

client.loop_forever()
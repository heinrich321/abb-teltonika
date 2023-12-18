# Import necessary libraries
import paho.mqtt.client as mqtt
import time
from  m4m30 import M4M_30_REG_MAP 

# MQTT broker and topic configurations
mqtt_host = "broker.hivemq.com"
mqtt_username = ""
mqtt_password = ""
mqtt_modbus_request_topic = "m4m-example/request"
mqtt_modbus_response_topic = "m4m-example/response"


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
    client.subscribe(mqtt_modbus_response_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    message = str(msg.payload, encoding='utf-8')

    message_arr = message.split(' ')
    cookie = int(message_arr[0])
    parameter = request_stack[cookie]
    if message_arr[1] == 'OK':
        number_arr = [int(numeric_string) for numeric_string in message_arr[2:]]
        value, units = decode_response(parameter, number_arr)
        # print("{}: {} {}".format(parameter, value, units))
        shadow[parameter] = { 'last_updated': current_milli_time(),  'value': value, 'units': units}
        print(shadow)
    else:
        print('Error @ reading ', parameter, message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_host, 1883, 60)

client.loop_start()

# Function to build the Modbus command for requesting data
def build_command(cookie, device_id, timeout, slave_id, parameter):
    #  1 <COOKIE> <SERIAL_DEVICE_ID> <TIMEOUT> <SLAVE_ID> <MODBUS_FUNCTION> <FIRST_REGISTER> <REGISTER_COUNT>
    reg = M4M_30_REG_MAP[parameter]
    reg_address = reg['address'] + 1
    reg_count = reg['n_registers']
    function = reg['function']
    msg = "1 {} {} {} {} {} {} {}".format(cookie, device_id, timeout, slave_id, function, reg_address, reg_count)
    return msg


# Initial configurations for Modbus request
cookie = 1
device_id = 0x01
slave_address = 0x01
timeout = 1 #seconds
read_frequency = 10

while True:
    time.sleep(read_frequency)

    param_list = list(M4M_30_REG_MAP.keys())
    for param in param_list:
        command = build_command(cookie, device_id, timeout, slave_address, param)

        # Cookie tracking used to identify what request the response is ascociated with
        request_stack[cookie] = param
        cookie = cookie + 1


        print('Reading {}'.format(param))
        print(command)
        # '1 1 1 1 1 3 23347 1'
        client.publish(mqtt_modbus_request_topic, payload=command, qos=0)
        time.sleep(0.25) #Delay for serial communication

#Some Executable Code Here
client.loop_stop()
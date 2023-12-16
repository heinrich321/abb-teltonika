import paho.mqtt.client as mqtt
import time
from  m4m30 import M4M_30_REG_MAP 

mqtt_host = "broker.hivemq.com"
mqtt_username = ""
mqtt_password = ""
mqtt_modbus_request_topic = "m4m-example/request"
mqtt_modbus_response_topic = "m4m-example/response"

request_stack = {}

def decode_uint16(arr):
    return arr[0]

def decode_uint32(arr):
    bytes = bytearray()
    for reg in arr:
        bytes = bytes + reg.to_bytes(2, 'big')
    val = int.from_bytes(bytes, byteorder='big')
    return val

decode = {
    'uint16': decode_uint16,
    'uint32': decode_uint32
}

def decode_response(parameter, response):
    reg = M4M_30_REG_MAP[parameter]
    decoded = decode[reg['data_type']](response)
    formatted = "{} {}".format((decoded * reg['resolution']), reg['units'])
    print(formatted)

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
    if message_arr[1] == 'OK':
        cookie = int(message_arr[0])
        parameter = request_stack[cookie]
        number_arr = [int(numeric_string) for numeric_string in message_arr[2:]]
        decode_response(parameter, number_arr)
    else:
        print('Error ', message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_host, 1883, 60)

client.loop_start()

def build_command(cookie, device_id, timeout, slave_id, parameter):
    #  1 <COOKIE> <SERIAL_DEVICE_ID> <TIMEOUT> <SLAVE_ID> <MODBUS_FUNCTION> <FIRST_REGISTER> <REGISTER_COUNT>
    reg = M4M_30_REG_MAP[parameter]
    reg_address = reg['address'] + 1
    reg_count = reg['n_registers']
    function = reg['function']
    msg = "1 {} {} {} {} {} {} {}".format(cookie, device_id, timeout, slave_id, function, reg_address, reg_count)
    return msg

cookie = 1
device_id = 0x01
slave_address = 0x01
timeout = 1 #seconds

while True:
    time.sleep(10)

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

#Some Executable Code Here
client.loop_stop()
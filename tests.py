from m4m30 import M4M_30_REG_MAP, decode_hex_str, find_parameter_by_address
import json

payload_str = '{"Modbus":{"timestamp":1702832463,"date":"17/12/2023 17:01:03","bdate":null,"server_id":1,"bserver_id":1,"addr":20497,"baddr":null,"full_addr":"420497","size":18,"data":"\\"0000000000000474\\"","raw_data":null,"server_name":"M4M","name":"REACTIVE_EXPORT"}}'
payload_json = json.loads(payload_str)['Modbus']
parameter = find_parameter_by_address(payload_json['addr'] - 1)
hex = payload_json['data'].strip('"')
value, units = decode_hex_str(hex, parameter)

print("{}: {} {}".format(parameter, value, units))
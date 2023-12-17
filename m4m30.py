M4M_30_REG_MAP = {
    'ACTIVE_ENERGY_IMPORT': {
        'address': 0x5000,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kWh',
        'data_type': 'unsigned'
    },
    'ACTIVE_ENERGY_EXPORT': {
        'address': 0x5004,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kWh',
        'data_type': 'unsigned'
    },
    'ACTIVE_ENERGY_NET': {
        'address': 0x5008,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kWh',
        'data_type': 'signed'
    },
    'REACTIVE_ENERGY_IMPORT': {
        'address': 0x500C,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kVARh',
        'data_type': 'unsigned'
    },
    'REACTIVE_ENERGY_EXPORT': {
        'address': 0x5010,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kVARh',
        'data_type': 'unsigned'
    },
    'REACTIVE_ENERGY_NET': {
        'address': 0x5014,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kVARh',
        'data_type': 'signed'
    },
    'APPARENT_ENERGY_IMPORT': {
        'address': 0x5018,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kVA',
        'data_type': 'unsigned'
    },
    'APPARENT_ENERGY_EXPORT': {
        'address': 0x501C,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kVA',
        'data_type': 'unsigned'
    },
    'APPARENT_ENERGY_NET': {
        'address': 0x5020,
        'quantities': 1,
        'n_registers': 4,
        'size': 4,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'kVA',
        'data_type': 'signed'
    },
    'PHASE_VOLTAGE_L1': {
        'address': 0x5B02,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.1,
        'function': 0x03,
        'units': 'V',
        'data_type': 'unsigned'
    },
    'PHASE_VOLTAGE_L2': {
        'address': 0x5B04,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.1,
        'function': 0x03,
        'units': 'V',
        'data_type': 'unsigned'
    },
    'PHASE_VOLTAGE_L3': {
        'address': 0x5B06,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.1,
        'function': 0x03,
        'units': 'V',
        'data_type': 'unsigned'
    },
    'LINE_VOLTAGE_L1_L2': {
        'address': 0x5B08,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.1,
        'function': 0x03,
        'units': 'V',
        'data_type': 'unsigned'
    },
    'LINE_VOLTAGE_L3_L2': {
        'address': 0x5B0A,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.1,
        'function': 0x03,
        'units': 'V',
        'data_type': 'unsigned'
    },
    'LINE_VOLTAGE_L1_L3': {
        'address': 0x5B0C,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.1,
        'function': 0x03,
        'units': 'V',
        'data_type': 'unsigned'
    },
    'CURRENT_L1': {
        'address': 0x5B10,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'A',
        'data_type': 'unsigned'
    },
    'CURRENT_L2': {
        'address': 0x5B12,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'A',
        'data_type': 'unsigned'
    },
    'CURRENT_L3': {
        'address': 0x5B14,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'A',
        'data_type': 'unsigned'
    },
    'CURRENT_N': {
        'address': 0x5B16,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'A',
        'data_type': 'unsigned'
    },
    'ACTIVE_POWER_TOTAL': {
        'address': 0x5B1A,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'W',
        'data_type': 'signed'
    },
    'ACTIVE_POWER_L1': {
        'address': 0x5B1C,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'W',
        'data_type': 'signed'
    },
    'ACTIVE_POWER_L2': {
        'address': 0x5B1E,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'W',
        'data_type': 'signed'
    },
    'ACTIVE_POWER_L3': {
        'address': 0x5B20,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'W',
        'data_type': 'signed'
    },
    'REACTIVE_POWER_TOTAL': {
        'address': 0x5B22,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'var',
        'data_type': 'signed'
    },
    'REACTIVE_POWER_L1': {
        'address': 0x5B24,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'var',
        'data_type': 'signed'
    },
    'REACTIVE_POWER_L2': {
        'address': 0x5B26,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'var',
        'data_type': 'signed'
    },
    'REACTIVE_POWER_L3': {
        'address': 0x5B28,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'var',
        'data_type': 'signed'
    },
    'APPARENT_POWER_TOTAL': {
        'address': 0x5B2A,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'VA',
        'data_type': 'signed'
    },
    'APPARENT_POWER_L1': {
        'address': 0x5B2C,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'VA',
        'data_type': 'signed'
    },
    'APPARENT_POWER_L2': {
        'address': 0x5B2E,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'var',
        'data_type': 'signed'
    },
    'APPARENT_POWER_L3': {
        'address': 0x5B30,
        'quantities': 1,
        'n_registers': 2,
        'size': 2,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'VA',
        'data_type': 'signed'
    },
    'FREQUENCY': {
        'address': 0x5B32,
        'quantities': 1,
        'n_registers': 1,
        'size': 1,
        'resolution': 0.01,
        'function': 0x03,
        'units': 'Hz',
        'data_type': 'unsigned'
    },
    'POWER_FACTOR_TOTAL': {
        'address': 0x5B40,
        'quantities': 1,
        'n_registers': 1,
        'size': 1,
        'resolution': 0.001,
        'function': 0x03,
        'units': 'deg',
        'data_type': 'signed'
    },
    'POWER_FACTOR_L1': {
        'address': 0x5B41,
        'quantities': 1,
        'n_registers': 1,
        'size': 1,
        'resolution': 0.001,
        'function': 0x03,
        'units': 'deg',
        'data_type': 'signed'
    },
    'POWER_FACTOR_L2': {
        'address': 0x5B42,
        'quantities': 1,
        'n_registers': 1,
        'size': 1,
        'resolution': 0.001,
        'function': 0x03,
        'units': 'deg',
        'data_type': 'signed'
    },
    'POWER_FACTOR_L3': {
        'address': 0x5B43,
        'quantities': 1,
        'n_registers': 1,
        'size': 1,
        'resolution': 0.001,
        'function': 0x03,
        'units': 'deg',
        'data_type': 'signed'
    },
}

def find_parameter_by_address(address):
    param_list = list(M4M_30_REG_MAP.keys())
    for param in param_list:
        if M4M_30_REG_MAP[param]['address'] == address:
            return param
    return None



def decode_hex_str(hex_string, parameter):
    byte_arr = bytes.fromhex(hex_string)
    non_scaled_value = int.from_bytes(byte_arr, byteorder='big')
    value = round(non_scaled_value * M4M_30_REG_MAP[parameter]['resolution'], 2)
    return value, M4M_30_REG_MAP[parameter]['units']
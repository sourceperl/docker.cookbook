# Modbus/TCP server

from pyModbusTCP.server import ModbusServer

if __name__ == '__main__':
    server = ModbusServer(host='0.0.0.0', port=5020)
    server.start()

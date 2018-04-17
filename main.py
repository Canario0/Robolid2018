# Ejemplo Uso de la librería PySerial

# 1º importamos la librería PySerial y la librería para la configuración.
import serial
import configparser

config = configparser.ConfigParser()
config.read('configuracion')

# 2º  Adrimos el puerto serial
# La idea de poner un timeout, es hacer que si se bloquea esperando datos (que no van a llegar) termine el probrama
port = serial.Serial(config['DEFAULT']['Port'], config['DEFAULT']['BaudRate'], timeout=60)

# 3º Mandamos un mensaje a arduino

port.write(b"enciendete\n")

# 4º Esperamos la contestación de arduino

ack = port.readline().decode('utf8')

# 5º Mostramos al usuario los datos recividos

print(ack)

# 6º Cerramos el puerto serial

port.close()


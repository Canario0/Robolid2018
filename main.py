# Ejemplo Uso de la librería PySerial

# 1º importamos la librería PySerial , la librería para la configuración y la base de datos.
import serial
import configparser
from db import create_medicion, create_sensor, get_mediciones, get_sensores
import re  # Libreria para expresiones regulares

exp = re.compile(r"#(\d)#\d#(\d+)#\d+#")

config = configparser.ConfigParser()
config.read('configuracion')

# 2º  Adrimos el puerto serial
# La idea de poner un timeout, es hacer que si se bloquea esperando datos (que no van a llegar) termine el probrama
port = serial.Serial(config['DEFAULT']['Port'],
                     config['DEFAULT']['BaudRate'], timeout=60)

# 3º Empezamos a leer los datos de arduino
while 1:
    try:

        input_data = port.readline().decode('utf8')
        # 4º Comprobamos si hemos leido algo y la entrada
        # sigue el patrón y sacamos los datos que necesitamos, añadiendolo a la base de datos.
        if len(input_data) == 0:
            print("Whoops, check arduino")
            break
        elif exp.match(input_data):
            dato =  exp.match(input_data)
            create_medicion(int(dato.group(1)), int(dato.group(2)))
            #print(int(dato.group(1)), int(dato.group(2)))

    except serial.SerialException:
        print("Sorry, we lost connection")
        break

# 5º Cerramos el puerto serial

port.close()

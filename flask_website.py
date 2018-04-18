from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, current_app
from flask_socketio import SocketIO, emit, join_room, leave_room
from random import random
from serial import Serial, SerialException
import re
from threading import Thread
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True
socketio = SocketIO(app, async_mode='gevent')
thread = None

@app.route('/')
def index(name=None):
    global thread
    if thread is None:
        thread = Thread(target=serial_handler)
        thread.start()
    return render_template('index.html', name=name)

@socketio.on('join', namespace='/test')
def connect(message):
    join_room(message['room'])
    print('New connection')

@socketio.on('leave', namespace='/test')
def disconnect(message):
    leave_room(message['room'])
    print('An user has disconnected')

@socketio.on('my event')
def my_event():
    emit('new temp', {'temp': random()*50}, namespace='/test')

def serial_handler():
    exp = re.compile(r"#(\d)#(\d+)#\d+#")

    serial_port = Serial('/dev/ttyACM0', 9600, timeout=60)

    while 1:
        try:
            input_data = serial_port.readline().decode('utf8')
            serial_port.flushInput()
            # 4º Comprobamos si hemos leido algo y la entrada
            # sigue el patrón y sacamos los datos que necesitamos, añadiendolo a la base de datos.
            if len(input_data ) == 0:
                print("Whoops, check arduino")
                break
            elif exp.match(input_data):
                dato =  exp.match(input_data)
                # create_medicion(int(dato.group(1)), int(dato.group(2)))
                #print(int(dato.group(1)), int(dato.group(2)))
                socketio.emit('new temp', {'temp': dato.group(2)}, namespace='/test')
                print(f">>{dato.group(2)}")
            else:
                print("Canario puto")
            time.sleep(1)

        except SerialException:
            print("Sorry, we lost connection")
            break

    serial_port.close()

if __name__ == '__main__':
    socketio.run(app)
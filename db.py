from peewee import Model, IntegerField, ForeignKeyField, CharField, SqliteDatabase, DateTimeField
import configparser, datetime

# Idicamos el nombre de la base de datos

db = SqliteDatabase("datos.db")


# Tablas que contienen la base de datos

class BaseModel(Model):
    class Meta:
        database = db


class Sensor(BaseModel):
    id = IntegerField(primary_key=True)
    nombre = CharField(max_length=50)


class Dato(BaseModel):
    id = ForeignKeyField(Sensor, backref="mediciones")
    fecha = DateTimeField(default=datetime.datetime.now, primary_key=True) # Si no se expecifica otro dato, se asigna la fecha actual
    valor = IntegerField()

# Funciones para insertar sensores y sus mediciones
db.connect()


def create_sensor(id, nombre):
    with db.atomic():
        Sensor.create(id=id, nombre=nombre)

def create_medicion(id, valor):
    with db.atomic():
        Dato.create(id=id, valor=valor)

# Algunas consultas básicas

def get_sensores():
    return list(Sensor.select().dicts())

def get_mediciones(id):
    sensor= Sensor.select().where(Sensor.id == id)
    return list(sensor.mediciones.dicts()) if len(list(sensor))>0 else []

# Solo se ejecuta si lanzas directamente el fichero

if __name__ == "__main__":
    if not Sensor.table_exists():
        Sensor.create_table()
    if not Dato.table_exists():
        Dato.create_table()
    # Definimos los sensores que tenemos
    create_sensor(1, "HRC-04")

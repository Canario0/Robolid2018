# Robolid2018 
## Curso de recolección de datos con arduino, peewee, pyserial y flask 
 
### Introducción 
Este curso es una continuación del taller anterior, en el que usaremos python y algunas de sus librerías (peewee para manejar los datos, pyserial para transmitir la información y flask para mostrar los datos en web) 
 
En caso de que no tengas python instalado o no sepas instalar las librerías necesarias, [aqui tienes una guia de instalación.](INSTALL.md) 
 
### Funcionamiento 
Este repositorio esta dividido en varios branches, cada uno centrado en una parte especifica. El orden en el que se explicaran y trabajaran es el siguiente: 
 
- En el branch Pyserial crearemos un programa en Python básico con el que nos comunicaremos con el arduino a través de serial para recibir la información de los sensores en nuestro programa 
 
- En el branch Pyserial + Peewee organizaremos los datos recibidos en una base de datos para que estos sean persistentes entre ejecuciones del programa 
 
- En el branch Pyserial + Peewee + Flask crearemos una página web básica que muestre los datos recibidos del arduino con gráficas
 

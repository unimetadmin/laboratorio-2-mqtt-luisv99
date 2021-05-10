import ssl
import sys
import json
import random
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import time
import datetime



def on_connect(client, userdata, flags, rc):
	print('conectado publicador')

def main():
    client = paho.mqtt.client.Client("luisv99", False)
    client.qos = 0
    client.connect(host='localhost')
    hora_actual = datetime.datetime.now()
    while(True):
        #Tanque de agua
        time.sleep(1)
        capacidad_tanque = 100
        media = 10
        desviacion = 5
        capacidad_tanque = 3*((capacidad_tanque) - (capacidad_tanque - np.random.normal(media , desviacion)))
        if capacidad_tanque <= 50 and capacidad_tanque >0 :
            hora_actual = hora_actual + datetime.timedelta(minutes=10)
            payload_capacidad_tanque = {
                "Area": "bano",
                "Nivel_Agua": str(capacidad_tanque),
                "Alerta": "Se esta acabando el agua",
                "Hora": str(hora_actual)
            }
            client.publish('casa/bano/tanque',json.dumps(payload_capacidad_tanque),qos=0)		
            print(payload_capacidad_tanque)

        if capacidad_tanque >50:
            hora_actual = hora_actual + datetime.timedelta(minutes=10)
            payload_capacidad_tanque = {
                "Area": "bano",
                "Nivel_Agua": str(capacidad_tanque),
                "Alerta": "El nivel de agua bajo pero hay suficiente",
                "Hora": str(hora_actual)
            }
            client.publish('casa/bano/tanque',json.dumps(payload_capacidad_tanque),qos=0)		
            print("Capacidad actual del tanque", capacidad_tanque)
            print(payload_capacidad_tanque)

        if capacidad_tanque <=0:
            hora_actual = hora_actual + datetime.timedelta(minutes=10)
            capacidad_tanque= 0
            payload_capacidad_tanque = {
                "Area": "bano",
                "Nivel_Agua": str(capacidad_tanque),
                "Alerta": "Se acabo el agua",
                "Hora": str(hora_actual)
            }
            client.publish('casa/bano/tanque',json.dumps(payload_capacidad_tanque),qos=0)	
            print("Capacidad actual del tanque", capacidad_tanque)	
            print(payload_capacidad_tanque)
        
        if capacidad_tanque < 100:
            hora_actual = hora_actual + datetime.timedelta(minutes=30)
            time.sleep(1)
            media2 = 20
            desviacion2 = 5
            capacidad_tanque = capacidad_tanque + np.random.normal(media2 , desviacion2)
            if capacidad_tanque > 100:
                capacidad_tanque= 100
            payload_capacidad_tanque = {
                "Area": "bano",
                "Nivel_Agua": str(capacidad_tanque),
                "Alerta": "El nivel de agua subio",
                "Hora": str(hora_actual)
            }
            client.publish('casa/bano/tanque',json.dumps(payload_capacidad_tanque),qos=0)		
            print(payload_capacidad_tanque)
        
if __name__ == '__main__':
	main()
	sys.exit(0)
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

		#Contador de personas en la sala
		hora_actual = hora_actual + datetime.timedelta(minutes=1)
		contador_personas = int(np.random.uniform(0, 10))
        
		if contador_personas < 5:
			payloadPersonas = {
			"Area": "salaCont",
			"Cantidad_personas": str(contador_personas),
			"Alerta": "No hay riesgo de COVID",
			"Hora": str(hora_actual)
		}
			client.publish('casa/sala/conta_personas',json.dumps(payloadPersonas),qos=0)	
			print(payloadPersonas)
		else: 
			payloadPersonas2 = {
			"Area": "salaCont",
			"Cantidad_personas": str(contador_personas),
			"Alerta": "Hay riesgo de COVID",
			"Hora": str(hora_actual)
		}
			client.publish('casa/sala/conta_personas',json.dumps(payloadPersonas2),qos=0)
			print(payloadPersonas2)	
		time.sleep(1)

        
if __name__ == '__main__':
	main()
	sys.exit(0)
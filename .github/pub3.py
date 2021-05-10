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
		hora_actual = hora_actual + datetime.timedelta(seconds=1)
		#Temperatura de la olla
		temp_olla = int(np.random.uniform(0, 150))
		if temp_olla >= 100:
			payloadOlla2 = {
			"Area": "cocinaO",
			"Temperatura_olla": str(temp_olla),
			"Agua": "Hervida",
			"Hora": str(hora_actual)
		}
			client.publish('casa/cocina/temp_olla',json.dumps(payloadOlla2),qos=0)	
			print(payloadOlla2)
		else: 
			payloadOlla = {
			"Area": "cocinaO",
			"Temperatura_olla": str(temp_olla),
			"Agua": "No Hervida",
			"Hora": str(hora_actual)
		}
			client.publish('casa/cocina/temp_olla',json.dumps(payloadOlla),qos=0)
			print(payloadOlla)	
		time.sleep(1)

        
if __name__ == '__main__':
	main()
	sys.exit(0)

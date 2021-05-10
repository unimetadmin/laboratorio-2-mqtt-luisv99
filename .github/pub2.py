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
		#capacidad de hielos de la nevera
		hora_actual = hora_actual + datetime.timedelta(minutes=10)
		hielos = int(np.random.uniform(0, 10))
		payloadHielo = {
			"Area": "cocinaH",
			"Hielo": str(hielos),
			"Hora": str(hora_actual)
		}
		client.publish('casa/cocina/temp_nevera',json.dumps(payloadHielo),qos=0)		
		print(payloadHielo)
		time.sleep(1)

        
if __name__ == '__main__':
	main()
	sys.exit(0)

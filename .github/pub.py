import ssl
import sys
import json
import random
import datetime
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np




def on_connect(client, userdata, flags, rc):
	print('conectado publicador')

def main():
	client = paho.mqtt.client.Client("luisv99", False)
	client.qos = 0
	client.connect(host='localhost')
	hora_actual = datetime.datetime.now()
	while(True):
		media = 10
		desv = 2
		hora_actual = (hora_actual + datetime.timedelta(minutes=5))
		#Temperatura de la nevera
		temp_nevera = int(np.random.normal(media, desv))
		payloadTemp = {
			"Area": "cocinaN",
			"Temperatura_nevera": str(temp_nevera),
			"Hora": str(hora_actual)
		}
		client.publish('casa/cocina/temp_nevera',json.dumps(payloadTemp),qos=0)		
		print(payloadTemp)
		time.sleep(1)
#--------------------------------------------------------------------------------------------


        
if __name__ == '__main__':
	main()
	sys.exit(0)


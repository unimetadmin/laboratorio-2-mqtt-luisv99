import ssl
import sys
import json
import random
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import time
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
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
        hora_actual = hora_actual + datetime.timedelta(minutes=45)
        owm = OWM('965a331e559460571664166472115691') #API KEY
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place('Caracas')
        w = observation.weather
        temp = w.temperature('celsius')
        tempCcs = temp['temp']
        payloadAlexa = {
			"Area": "salaAlexa",
			"Temperatura_caracas": str(tempCcs),
            "Hora": str(hora_actual)
		}
        client.publish('casa/sala/alexa',json.dumps(payloadAlexa),qos=0)		
        print(payloadAlexa)
        time.sleep(1)

        
if __name__ == '__main__':
	main()
	sys.exit(0)

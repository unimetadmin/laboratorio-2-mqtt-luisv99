import sys
import paho.mqtt.client
import psycopg2
from psycopg2.extras import Json
import json

connection = psycopg2.connect(user="lvqfpovj",
                                  password="gmdtsPmJsSGibIXp-oTFYP93W1oYNkjh",
                                  host="queenie.db.elephantsql.com",
                                  port="5432",
                                  database="lvqfpovj")


def filtroQuery(p): 
	if p['Area'] == "cocinaN":
		query = """INSERT INTO Nevera (Temperatura, Fecha_Hora)
		VALUES(%s,%s);"""
		doQuery( query, p["Temperatura_nevera"], p["Hora"])

	if p['Area'] == "cocinaH":
		query = """INSERT INTO Hielo (Capacidad, Fecha_Hora)
		VALUES(%s,%s);"""
		doQuery( query, p["Hielo"],p["Hora"] )

	if p['Area'] == "cocinaO":
		query = """INSERT INTO Olla (Temperatura, Status_Agua, Fecha_Hora)
		VALUES(%s,%s,%s);"""
		doQuery( query, p["Temperatura_olla"], p["Agua"],p["Hora"] )

	if p['Area'] == "salaCont":
		query = """INSERT INTO Contador (Cantidad_Personas, Alerta, Fecha_Hora)
		VALUES(%s,%s,%s);"""
		doQuery( query, p["Cantidad_personas"], p["Alerta"],p["Hora"] )

	if p['Area'] == "salaAlexa":
		query = """INSERT INTO Alexa (temperatura_Caracas, Fecha_Hora)
		VALUES(%s,%s);"""
		doQuery( query, p["Temperatura_caracas"],p["Hora"])
	
	if p['Area'] == "bano":
		query = """INSERT INTO Tanque (Nivel_agua, Alerta, Fecha_Hora)
		VALUES(%s,%s,%s);"""
		doQuery( query, p["Nivel_Agua"], p["Alerta"],p["Hora"])



def doQuery(query, *args):
	cur = connection.cursor()
	try:
		cur.execute(query, args)
	except Exception as e:
		connection.commit()
		print('error en el query', e)
	else:
		connection.commit()
		cur.close()


def on_connect(client, userdata, flags, rc):
	#print('connected (%s)' % client._client_id)
	client.subscribe(topic='casa/cocina/temp_nevera', qos=2)
	client.subscribe(topic='casa/cocina/temp_olla', qos=2)
	client.subscribe(topic='casa/sala/conta_personas', qos=2)
	client.subscribe(topic='casa/sala/alexa', qos=2)
	client.subscribe(topic='casa/bano/tanque', qos=2)

	query = """CREATE TABLE if not exists Nevera (
	Id serial NOT NULL PRIMARY KEY, 
	Temperatura INT NOT NULL,
	Fecha_Hora VARCHAR(30));"""
	doQuery(query)

	query2 = """CREATE TABLE if not exists Hielo (
	Id serial NOT NULL PRIMARY KEY, 
	Capacidad INT NOT NULL,
	Fecha_Hora VARCHAR(50) );"""
	doQuery(query2)

	query3 = """CREATE TABLE if not exists Olla (
	Id serial NOT NULL PRIMARY KEY, 
	Temperatura INT NOT NULL,
	Status_Agua VARCHAR (15) NOT NULL,
	Fecha_Hora VARCHAR(50) );"""
	doQuery(query3)

	query4 = """CREATE TABLE if not exists Contador (
	Id serial NOT NULL PRIMARY KEY, 
	Cantidad_Personas INT NOT NULL,
	Alerta VARCHAR (50) NOT NULL,
	Fecha_Hora VARCHAR(50) );"""
	doQuery(query4)

	query5 = """CREATE TABLE if not exists Alexa (
	Id serial NOT NULL PRIMARY KEY, 
	Temperatura_Caracas DECIMAL NOT NULL,
	Fecha_Hora VARCHAR(50));"""
	doQuery(query5)
	
	query6 = """CREATE TABLE if not exists Tanque (
	Id serial NOT NULL PRIMARY KEY, 
	Nivel_agua DECIMAL NOT NULL,
	Alerta VARCHAR (100) NOT NULL,
	Fecha_Hora VARCHAR(50));"""
	doQuery(query6)


def on_message(client, userdata, message):
	p = json.loads(message.payload)
	print(p)
	print('------------------------------')
	print('topic: %s' % message.topic)
	print('payload: %s' % message.payload)
	print('qos: %d' % message.qos)
	
	if p['Area']=="cocinaN":
		filtroQuery(p)
	if p['Area']=="cocinaH":
		filtroQuery(p)
	if p['Area']=="cocinaO":
		filtroQuery(p)
	if p['Area']=="salaCont":
		filtroQuery(p)
	if p['Area']=="salaAlexa":
		filtroQuery(p)
	if p['Area']=="bano":
		filtroQuery(p)
	



def main():
	client = paho.mqtt.client.Client(client_id='lab2-subs', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()


if __name__ == '__main__':
	main()

sys.exit(0)
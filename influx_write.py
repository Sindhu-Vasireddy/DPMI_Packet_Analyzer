#!/usr/bin/python
from influxdb import InfluxDBClient
import time

''' 
# testing purpose
host='localhost'
user = 'root'
password = 'root'
DBNAME = 'DPMI5'
port=8086
'''

def new_db(host, port, USER, PASSWORD, DBNAME):
	json_body = [
	 {
	 "measurement":"tablestream",
	 "tags":{
		  "source":"server01",
		  "destination":"server-02",
		  "protocol":int(26532),
		},
	 #"time":int(time.time()),
	 "fields": {
	    "packets":int(6348),
	   }
	   }
	  ] 

	client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
	client.create_database(DBNAME)
	#client.write_points(json_body)
	#result = client.query('select protocol from tablestream;')
	#return ("Result: {0}".format(result))
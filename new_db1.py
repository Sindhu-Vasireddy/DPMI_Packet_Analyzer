#!/usr/bin/python

from influxdb import InfluxDBClient,DataFrameClient
from influx_write import new_db
import time
import json

# Parameters for the influxdb settings
host='localhost'
USER = 'root'
PASSWORD = 'root'
DBNAME = 'DPMI5'
port=8086
client = InfluxDBClient(host, port, USER, PASSWORD,DBNAME)
client1 = DataFrameClient(host, port, USER, PASSWORD,DBNAME)
series = []
##date=time.time

# Function for writing up the database entries.
def influx_entry(source,destination,packets,protocol,host='localhost', port=8086):
    resultset = client.query('show databases')
    databases = [i['name'] for i in resultset.get_points()]
    if not DBNAME in databases:
       new_db(host, port, USER, PASSWORD,DBNAME) 

    elif DBNAME in databases:
            pointValues = {
                    "measurement":"tablestream",
                    "tags":{
                        'source':source,
                        'destination':destination,
                        'protocol':int(protocol)
                           },
                    "fields":{
                        'packets':int(packets),
                          }
                          }
            series.append(pointValues)
    print series

    print("Create a retention policy")
    retention_policy = 'server_data'
    client.create_retention_policy(retention_policy, '1h', 2, default=True)

    client.write_points(series, retention_policy=retention_policy)
    time.sleep(2)

def read_data():
    return client.query("select * from tablestream")

def read_data1():
    return client1.query("select * from tablestream")

def adding_data(p):
      print "I am about to add the entry!!!"
      while True:
        value=p.stdout.readline()
        print value,
        if len(value) == 0 or value=='' or p.poll()!=None:
              continue
        try:
              list_value = json.loads(value)
        except:
              continue
        for vlist in list_value:
              source,protocol,destination = vlist[0].split('-')
              packets=vlist[1]
              print source,protocol,destination,packets
              print "making a database entry"
              influx_entry(source,destination,packets,protocol)
              print source,protocol,destination,packets
      return "Done"


# DPMI_PACKET_ANALYZER: Understanding of how to run the code.

## Checklist
Before running the code, please ensure that you have completed the following checklist:

- [x] Make sure the mp stream is running.
- [x] Make sure InfluxDB is running fine.
- [x] Make sure you have all the required Python modules installed as specified in the requirements.txt file.

## Pre-Requisites
To install the requirements from the requirements.txt file, follow these steps:

1. Install Python package manager (pip) if not already installed:
```sudo apt-get install python-pip```

2. Install the required Python modules from requirements.txt:
```sudo pip install -r requirements.txt```

3. Verify if all the required modules have been installed:
```pip freeze```

## Procedure
- Getting started with running the application:

To get started with running the application, you need to run the app.py. Before running the app.py, make sure that you switch to the root user as follows.

``` sudo -s python app.py```

### 1) starting the analyzer application

- If you want to pass two values, use the following command:
``` curl -i "http://0.0.0.0:8083/start?streamname1=01::10:01&streamname2=01::10:02" -u <userName>:<password>```

- If you want to pass three values, use the following command:
``` curl -i "http://0.0.0.0:8083/start?streamname1=01::10:01&streamname2=01::10:02&streamname3=01::10:03" -u <userName>:<password>```

For example:
``` curl -i "http://0.0.0.0:8083/start?streamname1=01::10:01&streamname2=01::10:02" -u admin:secret ```
```http 
HTTP/1.0 200 OK
Content-Type: application/json
Set-Cookie: session=eyJzdHJlYW0iOnsiIGIiOiJNREU2T2pjeSJ9fQ.DB7CLA.Cy_JADjYszkrdZdyR34gW9aepYw; HttpOnly; Path=/
Content-Length: 37
Server: Werkzeug/0.12 Python/2.7.9
Date: Sun, 11 Jun 2017 11:59:40 GMT
```
Note: If you now open InfluxDB, you should see the database created. Also, if you check the console where you ran app.py, you will see the output getting populated.

Additionally you can execute the following commands using the analyzer application:

### 2) Finding the status of the tophost:
```curl -i "http://localhost:8083/status" -u <userName>:<password>```
### 3) Total number of packets exchanged:
```curl -i "localhost:8083/tpe" -u <userName>:<password>```
### 4) Maximum packet:
```curl -i "localhost:8083/max_packet" -u <userName>:<password>```
### 5) Minimum packet:
```curl -i "localhost:8083/min_packet" -u <userName>:<password>```
### 6) Last packet:
```curl -i "localhost:8083/last_packet" -u <userName>:<password>```
### 7) Most Active packets:
```curl -i "localhost:8083/active_tuple" -u <userName>:<password>```
### 8) Average number of packets exchanged:
```curl -i "localhost:8083/average_packets" -u <userName>:<password>```
### 9) Seeing the content of the database:
```curl -i "localhost:8083/tasks" -u <userName>:<password>```
### 10) Stopping the application:
```curl -i "localhost:8083/stop" -u <userName>:<password>```
# DPMI Packet Analyzer App

The Packet Analyzer is a Python-based application designed for network traffic analysis and monitoring. It allows users to capture and analyze packets exchanged in a network stream and provides various statistics related to the traffic data.

## Capabilities

The Packet Analyzer app offers the following capabilities:

1. **Starting the Analyzer Application**: To start the Packet Analyzer application, run [`app.py`](app.py). Before running the script, ensure that you have completed the checklist mentioned in the [How to Run](how_to_run.md) guide.

2. **Capture and Analyze Network Traffic**: The Packet Analyzer is capable of capturing and analyzing network traffic for multiple streams concurrently. You can start the analysis by sending a CURL command with stream names to the application.

3. **Stopping the Analysis**: To stop the analysis, use the appropriate CURL command.

4. **Status of the Tophost**: Check the status of the analysis process with a CURL command.

5. **Network Traffic Statistics**: Obtain various statistics related to the packets exchanged in the network streams. This includes total number of packets exchanged, maximum packet, minimum packet, last sample packet, most active tuple, and average number of packets exchanged.

6. **View Database Content**: You can view the content of the database where the packet data is stored.

## Installation and Requirements

Before running the application, ensure that the following prerequisites are met:

1. Make sure the `"mp stream"` is running.
2. Ensure InfluxDB is operational.
3. Install the required Python modules specified in `requirements.txt` as follows:
   ``` pip install -r requirements.txt```

For detailed installation instructions and requirements, refer to the [How to Run](how_to_run.md) guide.

## InfluxDB Configuration

The Packet Analyzer uses InfluxDB for storing the captured packet data. The database connection settings are defined in the `influx_write.py` file. Modify the host, port, username, password, and database name as required.

### Influx Write and Database Functions

The [`influx_write.py`](influx_write.py) file contains functions for writing data to the InfluxDB database. The `new_db()` function creates the database, while the `influx_entry()` function writes data points to the database.

The [`new_db1.py`](new_db1.py) file provides additional functions for reading and adding data to the database. The `adding_data()` function is used to continuously add data points to the database while the analysis is running.

## Starting the Packet Analysis

To start the packet analysis, run `app.py`, and use the provided CURL commands to initiate and control the analysis process. The application will collect packet data, and you can access various statistics related to the network traffic.

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

Additionally, Before running the app using [`app.py`](app.py), ensure that you have completed the checklist mentioned in the [How to Run](how_to_run.md) guide.

Enjoy using the Packet Analyzer to gain insights into your network traffic and streamline your network analysis tasks!

## Acknowledgements
We are now able to handle multiple streams and have tried our best to make the code have better practical implications from a customer's perspective, as per the changes proposed by our Prof. Patrik Arlos. We thank him for all the guidance and support. Detailed progress of the app development is documented in [`ProgressTracker.md`](ProgressTracker.md)

from flask import Flask,request,jsonify,session,render_template, request,redirect,url_for
from flask_restful import Resource, Api
import new_db1
import json
import subprocess
from subprocess import Popen, PIPE,STDOUT
import signal
import os
from threading import Thread
from functools import wraps
from flask import request, Response

#Flask relative settings
app = Flask(__name__)
api = Api(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PORT=8083
p=None

# Authentication
# flask.pocoo.org/snippets/8/

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated



# Define a route for the default URL, which loads the information on how to
# run the app.
#http://localhost:<portnumber>/
@app.route('/')
def form():
    return render_template('how_to_run.html')

##
#the below link /start s open via the form_submit.html page.
##
@app.route('/start',methods=['GET'])
@requires_auth
def influx_insert():
  values = request.args.to_dict().values()
  print values
  for stream in values:
      #stream=values['streamname']  # we are pulling this from the curl command
      print stream
      session['stream'] = str(stream)
      print "We have passed this stream:{}".format(stream)
      global p
      p = Popen(["./run_tophosts.sh", "{}".format(stream)], stdout=PIPE,stderr=PIPE,close_fds=True)
      background_insert = Thread(target=new_db1.adding_data,args=(p,))
      background_insert.start()
      print p
  return jsonify("The tophost has started running!!!")

                     

##
#the below link /stop is to stop the tophost process.
##

@app.route('/stop',methods=['GET'])
@requires_auth
def stop_tophost():
    child = subprocess.Popen(['pgrep','tophost'],stdout=subprocess.PIPE)
    output=child.communicate()
    for value in [ int(value) for value in output[0].split('\n') if len(value) > 0]:
      print "Killing the process id - {}".format(value)
      os.kill(value,signal.SIGKILL)
    return jsonify("Time for a Break ")


##
#the below link /status is to find status of the tophost process.
##
@app.route('/status',methods=['GET'])
@requires_auth
def status_tophost():
    child = subprocess.Popen(['pgrep','tophost'],stdout=subprocess.PIPE)
    output=child.communicate()
    if len(output[0].split('\n')) > 1:
      return jsonify("The tophost is running great !!!")
    else:
      return jsonify("The tophost is not running !!!")

##
# This is for finding the maximum number of  - done
# packets exchanged.
##

@app.route('/tpe', methods=['GET'])
@requires_auth
def total_packets_exchanged():
  stream=session.get('stream')
  packets=session.get('packets')
  data = new_db1.read_data1()['tablestream']
  # tail(10) represents the latest 10 packets
  res = {
  'number_packets_exchanged':data.packets.tail(10).sum()
   }
  return jsonify(str(res))

##
# This is for finding the maximum packet. - done
# 
##
@app.route('/max_packet', methods=['GET'])
@requires_auth
def maximum_packet():
  stream=session.get('stream')
  packets=session.get('packets')
  data = new_db1.read_data1()['tablestream']
  data1=data[data['packets']==data.packets.max()][['source','destination','packets']]
  '''
  # data1 collects all the packtes which have max packet data.
  # if you want to check it go ahead and put data1 in the res value.
  '''
 
  res = {
  'max_packets':data1.iloc[0],
   }
  return jsonify(str(res))


##
# This is for finding the minimum packet. - done
# 
##
@app.route('/min_packet', methods=['GET'])
@requires_auth
def minimum_packet():
  data = new_db1.read_data1()['tablestream']
  data1=data[data['packets']==data.packets.min()][['source','destination','packets']]
  '''
  # data1 collects all the packtes which have max packet data.
  # if you want to check it go ahead and put data1 in the res value.
  '''
  
  res = {
  'min_packets':data1.iloc[0],
   }
  return jsonify(str(res))

##
# This is for last sample packet. - done 
# 
##
@app.route('/last_packet', methods=['GET'])
@requires_auth
def last_packet():
  data = new_db1.client.query("select * from tablestream")
  pdata = list(data.get_points(measurement = 'tablestream'))
  res = {
  'last_sample_packets':str(pdata[0])
   }
  return jsonify(str(res))

##
# This is for the most active tuple. - done
# 
##

@app.route('/active_tuple', methods=['GET'])
@requires_auth
def most_active_tuple():
  stream=session.get('stream')
  packets=session.get('packets')
  data = new_db1.read_data1()['tablestream']
  res = {
  'most_active_tuple':(data.groupby('source').count()['destination'].tail(),
    data.groupby('destination').count()['source'].tail()
    )
   }
  return jsonify(str(res))


##
# This is for the average number of packets.  - TODO
##

@app.route('/average_packets', methods=['GET'])
@requires_auth
def average_packet():
  data = new_db1.read_data1()['tablestream']
  # tail(10) represents the 10 records.
  res = {
    'average_number_packets': data.packets.tail(10).mean()
   }
  return jsonify(str(res))

##
# This is to verify all the packets that are appliced till now. - done
##

@app.route('/tasks', methods=['GET'])
@requires_auth
def index():
  output=new_db1.read_data()
  res = {
    'average_number_packets': str(output)
   }
  return jsonify(str(output))
    

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=PORT)


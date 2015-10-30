import zmq
import sys
import random
import json

try:
    gatewayid = sys.argv[1]
except:
    gatewayid = 'GDM01'

data = {
    "UUID":gatewayid,
    "requestid":"289325",
    "payload":"0",
    "transducers":"ARE01",

}

jsn = json.dumps(data)
port = "5550"
context = zmq.Context()
print "Sending Data to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
socket.send_json (jsn)


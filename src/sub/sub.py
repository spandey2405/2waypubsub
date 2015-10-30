import sys
import zmq
import json
#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)


socket.connect("tcp://localhost:5552")

# Subscribe to zipcode, default is NYC, 10001
gateway_id = sys.argv[1] if len(sys.argv) > 1 else "GDM01"

# Python 2 - ascii bytes to unicode str
if isinstance(gateway_id, bytes):
    gateway_id = gateway_id.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, gateway_id)
print("Gateway Server : %s Online" % gateway_id)

def demogrify(topicmsg):
    """ Inverse of mogrify() """
    json0 = topicmsg.find('{')
    topic = topicmsg[0:json0].strip()
    msg = json.loads(topicmsg[json0:])
    return topic, msg

def send_message(jsn):
    port = "5551"
    context = zmq.Context()
    print "Sending Data to server..."
    socket = context.socket(zmq.REQ)
    socket.connect ("tcp://localhost:%s" % port)
    socket.send_json (jsn)
    
while True:
    topic, msg = demogrify(socket.recv())
    a = json.dumps(msg)
    res = send_message(a)
    # if res == True:
    #     print "Responce Forwarded"

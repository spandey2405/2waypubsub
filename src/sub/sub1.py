import sys
import zmq
import json
#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)


socket.connect("tcp://localhost:5553")

# Subscribe to zipcode, default is NYC, 10001
request_id = sys.argv[1] if len(sys.argv) > 1 else "289325"

# Python 2 - ascii bytes to unicode str
if isinstance(request_id, bytes):
    request_id = request_id.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, request_id)
print("Gateway Server : %s Online" % request_id)

def demogrify(topicmsg):
    """ Inverse of mogrify() """
    json0 = topicmsg.find('{')
    topic = topicmsg[0:json0].strip()
    msg = json.loads(topicmsg[json0:])
    return topic, msg

while True:
    topic, msg = demogrify(socket.recv())
    print msg


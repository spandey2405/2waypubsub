import sys
import zmq

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
while True:
    string = socket.recv_json()
    print string


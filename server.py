import zmq
import time
import sys
import random
import json

port = "5560"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:%s" % port)

context_send = zmq.Context()
socket_send = context.socket(zmq.PUB)
socket_send.bind("tcp://*:5552")

while True:
    #  Wait for next request from client
    message = socket.recv()
    message = json.loads(message)
    print "Received request: ", message['UUID']
    socket.send("World from server")
    uid = message['UUID']
    socket_send.send_string('%s %s' % (uid,message))
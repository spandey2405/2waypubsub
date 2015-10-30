__author__ = 'sp'
import zmq
import time
import sys
import random
import json

def pub_start():
    port = "5560"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:%s" % port)

    context_send = zmq.Context()
    socket_send = context.socket(zmq.PUB)
    socket_send.bind("tcp://*:5552")

    def mogrify(filter, jsn):
        """ json encode the message and prepend the topic """
        return filter + ' ' + json.dumps(jsn)


    while True:
        #  Wait for next request from client
        message = socket.recv_json()
        message = json.loads(message)
        print message
        socket.send_string("World from server")
        uid = message['UUID']
        socket_send.send_string(mogrify(uid, message))

if __name__ == '__main__':
    pub_start()
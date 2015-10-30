import zmq

def main():

    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.XREP)
        frontend.bind("tcp://*:5551")
        # Socket facing services
        backend = context.socket(zmq.XREQ)
        backend.bind("tcp://*:5561")

        zmq.device(zmq.QUEUE, frontend, backend)
    except Exception, e:
        print e
        print "bringing down zmq device"

if __name__ == "__main__":
    main()
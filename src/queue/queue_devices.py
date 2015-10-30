from src.queue import queue_request
from src.queue import queue_responce

class queue():

    def start_queue(self):
        # Queue for request
        queue_request.main()

        # Queue for responce
        queue_responce.main()

def init():
    a = queue()
    a.start_queue()


if __name__ == '__main__':
    init()

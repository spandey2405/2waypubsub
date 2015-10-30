from src.server import pub_request
from src.server import pub_responce

class server():

    def start_pub(self):
        # Queue for request
        pub_request.pub_start()

        # Queue for responce
        pub_responce.pub_start()

def init():
    a = server()
    a.start_pub()


if __name__ == '__main__':
    init()

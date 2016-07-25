import zmq


ERROR = b'Fail'
SUCCESS = b'Done'


class ClientOrServer(object):

    def __init__(self, port=5000):
        self.port = port

    def __enter__(self):
        self.context = zmq.Context().__enter__()
        self.socket = self.context.socket(zmq.PAIR)
        self.connect_or_bind()
        return self

    def start(self):
        self.__enter__()

    def close(self):
        self.__exit__()

    def __exit__(self, *args, **kwargs):
        self.socket.close()
        self.context.__exit__(*args, **kwargs)


class Server(ClientOrServer):
    """Callback takes message as argument and returns success as boolean.

    Once the run() has been launched the server passes received messages
    to the callback and sends back success status.
    """

    def __init__(self, port=5000, callback=lambda _: True):
        super(Server, self).__init__(port=port)
        self.callback = callback
        self.running = False

    def _socket_address(self):
        return "tcp://*:{}".format(self.port)

    def connect_or_bind(self):
        self.socket.bind(self._socket_address())

    def run(self):
        self.running = True
        while self.running:
            cmd = self.socket.recv()
            result = self.callback(cmd)
            self.socket.send(SUCCESS if result else ERROR)


class Client(ClientOrServer):

    def __init__(self, port=5000, address="localhost"):
        super(Client, self).__init__(port=port)
        self.address = address

    def _socket_address(self):
        return "tcp://{}:{}".format(self.address, self.port)

    def connect_or_bind(self):
        self.socket.connect(self._socket_address())

    def send_command(self, command):
        """Sends command to server and waits for success value.

        Raises exception on failure from server. Command must be a byte
        string.
        """
        assert(type(command) is bytes)
        self.socket.send(command)
        ans = self.socket.recv()
        if ans == ERROR:
            raise ValueError("Server failed to execute.")
        elif ans == SUCCESS:
            return
        else:
            raise ValueError("Unknown message: " + ans)

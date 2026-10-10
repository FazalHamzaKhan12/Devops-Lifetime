class Server:

    def __init__(self, status):
        self.status = status


def start_server(server):
    # 'server' refers to the SAME Server object
    # that 'my_server' refers to
    server.status = "running"


my_server = Server("stopped")

# Reference to the Server object is passed here
start_server(my_server)

print(my_server.status)
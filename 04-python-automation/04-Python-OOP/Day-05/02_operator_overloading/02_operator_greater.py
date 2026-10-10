class Server:

    def __init__(self, memory):
        self.memory = memory


    def __gt__(self, other):
        return self.memory > other.memory


server1 = Server(16)
server2 = Server(8)

print(server1 > server2)
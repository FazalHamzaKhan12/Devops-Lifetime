class Server:

    def __init__(self, cpu):
        self.cpu = cpu

    def __add__(self, other):
        return self.cpu + other.cpu

    def __sub__(self, other):
        return self.cpu - other.cpu


server1 = Server(50)
server2 = Server(40)


print(server1 + server2)
print(server1 - server2)

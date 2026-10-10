class Server:

    def __init__(self,name , ip):
        self.name = name
        self.ip = ip


class Deployment:

    def __init__(self, application, server):
        self.name = application

        # Deployment HAS-A Server
        self.server = server


server1 = Server("Web-Server", "10.0.0.10")

depl1 = Deployment("My-APP", server1)

print(depl1.name)
print(depl1.server.name)
print(depl1.server.ip)

        
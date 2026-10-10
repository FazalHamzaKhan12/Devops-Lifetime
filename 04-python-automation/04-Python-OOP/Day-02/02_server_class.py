class Server:

    def __init__(self, name, ip , environment):
        self.name = name
        self.ip = ip
        self.environment = environment

    def show_info(self):
        print(f"Server: {self.name}")
        print(f"IP: {self.ip}")
        print(f"Environment: {self.environment}")

server1 = Server("web-server", "10.0.0.10", "production")

server2 = Server("api-server", "10.0.0.20", "staging")

server1.show_info()
server2.show_info()
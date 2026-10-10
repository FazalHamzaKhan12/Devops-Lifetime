class Server:
    def configure(self, name, ip=None):
        if ip is None:
            print(f"Configuring server: {name}")
        else:
            print(f"Configuring servers: {name}")
            print(f"IP Address: {ip}")


server1 = Server()

server1.configure("web-server")
server1.configure("web-server", "192.3.2.4")

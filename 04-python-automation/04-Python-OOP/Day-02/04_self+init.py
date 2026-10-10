class Server:

    def __init__(self, s_name, ip, environmnet,statsi):
        self.server_name = s_name
        self.ip_address = ip
        self.environemtn = environmnet
        self.status = statsi


    def show_info(self):
        print(f"Server: {self.server_name}")
        print(f"IP: {self.ip_address}")
        print(f"Environment: {self.environemtn}")
        print(f"Status: {self.status}")



server1 = Server("dev-server", "10.0.0.10", "development", "Running") 
server2 = Server("prod-server", "10.0.0.20", "production","Running")


server1.show_info()
server2.show_info()
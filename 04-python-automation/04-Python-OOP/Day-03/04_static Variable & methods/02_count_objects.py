class Server:

    # Static/Class variable
    # One value shared by the whole class
    total_servers = 0

    def __init__(self, name):
        self.name = name

        # Increase the shared counter
        Server.total_servers += 1


server1 = Server("Web Server")
server2 = Server("Database Server")
server3 = Server("Backup Server")

# There are 3 Server objects
print(Server.total_servers)
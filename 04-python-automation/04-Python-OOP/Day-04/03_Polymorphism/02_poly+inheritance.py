class Server:

    def start(self):
        print("starting Server")


class WebServer(Server):

    def start(self):
        print("Starting Web Server")


class DatabasesServer(Server):

    def start(self):
        print("starting a database server")


web = WebServer()
database = DatabasesServer()

servers = [web, database]

for server in servers:
    server.start()
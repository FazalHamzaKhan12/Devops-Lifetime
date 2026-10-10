class Server:

    def start(self):
        print("Server started")


class WebServer(Server):

    def website(self):
        print("Website running")


class DatabaseServer(Server):

    def database(self):
        print("Database running")


web = WebServer()
db = DatabaseServer()

web.start()
web.website()

db.start()
db.database()
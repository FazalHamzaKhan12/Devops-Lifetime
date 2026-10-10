class Server:

    # Parent class
    def start(self):
        print("Server started")

    def stop(self):
        print("Server stopped")


class WebServer(Server):

    # WebServer's own method
    def deploy_website(self):
        print("Website deployed")


web1 = WebServer()

# These methods come from Server
web1.start()
web1.stop()

# This method belongs to WebServer
web1.deploy_website()
class Server:

    def __init__(self, name, ip):
        self.name = name 
        self.ip = ip

    def start(self):
        print(f"{self.name} server started")

class WebServer(Server):

    def __init__(self, name , ip , website):
        super().__init__(name,ip)

        self.website = website

    def start(self):

    # Child's own behavior
        
        print(f"Starting web server for {self.website}")
        super().start()

web = WebServer(
    "Web-Server",
    "10.0.0.10",
    "example.com"   
)

web.start()
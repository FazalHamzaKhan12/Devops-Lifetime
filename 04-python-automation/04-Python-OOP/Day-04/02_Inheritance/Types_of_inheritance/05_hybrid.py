class Server:

    def start(self):
        print("Server started")


class LinuxServer(Server):
    
    def linux(self):
        print("Linux server")


class WindowsServer(Server):

    def windows(self):
        print("Windows server")


class DevOps(LinuxServer, WindowsServer):

    def deploy(self):
        print("Deploying")


obj = DevOps()

obj.start()
obj.linux()
obj.windows()
obj.deploy()
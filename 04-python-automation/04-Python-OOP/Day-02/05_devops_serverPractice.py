# class Server:

#     def __init__(self, serverName, ip_add, environment, status, cpu_usage):
#         self.name = serverName
#         self.ip = ip_add
#         self.env = environment
#         self.status = status
#         self.cpuusage = cpu_usage


#     def show_info(self):
#         print(f"Server: {self.name}")
#         print(f"IP: {self.ip}")
#         print(f"Environment: {self.env}")
#         print(f"Status: {self.status}")
#         print(f"CPU Usage: {self.cpuusage}%")

#     def start_server(self):
#         if self.status == "stopped" and self.cpuusage == 0:

#             print("working Loading 1,3,5,7.......99")
#             self.status = "running"
#             self.cpuusage = int(input("Enter cpu_usage: "))
#         else:
#             print("everything's Ok")

#     def stop_server(self):
#         if self.status == "running" and self.cpuusage != 0:
#             print("working Loading 1,3,5,7.......99")
#             self.status = "stopped"
#             self.cpuusage = 0
#         else:
#             print("everything's Ok")


#     def change_cpu(self):
#         change_cpu = int(input("Enter New CPU Usage: "))
#         if self.cpuusage == 0:
#             print("yoo your server is Closed")
#         elif self.cpuusage > 0:
#             self.cpuusage = change_cpu            




# server1 = Server("dev-web-server", "10.0.0.10", "development", "stopped", 0)
# server2 = Server("prod-web-server", "10.0.0.20", "production", "stopped", 0)

# server1.show_info()
# server2.show_info()

# server1.start_server()
# server1.show_info()





""" the uppper is mine coding and the below is ai written if he devops enginer/"""

class Server:

    def __init__(self, name, ip, environment, status="stopped", cpu_usage=0):
        self.name = name
        self.ip = ip
        self.environment = environment
        self.status = status
        self.cpu_usage = cpu_usage

    def show_info(self):
        print("\n--- Server Information ---")
        print(f"Server      : {self.name}")
        print(f"IP Address  : {self.ip}")
        print(f"Environment : {self.environment}")
        print(f"Status      : {self.status}")
        print(f"CPU Usage   : {self.cpu_usage}%")

    def start_server(self):
        if self.status == "stopped":
            print(f"\nStarting {self.name}...")

            self.status = "running"
            self.cpu_usage = 10

            print("Server started successfully.")

        else:
            print(f"{self.name} is already running.")

    def stop_server(self):
        if self.status == "running":
            print(f"\nStopping {self.name}...")

            self.status = "stopped"
            self.cpu_usage = 0

            print("Server stopped successfully.")

        else:
            print(f"{self.name} is already stopped.")

    def change_cpu(self):
        if self.status == "stopped":
            print(f"{self.name} is stopped. CPU usage cannot be changed.")
            return

        new_cpu = int(input("Enter new CPU usage: "))

        if 0 <= new_cpu <= 100:
            self.cpu_usage = new_cpu
            print("CPU usage updated successfully.")
        else:
            print("CPU usage must be between 0 and 100.")


# Create servers

server1 = Server(
    "dev-web-server",
    "10.0.0.10",
    "development"
)

server2 = Server(
    "prod-web-server",
    "10.0.0.20",
    "production"
)


# Display initial information

server1.show_info()
server2.show_info()


# Start development server

server1.start_server()
server1.change_cpu()

server1.show_info()

# Check production server

server2.show_info()


# Stop development server

server1.stop_server()

server1.show_info()

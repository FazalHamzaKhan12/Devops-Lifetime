class Server:

    @staticmethod
    def calculate_cpu(total, used):
        usage = (used / total) * 100
        return usage


cpu = Server.calculate_cpu(100, 70)
print(f"CPU usage: {cpu}%")
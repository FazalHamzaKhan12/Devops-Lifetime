class Network:

    @staticmethod
    def check_ip(ip):
        if "." in ip:
            print("Valid IP Format")
        else:
            print("Invalid IP Format")


Network.check_ip("39.63.181.63")
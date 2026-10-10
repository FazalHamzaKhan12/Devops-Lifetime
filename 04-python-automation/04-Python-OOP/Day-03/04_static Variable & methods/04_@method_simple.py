class Server:

    @staticmethod
    def show_os():
        # No self because we don't need a particular Server object        
        print("Linux")

# We can call it directly using the class
Server.show_os()
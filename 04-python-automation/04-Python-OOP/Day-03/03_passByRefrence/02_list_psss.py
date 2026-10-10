def add_server(servers):
    # 'servers' refers to the SAME list that 'my_servers' refers to
    servers.append("server-3")


my_servers = ["server-1", "server-2"]

# The reference to my_servers' list is passed to the function
add_server(my_servers)

print(my_servers)
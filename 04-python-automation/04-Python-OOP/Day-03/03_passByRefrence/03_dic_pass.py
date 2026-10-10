def update_server(server):
    # 'server' refers to the SAME dictionary as 'my_server'
    server["status"] = "running"


my_server = {
    "name": "web-server",
    "status": "stopped"
}

# Reference to my_server's dictionary is passed here
update_server(my_server)

print(my_server)
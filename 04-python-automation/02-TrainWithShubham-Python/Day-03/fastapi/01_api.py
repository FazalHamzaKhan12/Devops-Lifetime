from fastapi import FastAPI
import psutil

app = FastAPI(title="My First API")

@app.post("/user")
def create_user():
    return {"message": "User created"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/metrics")
def metrics():
    """Get system metrics including CPU, memory, and disk usage."""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    return {
        "cpu_percent": cpu_percent,
        "memory_info": {
            "total": memory_info.total,
            "used": memory_info.used,
            "free": memory_info.free,
            "percent": memory_info.percent
        },
        "disk_info": {
            "total": disk_info.total,
            "used": disk_info.used,
            "free": disk_info.free,
            "percent": disk_info.percent
        }
    }


@app.get("/server-info")
def server_info():
    return {
        "name": "web-server",
        "version": "1.0.0",
        "status": "running",
        "port": 8080
    }
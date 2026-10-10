import psutil

Threshold = {
    "cpu": 80.3,
    "memory": 80.5,
    "disk": 80.7
}

def collect_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }


def evaluate_metrics(name, value, threshold):
    if value > threshold:
        # Added 'False' so it returns two values during a warning
        return f"warning: {name} usage is above threshold!", False 
    return "Healthy", True 

def main():
    try:
        metrics = collect_metrics()
    except Exception as exc:  # psutil can fail on odd platforms/permissions
        print("Could not read system metrics:", exc)
        return

    print("\n=== System Health Report ===")
    all_healthy = True
    for name, value in metrics.items():
        status, healthy = evaluate_metrics(name, value, Threshold[name])
        all_healthy = all_healthy and healthy
        print(f"{name:7}: {value:5.1f}%  -> {status}")

    print("Overall:", "Healthy" if all_healthy else "NEEDS ATTENTION")


if __name__ == "__main__":
    main()
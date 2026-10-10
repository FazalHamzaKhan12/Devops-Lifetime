class AWS:

    def deploy(self):
        print("Deploying to AWS")


class Azure:

    def deploy(self):
        print("Deploying to Azure")


class Docker:

    def deploy(self):
        print("Deploying Docker container")


class Kubernetes:

    def deploy(self):
        print("Deploying to Kubernetes")



resecres = [
    AWS(),
    Azure(),
    Docker(),
    Kubernetes()
]


for i in resecres:
    i.deploy()
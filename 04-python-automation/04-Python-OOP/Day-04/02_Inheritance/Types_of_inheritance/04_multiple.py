class Linux:

    def linux_command(self):
        print("Linux command")


class AWS:

    def aws_command(self):
        print("AWS command")


class DevOpsEngineer(Linux, AWS):

    def deploy(self):
        print("Deploying application")


devops = DevOpsEngineer()

devops.linux_command()
devops.aws_command()
devops.deploy()
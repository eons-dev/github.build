import logging
import ebbs

class github(ebbs.Builder):
    def __init__(this, name="github"):
        super().__init__(name)

        this.supportedProjectTypes = []

        this.requiredKWArgs.append('pat')

    def Build(this):
        this.Login()

    def Login(this):
        this.RunCommand(f"echo {this.kwArgs['pat']} | gh auth login --with-token")
        code, user = this.RunCommand("gh api user", saveout=True)
        logging.info(f"Logged in as: {user['login']}")
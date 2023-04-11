import logging
import ebbs
import subprocess
import json

class github(ebbs.Builder):
    def __init__(this, name="github"):
        super().__init__(name)

        this.supportedProjectTypes = []

        this.requiredKWArgs.append('pat')

    def Build(this):
        this.Login()

    def Login(this):
        this.RunCommand(f"echo '{this.pat}' | gh auth login --with-token")
        code, user = this.RunCommand("gh api user", saveout=True)
        user = f"{user[0]}}}" #output correction, I guess.
        logging.info(f"Logged in as: {json.loads(user)['login']}")

    def GetRepos(this, org):
        # NOTE: this.RunCommand apparently doesn't capture all the repos. There seems to be a race condition in when gh actually returns and when subprocess thinks it returns.
        result = subprocess.run(["gh", "repo" ,"list", org, "--json", "name", "--limit", "200"], stdout=subprocess.PIPE)
        repos = json.loads(result.stdout.decode("utf-8"))
        repos = [f"{org}/{repo['name']}" for repo in repos]
        return repos
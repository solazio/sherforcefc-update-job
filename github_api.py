import requests
import base64
import os
from datetime import datetime


class GitHubCommit:
    """
    Update a specific file in your Github repo using the API.
    """

    def __init__(self):
        self.api_url = "https://api.github.com"
        self.access_token = os.environ.get()("GITHUB_TOKEN")
        self.today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.update_file()

    def update_file(self):
        if self.access_token:
            headers = {"Authorization": f"token {self.access_token}"}
        else:
            headers = {}

        try:
            with open("info.md", "rb") as f:
                # Encode file content to base64
                content = base64.b64encode(f.read())
            f.close()
        except Exception:
            content = None
            print("The file 'info.md' has no content!")

        if content:
            try:
                requests.put(
                    f"{self.api_url}/repos/solazio/sherforcefc.co.uk/contents/"
                    "src/pages/index.md",
                    headers=headers,
                    params={},
                    json={
                        "branch": "master",
                        "message": f"UpdateBot - {self.today}",
                        "content": content,
                        "sha": "de583194428973323a668faa0aec68e03c7c4064",
                    },
                )
            except Exception as e:
                print(e)

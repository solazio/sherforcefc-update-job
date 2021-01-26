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
        self.access_token = os.environ.get("GITHUB_TOKEN")
        self.today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.get_file_sha()
        self.update_file()

    def get_file_sha(self):
        try:
            with open("file_sha.txt", "r") as f:
                self.file_sha = f.read().rstrip("\n")
            f.close()
        except Exception:
            self.file_sha = None
            print("The file 'file_sha.txt' has no content!")

    def update_file_sha(self):
        try:
            with open("file_sha.txt", "w") as f:
                f.write(self.file_sha)
            f.close()
        except Exception:
            self.file_sha = None
            print("Something went wrong while updating 'file_sha.txt'!")

    def update_file(self):
        if self.access_token:
            headers = {
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"token {self.access_token}",
            }
        else:
            headers = {}

        try:
            with open("info.md", "rb") as f:
                # Encode file content to base64
                file_content = f.read()
                content = base64.b64encode(file_content).decode("utf-8")
            f.close()
        except Exception:
            content = None
            print("The file 'info.md' has no content!")

        if content:
            try:
                resp = requests.put(
                    f"{self.api_url}/repos/solazio/sherforcefc.co.uk/"
                    "contents/src/pages/index.md",
                    headers=headers,
                    params={},
                    json={
                        "branch": "master",
                        "message": f"UpdateBot - {self.today}",
                        "content": content,
                        "sha": self.file_sha,
                    },
                )

                print(resp.json())
                self.file_sha = resp.json()["content"]["sha"]
                self.update_file_sha()
            except Exception as e:
                print(e)

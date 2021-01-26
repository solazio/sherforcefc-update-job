## This is codebase for the cron job responsible to update https://github.com/solazio/sherforcefc.co.uk repository every week with the latest data from the FA website

To get the file SHA do:
1. A request to https://api.github.com/repos/solazio/sherforcefc.co.uk/git/ref/heads/master [note the branch is master in this case]
curl -H "Authorization: token <GITHUB_TOKEN>" https://api.github.com/repos/solazio/sherforcefc.co.uk/git/ref/heads/master
2. A request to the commit url from the response you get in step 1
3. Do recursive requests to the tree url you got in step 2


Docs for GitHub API: https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#contents


Alternative on how to commit a file:
https://docs.github.com/en/free-pro-team@latest/rest/guides/getting-started-with-the-git-database-api
http://www.levibotelho.com/development/commit-a-file-with-the-github-api/


To run it locally add the following lines to github_api.py
```
from dotenv import load_dotenv

load_dotenv()
```

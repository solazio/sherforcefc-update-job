import os

from github_api import GitHubCommit
from get_website_data import GetWebsiteData
from apscheduler.schedulers.blocking import BlockingScheduler


def update_website():
    GetWebsiteData()
    GitHubCommit()


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_executor("processpool")
    scheduler.add_job(update_website, "cron", day_of_week=6, hour=20)
    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

update_website()

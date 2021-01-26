import urllib.request
from bs4 import BeautifulSoup


class GetWebsiteData:
    """
    Get the table data from an FA url
    """

    def __init__(self):
        self.URL = "https://fulltime-league.thefa.com/ProcessPublicSelect.do?psSelectedSeason=997972047&psSelectedDivision=193785606&psSelectedCompetition=0&psSelectedLeague=2113065"
        self.write_data_to_file()

    def fetch_data(self):
        source = urllib.request.urlopen(self.URL).read()
        soup = BeautifulSoup(source, "html.parser")
        tables = soup.find_all("table")

        return tables

    def write_data_to_file(self):
        my_file = open("info.md", "w")
        tables = self.fetch_data()
        table_rows = tables[0].find_all("tr")
        my_file.write(
            "---\ntemplateKey: index-page\ntitle: Sher Force Football"
            " Club\nteams:\n"
        )
        j = 0
        for tr in table_rows:
            if j < len(table_rows) - 1:
                i = 0
                for td in tr.find_all("td"):
                    if i == 1:
                        my_file.write(
                            "  - name: {text}\n".format(
                                text=td.get_text().replace("\n", " ").strip()
                            )
                        )
                    elif i == 2:
                        my_file.write(
                            "    played: {text}\n".format(
                                text=td.get_text().replace("\n", " ").strip()
                            )
                        )
                    elif i == 3:
                        my_file.write(
                            "    won: {text}\n".format(
                                text=td.get_text().replace("\n", " ").strip()
                            )
                        )
                    elif i == 4:
                        my_file.write(
                            "    drawn: {text}\n".format(
                                text=td.get_text().replace("\n", " ").strip()
                            )
                        )
                    elif i == 5:
                        my_file.write(
                            "    lost: {text}\n".format(
                                text=td.get_text().replace("\n", " ").strip()
                            )
                        )
                    elif i == 6:
                        my_file.write(
                            "    gd: {text}\n".format(
                                text=td.get_text().replace("\n", " ").strip()
                            )
                        )
                    elif i == 7:
                        my_file.write(
                            "    points: {text}\n".format(
                                text=td.get_text().replace("\n", " ").strip()
                            )
                        )
                    i = i + 1
            j = j + 1

        my_file.write("---\n")
        my_file.close()

        return

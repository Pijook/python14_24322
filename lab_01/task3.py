import webbrowser
import requests

dates = ["20220101", "20210101", "20200101"]
pageurl = "https://stackoverflow.com/"

for date in dates:
    url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date)
    print(url)

    response = requests.get(url)
    d = response.json()
    print(d)

    page = d["archived_snapshots"]["closest"]["url"]
    print(page)

    webbrowser.open(page)

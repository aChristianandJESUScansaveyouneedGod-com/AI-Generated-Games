import requests

def download_asset(url, path):

    r = requests.get(url)

    with open(path,"wb") as f:
        f.write(r.content)

    print("Asset downloaded:", path)

#команда парисинга
#snscrape --max-result 10 --jsonl telegram-channel python2day > txt.txt
import json
from bs4 import BeautifulSoup
import requests
inp = open("txt.txt")
inp = inp.readlines()
for i in inp:
    j = json.loads(i)
    url = j["url"]
    u = url.split("https://t.me/s/python2day/")
    src = BeautifulSoup(requests.get(f"https://t.me/s/python2day/{u[1]}").text)
    b = src.find(attrs={"data-post" : f"python2day/{u[1]}"}).find_all("b")
    for t in b:
        print(t.text)
    print()
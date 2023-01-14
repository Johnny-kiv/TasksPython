#команда парисинга
#snscrape --max-result 10 --jsonl telegram-channel python2day > txt.txt
import json
import subprocess
from bs4 import BeautifulSoup
import requests
ip = input()
subprocess.run("pip install snscrape",shell=True)
subprocess.run(f"snscrape --max-result 10 --jsonl telegram-channel {ip} > txt.txt",shell=True)
inp = open("txt.txt")
inp = inp.readlines()
for i in inp:
    jsn = json.loads(i)
    url = jsn["url"]
    datapost = url.split("/")[-1]
    src = BeautifulSoup(requests.get(url).text)
    print("################")
    statey = src.find(attrs={"data-post" : f"{ip}/{datapost}"})
    for j in str(statey).split("<br>"):
        print(j)

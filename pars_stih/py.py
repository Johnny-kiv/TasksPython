import requests
from bs4 import BeautifulSoup
i = open("input.txt")
urls = i.read().split("\n")
l=000
for u in urls:
    l+=1
    o = open(f"stih_00{l}.txt", "w")
    src=requests.get(u).text
    soup=BeautifulSoup(src)
    poema = soup.find("section",class_="content").find_all("p")
    aftor = soup.find("section",class_="content").find(class_="tema-stih")
    name = soup.find("section",class_="content").find("h1")
    o.write("\t"+"\t"+"\t"+name.text)
    o.write(aftor.text)
    for p in poema:
        o.write(p.text+"\n")


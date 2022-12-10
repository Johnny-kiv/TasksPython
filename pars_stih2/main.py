"""import requests
import sqlite3
from bs4 import BeautifulSoup

conn = sqlite3.connect('stixes.db')
cur = conn.cursor()

url = "https://stihibase.ru/author/"
src = BeautifulSoup(requests.get(url).text)
authors = src.find_all("li",class_="alfavit-stixi-title")
for aut in authors:
    print(aut.text.strip())
    a = aut.find("a").get("href")
    stixes = BeautifulSoup(requests.get("https://stihibase.ru"+a).text)
    items=stixes.find_all("li",class_="alfavit-stixi-title")
    l=0
    for i in items:
        l+=1
        if l!=340:
            z=i.find("a").get("href")
            o = open(f"/home/user/stixes/stih_{a.split('/')[3]}_{l}.txt", "w")
            s = BeautifulSoup(requests.get(F"https://stihibase.ru{z}").text)
            poema = s.find("section",class_="content").find_all("p")
            aftor = s.find("section",class_="content").find(class_="tema-stih")
            name = s.find("section",class_="content").find("h1")
            o.write("\t"+"\t"+"\t"+name.text)
            o.write(aftor.text)
            o.write("\n")
            for p in poema:
                o.write(p.text+"\n")
            insertQuery = f'''INSERT INTO
                        Stixes  (id, author, name, file_name)
                        VALUES ({l}, '{aftor.text.split("   ")[4]}','{name.text}','stih_{a.split('/')[3]}_{l}');'''
            cur.execute(insertQuery)
            conn.commit()
conn.close()"""
from bs4 import BeautifulSoup
import requests
url = requests.get("https://stihibase.ru/author/").content
rest = BeautifulSoup(url)
authors = rest.find_all("li",class_="alfavit-stixi-title")
for i in authors:
    try:
        print("https://stihibase.ru"+i.find("a").get("href"))
    except:
        pass

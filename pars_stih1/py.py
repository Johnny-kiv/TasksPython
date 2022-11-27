#################################
#Задача:
#Необходимо написать программу, которая будет считывать файл с ссылками в каждой строке. далее программа должна получить по каждой ссылки чистый текст стихотворения. Каждый стих должен быть в отдельном файле, причем первой строкой должно идти наименование стихотворения, второй строкой автор, третья строка  - это пустая строка,  четвертая строка - начинается стихотворение. Название выходных файлов должно идти так: stih_00001.txt, stih_00002.txt, stih_00003.txt и т.д.
#Пример входного файла: input.txt
#Пример выходного файла: stih_00001.txt
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
    o.write("\n")
    for p in poema:
        o.write(p.text+"\n")


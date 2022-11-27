import requests
from bs4 import BeautifulSoup
url1 = 'https://stihibase.ru/author/f/fet/mama_gljan_ka_iz_okoshka/'
url2 = 'https://stihibase.ru/author/b/barto/snegir/'
url3 = 'https://stihibase.ru/author/a/ancharov/oduvanchiki/'
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
bs1 = BeautifulSoup(response1.text,"lxml")
bs2 = BeautifulSoup(response2.text,"lxml")
bs3 = BeautifulSoup(response3.text,"lxml")
autor1 = bs1.find('a', 'link-details')
autor2 = bs2.find('a', 'link-details')
autor3 = bs3.find('a', 'link-details')
nazvanie_1_stiha = bs1.find('header','head-content-poema').find_all('h1')
nazvanie_2_stiha = bs2.find('header','head-content-poema').find_all('h1')
nazvanie_3_stiha = bs3.find('header','head-content-poema').find_all('h1')
stih1 = bs1.find('article', 'block-poema').find_all('p')
stih2 = bs2.find('article', 'block-poema').find_all('p')
stih3 = bs3.find('article', 'block-poema').find_all('p')
res1 = '\n'.join(x.text for x in nazvanie_1_stiha)
res_1 = '\n'.join(x.text for x in stih1)
res2 = '\n'.join(x.text for x in nazvanie_2_stiha)
res_2 = '\n'.join(x.text for x in stih2)
res3 = '\n'.join(x.text for x in nazvanie_3_stiha)
res_3 = '\n'.join(x.text for x in stih3)
lines1 = [res1, autor1.text, '', res_1]
lines2 = [res2, autor2.text, '', res_2]
lines3 = [res3, autor3.text, '', res_3]
f = open('текст первого стиха.txt', 'w')
for line in lines1:
    f.write(line + '\n')
f.close()
f = open('текст второго стиха.txt','w')
for line in lines2:
    f.write(line + '\n')
f.close()
f = open('текст третьего стиха.txt','w')
for line in lines3:
    f.write(line + '\n')
f.close()


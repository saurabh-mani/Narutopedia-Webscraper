import requests
import bs4
import os

search_key = input("Enter Search Key: ").replace(" ","_")
res = requests.get("https://naruto.fandom.com/wiki/"+search_key)

soup = bs4.BeautifulSoup(res.text,"lxml")

paras = soup("p")

for  i in paras:
    if(i.text == "" or i.text == '\n' or str(i).find("caption")!=-1):
        continue
    os.system("clear")
    print(i.text)
    input("Press Enter to continue and Ctrl+C to exit")

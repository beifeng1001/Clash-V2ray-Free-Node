#第二个

import requests
import time
import os
from bs4 import BeautifulSoup

main_url = "https://clashnode.com/wp-content/uploads/"

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
html = requests.get(main_url,headers=UA)
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,"html.parser")
out = soup.find_all("span",class_="truncate")

# print(soup)


month = str(time.strftime("%m"))
day = int(time.strftime("%d"))
year = str(time.strftime("%Y"))

day = day - 1

# print(times,day,month,year)

url = main_url + year + "/" + month + "/" + str(time.strftime("%Y%m%d")) +".txt"

print(f"当前最新url是本月{day}号：{url}")
with open('./url.txt', 'wt') as f:
    print(url, file=f)
# 能帮助你就是我的快乐qwp
# 目标：aweikeji 订阅

import requests
import time
import os
from bs4 import BeautifulSoup

def quit():
    print(f"当前最新url是本月{updata_url_c}号：{file_url}")
    # 写入txt中
    with open('./url.txt', 'wt') as f:
        print(file_url, file=f)

# v2 cl ；此处更改clash还是v2ray

software = "cl" #Clash
url="https://agit.ai/213321sad/youtube-aweikeji/src/branch/master"
# 添加UA标识
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
try:
    html=requests.get(url,headers=headers)
except:
    print("无法链接到agit，可能是网络问题")
    exit()

html.encoding = "utf-8"
soup = BeautifulSoup(html.text,"html.parser")
out = soup.find_all("span",class_="truncate")
txt = str(out).split("</span>")[0].split("""" title""")[0].split("""href="/""")[1]

txt = txt.replace("src","raw")
url = "https://agit.ai/" + txt

# 获取时间
times = str(time.strftime("%Y%m%d")).split("23")[1]
month = times[0:2]
day = times[2:4]

# 换算时间格式
if int(month) < 10:
    month = month.split("0")[1]
if int(day) < 10:
    day = day.split("0")[1]

if str(software) == "v2":
    extension = ".txt"
elif str(software) == "cl":
    extension = ".yaml"
else:
    print("Error")
    exit()

file_url = url + "/" + month + "." + day + software + extension

# 循环查找最近更新内容（5次）
find = 0
while find < 5:
    html=requests.get(file_url,headers=headers)
    html.encoding = "utf-8"
    soup = BeautifulSoup(html.text,"html.parser")
    out = soup.find_all("h2")
    # 截断str
    try:
        txt = str(out).split("<h2>")[1].split("</h2>")[0]
    except:
        quit()

    if str(txt) == "Error 404":
        updata_url_a = url + "/" + month + "."
        updata_url_b = software + extension
        updata_url_c = int(day) - 1
        file_url = updata_url_a + str(updata_url_c) + updata_url_b
        print("获取失败,重试中")
        find = find + 1

print("正在尝试方案二")

file_url = url + "/" + month + "." + day + software
find_b = 0

while find_b < 5:
    html=requests.get(file_url,headers=headers)
    html.encoding = "utf-8"
    soup = BeautifulSoup(html.text,"html.parser")
    out = soup.find_all("h2")
    try:
        txt = str(out).split("<h2>")[1].split("</h2>")[0]
    except:
        quit()

    if str(txt) == "Error 404":
        updata_url_a = url + "/" + month + "."
        updata_url_b = software
        updata_url_c = int(day) - 1
        file_url = updata_url_a + str(updata_url_c) + updata_url_b
        print("获取失败,重试中")
        find_b = find_b + 1



print("获取失败，可能脚本已失效，或者作者停止更新超过最近五天")
exit()
# -*- coding:UTF-8 -*-

# noinspection PyUnresolvedReferences
from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    #要爬的目标网站
        target = 'http://www.biqukan.com/1_1094/5403177.html'
        req = requests.get(url=target)
    #将爬取的网站信息进行解析
    #使用find_all方法，获得html信息中所有class属性为showtxt的div标签。
        html = req.text
        bf = BeautifulSoup(html,"lxml")
        texts = bf.find_all('div', id="content" , class_ = "showtxt")
        print(texts)
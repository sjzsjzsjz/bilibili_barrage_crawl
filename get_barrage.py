# coding:utf8

'''
随意打开b站一个视频https://www.bilibili.com/video/av34238679
打开开发者工具发现弹幕就在list.so?oid=4564645这里面
网址为：https://api.bilibili.com/x/v1/dm/list.so?oid=59976715
作者：房东的猫emmm
'''

from pyquery import PyQuery as pq
import requests


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        response.encoding = "utf8"
    except Exception as e:
        print(repr(e))
        return
    else:
        return response.content


def parse_web_data(web_data):
    doc = pq(web_data)
    lis = doc("d")
    content = list()
    for i in lis.items():
        content.append(i.text())
    return content


def write_file(file, content):
    with open(file, "w", encoding="utf8")as f:
        for i in content:
            f.write(i + "\n")


if __name__ == '__main__':
    url = "https://api.bilibili.com/x/v1/dm/list.so?oid=59976715"
    web_data = get_html(url)
    if web_data is None:
        print("爬取错误")
        exit()
    content = parse_web_data(web_data)
    write_file("barrage.txt", content)

# coding:utf8
import requests
from lxml import etree
import json

def getOnePage(page):
    url = f'http://maoyan.com/board/{page*10}'
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/70.0.3538.67 Safari/537.36'}
    r = requests.get(url, headers=header)
    return r.text

def parse(text):
    #规范化  标准化
    html = etree.HTML(text)
    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    print(names)
    releasetimes = html.xpath('//p[@class="releasettime"]/@text()')
    for names, releasetimes in zip(names, releasetimes):
        item = {}
        item[names] = names
        item[releasetimes] = releasetimes
        yield item

def save2File(data):
    with open('moven.json', 'a', encoding='utf-8')as f:
        data = json.dumps(data, ensure_ascii=float)+ ',/n'
        f.write(data)

text = getOnePage(4)

items = parse(text)

for item in items:
    save2File(item)
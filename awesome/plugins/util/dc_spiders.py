import requests
import re
from lxml import etree

'''
 news_spiders:社区爬虫
 @Author:Skyzc
 @description:抓取[DrinkCoffee](http://bbs.skyzc.top/)社区最新5个帖子
 
'''

URL = 'http://bbs.skyzc.top/'

def get_lastitem():
    try:
        lastitem = []
        data = requests.get(URL)
        # print(data.text)

        item = re.findall(r'<li><a .*>(.*?)</a></li>',data.text)
        html = etree.HTML(data.text)
        item = html.xpath('//li/a/text()')
        for i in item:
            lastitem.append(i.replace('\n','').replace(' ',''))

        return lastitem
    except requests.exceptions.ConnectionError as e:
        # 链接错误
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)
        pass
    except:
        pass

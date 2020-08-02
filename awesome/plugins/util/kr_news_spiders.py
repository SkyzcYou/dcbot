import requests
import re
import json
from lxml import etree

'''
 36Kr_news_spiders:36Kr快讯爬虫
 @Author:Skyzc
 @description:抓取[36Kr快讯](https://36kr.com/newsflashes)新闻快讯 20条

'''

URL = 'https://36kr.com/newsflashes'


def get_newsflashes():
    try:
        newsflashes = []
        data = requests.get(URL)


        data_text = re.findall(r'<script>window.initialState=(.*?)<',data.text)
        str_data = "".join(data_text)
        json_data = json.loads(str_data)
        item_list = json_data['newsflashCatalogData']['data']['newsflashList']['data']['itemList']
        for item in item_list:
            # print(item['templateMaterial']['widgetTitle'])
            newsflashes.append(item['templateMaterial']['widgetTitle'])
        return newsflashes
    except requests.exceptions.ConnectionError as e:
        # 链接错误
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)
        pass
    except:
        pass

print(get_newsflashes())

import requests
import re

'''
 news_spiders:新闻爬虫
 @Author:Skyzc
 @description:抓取[环球网](https://www.huanqiu.com/)新闻
'''


# 获取科技新闻
def get_tech_news():
    # 环球网-科技 新闻API
    URL = 'https://tech.huanqiu.com/api/list?node=%22/e3pmh164r/e3pmh2hq8%22,%22/e3pmh164r/e3pmh33i9%22,%22/e3pmh164r/e3pmh356p%22,%22/e3pmh164r/e3pmh3dh4%22,%22/e3pmh164r/e3pmtlao3%22,%22/e3pmh164r/e3pmtm015%22,%22/e3pmh164r/e3pmtnh4j%22,%22/e3pmh164r/e3pn1fd3s%22,%22/e3pmh164r/e3pn46ri0%22,%22/e3pmh164r/e3pn4bn46%22,%22/e3pmh164r/e3pn4gh77%22,%22/e3pmh164r/e3pn4qlss%22,%22/e3pmh164r/e3pn6fo08%22,%22/e3pmh164r/e3ptqlvrg%22&offset=0&limit=20'

    try:
        tech_news = []
        # tech_response = requests.get('https://tech.huanqiu.com/')
        # tech_response.encoding = 'utf-8'
        #
        # print(tech_response.url)  # URL
        # print(tech_response.elapsed)  # 访问时间
        # print(tech_response.status_code)  # 状态码
        # print(tech_response.text)  # 文本内容
        #
        # new = re.findall(r'<div class="con-txt"><h4>(.*?)</h4>' , tech_response.text)
        # print(new)
        data = requests.get(URL)
        # print(data.json()['list'])

        for item in data.json()['list']:
            if 'title' in item:     # 该数据末尾有个空{},此处需要验证一下
                tech_news.append(item['title'])
        # print(tech_news)
        return tech_news
    except requests.exceptions.ConnectionError as e:
        # 链接错误
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)
        pass
    except:
        pass
get_tech_news()
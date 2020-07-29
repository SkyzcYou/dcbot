import requests
import re

'''
 news_spiders:新闻爬虫
 @Author:Skyzc
 @description:抓取[环球网](https://www.huanqiu.com/)新闻
'''

# 获取新闻
def get_news(URL):
    try:
        mil_news = []
        data = requests.get(URL)

        for item in data.json()['list']:
            if 'title' in item:     # 该数据末尾有个空{},此处需要验证一下
                mil_news.append(item['title'])
        print(mil_news)
        return mil_news
    except requests.exceptions.ConnectionError as e:
        # 链接错误
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)
        pass
    except:
        pass


# 此方法已作废
# 获取科技新闻
def get_tech_news():

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
        data = requests.get('URL')
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


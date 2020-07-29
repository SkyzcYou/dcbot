import re,json
import nonebot
import pytz
import datetime,feedparser,time,os

from nonebot import on_command,CommandSession
from apscheduler.schedulers.blocking import BlockingScheduler
from aiocqhttp.exceptions import Error as CQHttpError

'''
DC_RSS BOT
@Author: Skyzc
两种方式获取RSS
'''

# RSS地址
RSS_URL = "http://bbs.skyzc.top/atom"
LATEST_UPDATED = 0

# 命令任务
@on_command('dc_rss',aliases=('论坛动态'),only_to_me=False)
async def dc_rss_send(session:CommandSession):
    print(os.getcwd())
    message = rss_parse()
    push_message = \
    "> DC社区新帖/新回复\n" \
    + "\nTITLE： " + message['entries_title'] \
    + "\nSUMMARY： " + message['entries_summary'] + '...' \
    + "\n\nBY: " + message['entries_author']\
    + "\n" + message['entries_link']
    await session.send(push_message)

# 计划任务。每天 8-20点 每10分钟 执行一次
@nonebot.scheduler.scheduled_job('cron', hour='8-23',minute='0/10')
async def _():
    message = rss_parse()
    push_message = \
        "> DC社区新帖/新回复\n" \
        + "\nTITLE： " + message['entries_title'] \
        + "\nSUMMARY： " + message['entries_summary'] + '...' \
        + "\n\nBY: " + message['entries_author'] \
        + "\n" + message['entries_link']
    now_updated = message['entries_updated']
    bot = nonebot.get_bot()
    # 读取 json 文件信息 判断是否有更新
    data = get_data()
    old_updated = data['entries_updated']

    try:
        if now_updated != old_updated:
            # await bot.send_group_msg(group_id=762186255, message=push_message)
            await bot.send_group_msg(group_id=1134452485,message=push_message)
            # 存储数据
            save_file(message)
        else:
            print('论坛暂无更新...')
    except CQHttpError:
        pass


# 解析 RSS 数据,返回一个 dict
def rss_parse():
    # 解析所有信息得到一个字典
    all_info = feedparser.parse(RSS_URL)
    # print(all_info)
    # 将我们所需要的信息加入字典
    latest_info = {}

    latest_info['feed_title'] = all_info.feed.title   # 订阅的信息流名称 [DrinkCoffee]
    latest_info['feed_subtitle'] = all_info.feed.subtitle   # 订阅的信息流类型名称 [新回帖、新帖]
    # latest_info['last_modified'] = str(utc_format(all_info.headers['Last-Modified']))

    latest_info['entries_title'] = all_info.entries[0].title        # 文章标题
    latest_info['entries_author'] = all_info.entries[0].author      # 作者/回复人昵称

    entries_summary = all_info.entries[0].summary    # 摘要处理，利用正则去除符号
    dr = re.compile(r'<[^>]+>', re.S)
    entries_summary = dr.sub('', entries_summary)
    latest_info['entries_summary'] = entries_summary[0:20]

    latest_info['entries_updated'] = str(utc_format(all_info.entries[0].updated))    # 更新时间,(格式化为本地时间字符串)
    latest_info['entries_link'] = all_info.entries[0].link          # 链接

    # print(latest_info)


    for key in latest_info:
        print(key + ":" + latest_info[key])

    return latest_info


# UTC 时间转为本地时间
def utc_format(utc):
    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"
    utcTime = datetime.datetime.strptime(utc, UTC_FORMAT)
    localtime = utcTime + datetime.timedelta(hours=8)
    return localtime

# 每次获取到新的帖子，就把信息存入json文件
def save_file(item):
    # 先将字典对象转化为可写入文本的字符串
    item = json.dumps(item)
    path = './awesome/plugins/pl_config/dc_rss.json'   #
    try:
        with open(path, "w", encoding='utf-8') as f:
            f.write(item + "\n")
            f.close()
            print("^_^ write success")

    except Exception as e:
        print("write error==>", e)

# 获取 json 文件数据
# TODO:日报功能
def get_data():
    path = './awesome/plugins/pl_config/dc_rss.json'
    data = 0
    try:
        with open(path, "r", encoding='utf-8') as f:
            data = json.load(f)
            print("^_^ read success")
            f.close()
    except Exception as e:
        print("read error==>", e)

    return data









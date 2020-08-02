from datetime import datetime

import nonebot
import pytz

from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command, CommandSession

from awesome.plugins.pl_config import global_qqnumber
from awesome.plugins.util import news_spiders
from awesome.plugins.util import dc_spiders
from awesome.plugins.util.huanqiu_news_api import *


'''
 每日早安&晚安时间
 @Author:Skyzc
'''
week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }

# TODO: 早安心语/每日早报
# 计划任务：MorningTime 每天8点,推送早报
@nonebot.scheduler.scheduled_job('cron', hour='8')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    tech_news = news_spiders.get_news(TECH_URL)

    push_message = \
        "> DrinkCoffee-MorningTime\n" \
        + f"NOW：{now.year}-{now.month}-{now.day} {week_day_dict[now.weekday()]} {now.hour}:{now.minute}" \
        + "\n今日科技早报" \
        + "\n1. " + tech_news[0] \
        + "\n2. " + tech_news[1] \
        + "\n3. " + tech_news[2] \
        + "\n4. " + tech_news[3] \
        + "\n5. " + tech_news[4] \
        + "\n详情：http://t.cn/AiRcD2jq"

    try:
        await bot.send_group_msg(group_id=global_qqnumber.RSS_TEST,
                                 message=push_message)
        await bot.send_group_msg(group_id=global_qqnumber.DC_CS,
                                 message=push_message)
    except CQHttpError:
        pass


# 命令任务：手动获取新闻
@on_command('tech_news', aliases=('科技新闻'), only_to_me=False)
async def send_tech_news(session: CommandSession):
    tech_news = news_spiders.get_news(TECH_URL)
    now = datetime.now(pytz.timezone('Asia/Shanghai'))


    push_message = \
        "> DC_小菲为你送上当前科技新闻\n" \
        + f"NOW：{now.year}-{now.month}-{now.day} {week_day_dict[now.weekday()]} {now.hour}:{now.minute}" \
        + "\n1. " + tech_news[0] \
        + "\n2. " + tech_news[1] \
        + "\n3. " + tech_news[2] \
        + "\n4. " + tech_news[3] \
        + "\n5. " + tech_news[4] \
        + "\n详情：http://t.cn/AiRcD2jq"  # 环球时报科技区短链接，若使用长链接在QQ消息里会变成卡片 短链接转换：https://www.helingqi.com/url.php 使用新浪的t.cn

    await session.send(push_message)


# TODO：每日热帖推送
# NightTime 每天23点
@nonebot.scheduler.scheduled_job('cron', hour='23')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    last_item = dc_spiders.get_lastitem()

    push_message = \
        "> DrinkCoffee-NightTime\n" \
        + f"NOW：{now.year}-{now.month}-{now.day} {week_day_dict[now.weekday()]} {now.hour}:{now.minute}" \
        + "\n为你送上今日社区热帖：" \
        + "\n1. " + last_item[1] \
        + "\n2. " + last_item[2] \
        + "\n3. " + last_item[3] \
        + "\n4. " + last_item[4] \
        + "\n5. " + last_item[5]
    try:
        await bot.send_group_msg(group_id=global_qqnumber.RSS_TEST,
                                 message=push_message)
        await bot.send_group_msg(group_id=global_qqnumber.DC_CS,
                                 message=push_message)
    except CQHttpError:
        pass

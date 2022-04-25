# dcbot
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1/badge)](https://bestpractices.coreinfrastructure.org/projects/1)

**由于Coolq机器人已死亡,此项目主要功能已失效. 2020.10.1 注**

一个服务于DC社区QQ群机器人，实现众多实用性功能。

基于 [酷Q](https://cqp.cc/t/23253) , [CQHTTP](https://cqhttp.cc/docs/4.15/#/) 以及 [NoneBot](https://nonebot.cqp.moe/) 。


## 一、所实现的功能：
1. [DrinkCoffee](http://bbs.skyzc.top)社区RSS推送
2. 每日早报/新闻
## 二、@TODO
帮你百度Bot

## 三、项目结构
```
|-- undefined
    |-- config.py                       # 项目配置文件
    |-- README.md
    |-- requirements.txt                # 依赖文件
    |-- run.py                          # 主程序
    |-- awesome
    |   |-- plugins                     # 插件目录
    |       |-- dc_mnnews.py
    |       |-- dc_rss.py
    |       |-- weather.py
    |       |-- dev_fold                # 其他文件目录(开发工程中的一些不重要的文件，例如代码示例等)
    |       |   |-- data.json
    |       |   |-- myjob.py
    |       |-- pl_config               # 插件配置文件
    |       |   |-- dc_rss.json
    |       |-- util                    # 工具包
    |       |   |-- news_spiders.py
```

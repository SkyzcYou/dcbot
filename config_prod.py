from nonebot.default_config import *
import re

# 开发环境：

HOST = '0.0.0.0'                              # 运行地址
PORT = 5656                                     # 运行端口
SUPERUSERS = {1404725663}                       # 管理员QQ
COMMAND_START = ['', re.compile(r'[/!]+')]      # 配置命令的起始字符
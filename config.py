from nonebot.default_config import *
import re

HOST = '127.0.0.1'                              # 运行地址
PORT = 8080                                     # 运行端口
SUPERUSERS = {1404725663}                       # 管理员QQ
COMMAND_START = ['', re.compile(r'[/!]+')]      # 配置命令的起始字符
"""
Copyright 2021-2021 The TZIOT Authors. All rights reserved.
日志包.可打印实时日志
Authors: jdh99 <jdh821@163.com>
lagan取名来自于宜家的水龙头"拉根"
"""

import utime

# 日志级别
LEVEL_OFF = 0
LEVEL_DEBUG = 1
LEVEL_INFO = 2
LEVEL_WARN = 3
LEVEL_ERROR = 4

_level_ch = {LEVEL_OFF: 'O', LEVEL_DEBUG: 'D', LEVEL_INFO: 'I', LEVEL_WARN: 'W', LEVEL_ERROR: 'E'}

# 日志颜色
# 30 黑色 31 红色 32 绿色 33 黄色 34 蓝色 35 紫红色 36 青蓝色 37 白色
_level_color = {LEVEL_OFF: 30, LEVEL_DEBUG: 37, LEVEL_INFO: 36, LEVEL_WARN: 35, LEVEL_ERROR: 31}

_is_pause = False
_filter_level = LEVEL_WARN
_is_color = False


def set_filter_level(level: int):
    """设置日志级别"""
    global _filter_level
    _filter_level = level


def enable_color(enable: bool):
    """使能日志带颜色输出"""
    global _is_color
    _is_color = enable


def get_filter_level() -> int:
    """显示日志级别"""
    return _filter_level


def println(tag: str, level: int, msg: str, *args):
    """日志打印"""
    if _is_pause or _filter_level == LEVEL_OFF or level < _filter_level:
        return

    content = _level_ch[level] + '/' + tag + ': ' + (msg % args)
    if _is_color:
        content = '\033[7;' + '%d;' % _level_color[level] + '40m' + content + '\033[0m'
    _print(level, content)


def _print(level, msg):
    t = utime.time()
    hour = int(t / 3600)
    t -= hour * 3600
    minute = int(t / 60)
    second = t - minute * 60
    timestamp = '%02d:%02d:%02d - ' % (hour, minute, second)

    if _is_color:
        print('\033[7;' + '%d;' % _level_color[level] + '40m' + timestamp + '\033[0m' + msg)
    else:
        print(timestamp + msg)


def print_hex(tag: str, level: int, data: bytearray):
    """打印16进制字节流"""
    if _is_pause or _filter_level == LEVEL_OFF or level < _filter_level:
        return

    s = '\n****'
    for i in range(16):
        s += '%02x ' % i
    s += '\n---- : '
    for i in range(16):
        s += '-- '

    data_len = len(data)
    for i in range(data_len):
        if i % 16 == 0:
            s += '\n%04x : ' % i
        s += '%02x ' % data[i]

    prefix = '%c/%s' % (_level_ch[level], tag)
    new_format = prefix + ': '

    if _is_color:
        content = '\033[7;' + '%d;' % _level_color[level] + '40m' + new_format + '\033[0m' + s
    else:
        content = new_format + s
    _print(level, content)


def pause():
    """暂停日志打印"""
    global _is_pause
    _is_pause = True


def resume():
    """恢复日志打印"""
    global _is_pause
    _is_pause = False


def is_pause() -> bool:
    """是否暂停日志打印"""
    return _is_pause


def debug(tag: str, msg: str, *args):
    """打印debug信息"""
    println(tag, LEVEL_DEBUG, msg, *args)


def info(tag: str, msg: str, *args):
    """打印info信息"""
    println(tag, LEVEL_INFO, msg, *args)


def warn(tag: str, msg: str, *args):
    """打印warn信息"""
    println(tag, LEVEL_WARN, msg, *args)


def err(tag: str, msg: str, *args):
    """打印error信息"""
    println(tag, LEVEL_ERROR, msg, *args)

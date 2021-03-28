# micropython-lagan

## 介绍
基于micropython语言的日志库.

lagan取名来自于宜家的水龙头"拉根"。

本软件包已上传到pypi，可输入命令直接安装。
```shell
pip install micropython-lagan
```

## 功能
- 支持日志在终端实时打印
- 支持二进制流打印

与python标准版lagan相比，micropython版本的lagan删除了输出到日志文件，以及带颜色的日志打印等功能。

error打印函数名改为err，原因使用error函数名在设备运行会报错。

## 示例
```python
# 默认输出界别是info,本行不会打印
lagan.debug("case4", "debug test print")

lagan.info("case4", "info test print")
lagan.warn("case4", "warn test print")
lagan.err("case4", "error test print")
```

输出：
````
186172:12:16 -  I/case4: info test print
186172:12:16 -  W/case4: warn test print
186172:12:16 -  E/case4: error test print
````
注意：时间戳是基于设备本地时钟，不是标准时间。

## 二进制流打印
```python
s = bytearray()
for i in range(100):
    s.append(i)
lagan.print_hex('case2', lagan.LEVEL_ERROR, s)
```

输出：
````
186172:11:40 -  E/case2: 
****00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 
---- : -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
0000 : 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 
0010 : 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 
0020 : 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 
0030 : 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f 
0040 : 40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 
0050 : 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f 
0060 : 60 61 62 63 
````

#### ip 地址地理位置信息查询
查询来源：http://ip.taobao.com/instructions.php

##### 依赖库
- requests

##### 使用说明

- 从文件读数据  ./ip_query.py -f /path/ip.txt
- 从管道读取数据  cat /var/log/ip.log | python ip_query.py
- 从命令行参数读取数据  ./ip_query.py -a '192.168.1.191'


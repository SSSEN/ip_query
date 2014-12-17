ip 地址对应的地区查询，调用的是淘宝的接口
http://ip.taobao.com/instructions.php

- 从文件读数据  ./ip_query.py -f /path/ip.txt
- 从管道读取数据  cat /var/log/ip.log | python ip_query.py
- 从命令行参数读取数据  ./ip_query.py -a '192.168.1.191'

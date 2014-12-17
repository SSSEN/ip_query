#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
    调用 淘宝 ip  restful api 进行查询，
    支持直接指定 ip 地址查询 ，
    也支持读取文件按行解析查询地址
    同时支持从管道读取数据进行查询
"""
import requests
import argparse
import sys

URL = "http://ip.taobao.com/service/getIpInfo.php?ip="

def query_ip_info(ip):
    if not ip:
        print 'argument shoud not be none'
        return
    url = URL + str(ip)
    try:
        r = requests.get(url, timeout=5)
    except Exception as e:
        print e
    else:
        data = r.json()
        if data['code'] == 0:
            data = data['data']
            print ip, data['country'], "/", data['area'], "/", data['region'], "/", data['city'], "/", data['isp']
        else:
            print "查询失败: ", ip, data['data']

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--addr", help="输入单个 ip 地址进行查询")
    parser.add_argument("-f", "--file", help="输入文件路径，从文件中按行进行解析读取数据")
    parser.add_argument("-p", "--pipe", default=sys.stdin, const=sys.stdin, nargs="?", help="从管道中读取数据")

    args = parser.parse_args()

    if not any((args.addr, args.file, args.pipe)):
        parser.print_usage()
        sys.exit()

    elif args.addr:
        return ("addr", args.addr)
    elif args.file:
        return ("file", args.file)
    else:
        return ("pipe", sys.stdin)

def run():
    source, ips = parse_args()

    if source == "pipe":
        for ip in sys.stdin:
            query_ip_info(ip.strip())

    elif source == "addr":
        query_ip_info(ips)

    elif source == "file":
        try:
            with open(ips, "r") as f:
                while True:
                    ip = f.readline().strip()
                    if not ip:
                        break
                    query_ip_info(ip)
        except Exception as e:
            print e
    else:
        print "unknown error"

def test():
    run()

if __name__ == "__main__":
    test()

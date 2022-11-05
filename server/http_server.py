#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
#import pymongo
from http.server import BaseHTTPRequestHandler, HTTPServer
#from BaseHTTPServer import BaseHTTPRequestHandler
from http.server import HTTPServer, SimpleHTTPRequestHandler, test as test_orig
import logging
import time
import requests
import urllib3
urllib3.disable_warnings()
import base64
from data_analysis import *

data = {'status': 'success'}


class S(BaseHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)


    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(type(post_data),post_data[0:5])

        d1=post_data[5:len(post_data)]  #去掉code=
        
        #print(base64.b64decode(d1))
        d_data=base64.b64decode(d1) #base64 解密
        str1= d_data.decode("utf-8") #转成字符串
        raw_data = json.loads(str1) #字符串转json

        #提取主机头
        #print(raw_data)
        domain=raw_data.get("global").get("domain")
        origin='https://'+str(domain)
        referer='https://'+str(domain)
        
        #构建Referer 头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': origin,
            'Referer': referer
        }
        t_3s_list=list()
        try:
            #print(json1.get('data').get('t_3s_html_load'))
            print("获取原始数据")
            #print(raw_data.get("data").get("t_3s_html_load"))
            raw_data.get("data").get("t_3s_html_load")[0].get("fmp")
            #j_raw_data=json.dumps(raw_data)
            #print(j_raw_data)

            t_3s_load_data=t_3s_fun(raw_data)  #重构3s数据
            t_3s_list.append(t_3s_load_data) 
            #print(raw_data_.get('data').get('t_3s_html_load')[0],type(raw_data.get('data').get('t_3s_html_load')[0]))

            print("进行w外部数据重构")
            new_data=restruct_data(raw_data,t_3s_list) #重构外部数据
            #print(new_data)
            
            print("base64加密")
            e_data=encode_data(new_data)
            #print(e_data)
            
            str2=e_data.decode("utf-8") #转成字符串
            result="code="+str2
            print("加密字符串")
            print(result)
            res = requests.post('https://3s.sreanalyze.com/api/v1/stats/collect', headers=headers, data=result, verify=False)
            print(res.json())

            
        except:
            print("忽略非3s数据")


def run(server_class=HTTPServer, handler_class=S, port=8888):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

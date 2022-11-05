#import requests
import urllib3
import time
import hashlib
import random
import json
import base64
#urllib3.disable_warnings()

t_3s_list=list()


def t_3s_fun(rawdata):

    t_3s_data={"time":rawdata.get("data").get("t_3s_html_load")[0].get("time"),
        "redirect":rawdata.get("data").get("t_3s_html_load")[0].get("redirect"),
        "fetchstart":rawdata.get("data").get("t_3s_html_load")[0].get("fetchstart"),
        "dns":rawdata.get("data").get("t_3s_html_load")[0].get("dns"),
        "tcp":rawdata.get("data").get("t_3s_html_load")[0].get("tcp"),
        "ttfb":rawdata.get("data").get("t_3s_html_load")[0].get("ttfb"),
        "download":rawdata.get("data").get("t_3s_html_load")[0].get("download"),
        "processing":rawdata.get("data").get("t_3s_html_load")[0].get("processing"),
        "load":rawdata.get("data").get("t_3s_html_load")[0].get("load"),
        "domcontentloaded":rawdata.get("data").get("t_3s_html_load")[0].get("domcontentloaded"),
        "onload":rawdata.get("data").get("t_3s_html_load")[0].get("onload"),
        "firstscreen":rawdata.get("data").get("t_3s_html_load")[0].get("firstscreen"),
        "size":rawdata.get("data").get("t_3s_html_load")[0].get("size"),
        "pingcdn":rawdata.get("data").get("t_3s_html_load")[0].get("pingcdn"),
        #"fmp":rawdata.get("data").get("t_3s_html_load")[0].get("fmp"),
        "fmp":random.randint(1100,1500),
        "jsloadtime":rawdata.get("data").get("t_3s_html_load")[0].get("jsloadtime"),
        "fcp":rawdata.get("data").get("t_3s_html_load")[0].get("fcp"),
         }
    print("3s_数据构造完成")
    return t_3s_data


#t_3s_list.append(t_3s_load_data)

def restruct_data(rawdata,t_3s):
    new_data={"db":rawdata.get("db"),
        "global":rawdata.get("global"),
        "data":{"t_3s_html_ajax":rawdata.get("data").get("t_3s_html_ajax"),
               "t_3s_html_error":rawdata.get("data").get("t_3s_html_error"),
               "t_3s_html_info":rawdata.get("data").get("t_3s_html_info"),
               #"t_3s_html_load":t_3s_html_load},
               "t_3s_html_load":t_3s},
               "time":rawdata.get("time") }
    return new_data

def encode_data(d1):
    print("进入数据编码")
    #print(type(d1))
    tmp_json = json.dumps(d1)
    print(tmp_json)
    tmp_str = str(tmp_json)
   # print("tmp_str",tmp_str)
    e_data=base64.b64encode(tmp_str.encode("utf-8")) #base64加密
    return e_data
    # b4=base64.b64encode(j2)


#t1=t_3s_fun(rawdata)
#print(t1)
#t_3s_list.append(t1)
#t2=restruct_data(rawdata,t_3s_list)
#print(t2)

#new_data=restruct_data(rawdata)

#result=encode_data(new_data)


# -*- coding:utf-8 -*-
import re
import requests
import os
def find_project():
    url:str = input('请输入作品链接:')
    # 分析作品源码链接
    resp = requests.post(url)
    title = re.findall('<title>(.*?)</title>',resp.text)
    title = title[0]
    meta_name = re.findall('<meta name="description" content="(.*?)/>',resp.text,re.S)
    # 分析作品标题
    project_json_url = re.findall('\//steam.nosdn.127.net/(.*?).json',resp.text)
    project_json_url = project_json_url[0]
    num = len(project_json_url)
    project_json_url = project_json_url[num-32:num]
    project_json_url = 'http://steam.nosdn.127.net/'+project_json_url+'.json'
    # 匹配json源码链接
    project_json = requests.get(project_json_url)
    json = project_json.text
    # json源码
    title = str(title)
    with open(title+'.json','w',encoding='utf-8') as f:
            f.write(json)
            # 生成json文件
    filename = title+'.json'
    newname = title + ".sb3"
    os.rename(filename, newname)
    input('已生成'+newname+'文件，回车以关闭程序')
if __name__ == '__main__':
    find_project()

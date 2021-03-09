import os
import requests
from bs4 import BeautifulSoup
import csv
import sys
import time
import json
import re
from fake_useragent import UserAgent

xiaoqu_head = ['name', 'build_year', 'desc_href', '90_day_href', 'rend_href', 'district', 'bizcircle','建筑类型','物业费用','物业公司','开发商','楼栋总数','房屋总数','附近门店']

districts_all=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]
districts=["changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan"]
for district in districts:
    csv_r_name=district+"_all.csv"
    csv_w_name=district+"_detail.csv"
    # read from csv
    with open(csv_r_name, 'r', encoding='utf-8')as f:
        district_lst = list(csv.reader(f))
    f.close

    #print(district_lst)
    district_detail_lst=[]
    i = 1
    for xiaoqu in district_lst:
        url=xiaoqu[2]
        print("--------"+district+", "+str(i)+", "+xiaoqu[0]+":\t "+url)
        '''
        headers = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',},
            {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',},
            {'User-Agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',},
            ]
        '''
        #生成随机UA
        ua = UserAgent()
        hd=ua.random
        #print(type(hd.find("iPad")))
        #print(hd.find("iPad"))
        while ((hd.find("iPad")>=0) or (hd.find("Android")>=0)):
            print("while:"+hd)
            hd=ua.random
        headers={'User-Agent': hd}
        print(headers)
        r=requests.get(url=url, headers=headers)
        r.encoding='utf-8'
        content=r.text
        soup=BeautifulSoup(content, features="html.parser")
        xqinfo_lst=soup.find('div', class_='xiaoquInfo')
        for info in xqinfo_lst.find_all('span', class_='xiaoquInfoContent'):
            xqif_cnt = re.sub(r'栋$', "", info.text.strip())
            xqif_cnt = re.sub(r'户$', "", xqif_cnt)
            xqif_cnt = re.sub(r'元/平米/月$', "", xqif_cnt)
            xiaoqu.append(xqif_cnt)
        #print(xiaoqu)        
        district_detail_lst.append(xiaoqu)
        #print(district_detail_lst)
        i=i+1
        #time.sleep(1)
        # write to csv
        if i==100:
            with open(csv_w_name,'a+', newline='', encoding='utf-8') as f:
                f_csv = csv.writer(f)
                #f_csv.writerow(xiaoqu_head)
                f_csv.writerows(district_detail_lst)
            f.close()
            print("wirte district_detail_lst to file OK")
            i = 1
            district_detail_lst=[]
    with open(csv_w_name,'a+', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        #f_csv.writerow(xiaoqu_head)
        f_csv.writerows(district_detail_lst)
    f.close() 

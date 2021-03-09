# Use Python3
import os
from bs4 import BeautifulSoup
import requests
import csv
import sys
import time
import json
#reload(sys)
#sys.setdefaultencoding('utf-8')

districts=["baoshan", "changning", "chongming", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "qingpu", "songjiang", "xuhui", "yangpu"]

for district in districts:
    url='https://sh.ke.com/xiaoqu/'+district+'/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',}
    xiaoqu_head = ['name', 'build_year', 'desc_href', '90_day_href', 'rend_href', 'district', 'bizcircle']
    r=requests.get(url=url, headers=headers)
    r.encoding='utf-8'
    content=r.text
    district_lst = []
    soup=BeautifulSoup(content, features="html.parser")
    for divs in soup.find_all('div', class_='info'):
        xiaoqu = []
        dv_pst=divs.find('div', class_='positionInfo')
        dv_tt=divs.find('div', class_='title')
        dv_hi=divs.find('div', class_='houseInfo')
        for aa in dv_tt.find_all('a'):
            xiaoqu.append(aa.attrs['title'])
            xiaoqu.append(dv_pst.prettify()[-15:-11])
            xiaoqu.append(aa.attrs['href'])
        for aa in dv_hi.find_all('a'):
            xiaoqu.append(aa.attrs['href'])
        for aa in dv_pst.find_all('a'):
            xiaoqu.append(aa.attrs['title'][0:-2])
        district_lst.append(xiaoqu)
    #print(district_lst)
    print('---------------'+url+"---------------")
    print('---------------'+district+"---------------")
    # write to csv
    csv_name=district+"_all.csv"
    with open(csv_name,'a+', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        #f_csv.writerow(xiaoqu_head)
        f_csv.writerows(district_lst)
    f.close()
    pgs_lst=soup.find('div', class_='house-lst-page-box')
    pgs_info=json.loads(pgs_lst.attrs['page-data'])
    for i in range(2, pgs_info['totalPage']+1):
        district_lst=[]
        urls=url+'pg'+str(i)+'/'
        r=requests.get(url=urls, headers=headers)
        r.encoding='utf-8'
        content=r.text
        soup=BeautifulSoup(content, features="html.parser")
        print(urls)
        for divs in soup.find_all('div', class_='info'):
            xiaoqu = []
            dv_pst=divs.find('div', class_='positionInfo')
            dv_tt=divs.find('div', class_='title')
            dv_hi=divs.find('div', class_='houseInfo')
            for aa in dv_tt.find_all('a'):
                xiaoqu.append(aa.attrs['title'])
                xiaoqu.append(dv_pst.prettify()[-15:-11])
                xiaoqu.append(aa.attrs['href'])
            for aa in dv_hi.find_all('a'):
                xiaoqu.append(aa.attrs['href'])
            for aa in dv_pst.find_all('a'):
                xiaoqu.append(aa.attrs['title'][0:-2])
            district_lst.append(xiaoqu)
        #print(district_lst)
        print('---------------'+urls+"---------------")
        print('---------------'+district+"---------------")
        # write to csv
        csv_name=district+"_all.csv"
        with open(csv_name,'a+', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)
            #f_csv.writerow(xiaoqu_head)
            f_csv.writerows(district_lst)
        f.close()
        time.sleep(1)
print('--------------- DONE ---------------')
#print(soup.prettify())
#print(soup.title)
#print(soup.head)


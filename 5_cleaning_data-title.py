import csv
import os
import time

xiaoqu_title = ['名字', '建筑年代', '详情链接', '销售历史链接', '租房链接', '区', '街道','建筑类型','物业费用','物业公司','开发商','楼栋总数','房屋总数','附近门店']

districts_all=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]
districts=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]



for district in districts:
    csv_w_name=district+"-title.csv"
    csv_r_name=district+".csv"
    # read from csv
    with open(csv_r_name, 'r', encoding='utf-8')as f:
        district_lst = list(csv.reader(f))
    f.close
    district_lst.insert(0,xiaoqu_title)
    print("!!!!!! Done for "+district)
    time.sleep(2)
    with open(csv_w_name,'a+', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(district_lst)
    f.close() 

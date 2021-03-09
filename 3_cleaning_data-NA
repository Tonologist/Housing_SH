import csv
import os
import time


districts_all=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]
districts=["jiading",]


for district in districts:
    csv_w_name=district+".csv"
    csv_r_name=district+"_detail.csv"
    # read from csv
    with open(csv_r_name, 'r', encoding='utf-8')as f:
        district_lst = list(csv.reader(f))
    f.close

    district_detail_lst=[]
    for xiaoqu in district_lst:
        if (xiaoqu[3]).find("chengjiao")<0:
            xiaoqu.insert(3,"NA")
        if (xiaoqu[4]).find("zufang")<0:
            xiaoqu.insert(4,"NA")
        if (xiaoqu[1]).find("未知")>=0:
            xiaoqu[1]="NA"
        if (xiaoqu[7]).find("未知类型")>=0:
            xiaoqu[7]="NA"
        if (xiaoqu[8]).find("暂无信息")>=0:
            xiaoqu[8]="NA"
        if (xiaoqu[9]).find("暂无信息")>=0:
            xiaoqu[9]="NA"
        if (xiaoqu[10]).find("暂无信息")>=0:
            xiaoqu[10]="NA"
        #if (xiaoqu[13] and (xiaoqu[13]).find("暂无门店信息")>=0):
        #    xiaoqu[13]="NA"
        district_detail_lst.append(xiaoqu)
    print("!!!!!! Done for "+district)
    time.sleep(5)
    with open(csv_w_name,'a+', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        #f_csv.writerow(xiaoqu_head)
        f_csv.writerows(district_detail_lst)
    f.close() 

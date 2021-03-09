import csv
import os
import time


districts_all=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]


districts=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]

for district in districts:
    csv_w_name=district+".csv"
    csv_r_name=district+"_detail.csv"
    # read from csv
    with open(csv_w_name, 'r', encoding='utf-8')as f:
        district_lst = list(csv.reader(f))
    f.close

    district_detail_lst=[]
    print("!!!!!! for "+district)
    for xiaoqu in district_lst:
        #print(len(xiaoqu))
        if (len(xiaoqu)!=14):
            print(xiaoqu)

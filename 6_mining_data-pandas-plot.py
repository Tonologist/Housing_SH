import csv
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from scipy import stats


districts_all=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]
#districts=["jiading",]
districts=["chongming", "qingpu", "baoshan", "changning", "fengxian", "hongkou", "huangpu", "jiading", "jingan", "jinshan", "minhang", "pudong", "putuo", "songjiang", "xuhui", "yangpu"]
'''
title=['建筑年代','sum']
with open('group_sum_by_year.csv','a+', newline='', encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(title)
f.close()
'''
for district in districts:
    csv_w_name="dist_"+district+"_sum.csv"
    csv_r_name=district+"-title.csv"
    # read from csv
    data = pd.read_csv(csv_r_name)
    ''' 
    print("------------ data:")
    print(data)
    print("------------ data[0:3]:")
    print(data[0:3])
    print("------------ data.head:")
    print(data.head())
    print("------------ data.tail:")
    print(data.tail())
    #print("------------ data.drop:")
    #print(data.drop('附近门店', axis=1))
    print("------------ data type:")
    print(type(data))
    print("------------ data dtype:")
    print(data.dtypes)
    print("------------ data loc:")
    print(data.loc[:, ['year','房屋总数']])
    '''
    grouped=data.groupby("建筑年代")
    summary=grouped['房屋总数'].agg([np.sum])
    summary.to_csv(csv_w_name,index=True,mode='a', header=True,sep=',')
    data = pd.read_csv(csv_w_name)
    data.plot(x="建筑年代",y='sum', color ='b',  marker = 'o', legend = False)
    plt.title(district+' build house')
    plt.xlabel('Year', fontsize=10)
    plt.ylabel('house amount')
    plt.savefig(district+'_build_house_by_year.jpg')
    #plt.show()
    print("------------ done: "+district)
#print("!!!!!!! done: all dist")
#summary.to_csv("all_dist_group_sum_by_year.csv",index=True,mode='a', header=False,sep=',')

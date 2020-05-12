#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 15:11 
# @Author : qingping.niu
# @File : ddd.py 
# @Desc :
import csv
import pandas as pd
import xlrd

def readExcel(row):
    '''
    :param row: 该参数表示行
    :return:
    '''
    book = xlrd.open_workbook('sina.xlsx','r')
    table = book.sheet_by_index(0)
    # print(table)
    return table.row_values(row)

if __name__ == '__main__':
    ss = readExcel(1)
    print(ss[2])

    # df = pd.read_csv('test.csv')
    # list_label = df.columns.values
    # print(list_label)
    # rows = []
    # with open('test.csv')as f:
    #     reader = csv.reader(f)
    #     next(reader, None)
    #     for iter in reader:
    #         print(iter)
    #         rows.append(iter)
    # print(''.join(rows[0][0]).decode('gb2312'))
    # rows = []
    # with open('test.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     next(reader,None)
    #     for i in reader:
    #         print(i)
    #         rows.append(i)
    #
    #         print(''.join(rows[0][]))



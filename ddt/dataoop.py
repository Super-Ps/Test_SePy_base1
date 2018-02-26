#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2018/2/7


import xlrd

#
# data =xlrd.open_workbook("D:\\git\\Test_SePy_base1\\ddt\\dataoop_t1.xlsx")
#
# table = data.sheet_by_name('Sheet1')
#
# nrows = table.nrows
# print("总行数： %s" % nrows)
# ncols = table.ncols
# print("总列数： %s" % ncols)
#
# print(table.row_values(1))
#
# print(table.col_values(0))


class ExcelDate(object):

    def __init__(self,exclepath,sheetname):
        '''  获取对象，数据表，行数，列数 '''

        self.excelobj = xlrd.open_workbook(exclepath)
        self.table_data = self.excelobj.sheet_by_name(sheetname)
        self.keys = self.table_data.row_values(0)
        self.nrows = self.table_data.nrows
        print("self.nrows",self.nrows)
        self.nclos = self.table_data.ncols

    def getexceldata(self):
        ''' 获取第一行作为key的值，遍历其他行列对应value'''
        if self.nrows<=1:
            print("总行数小于1条")
        else:
            r=[]
            j = 1

            for i in range(self.nrows-1):
                #print("self.nrows-1",self.nrows-1)
                #print("i=",i)

                s = {}

                rows_values=self.table_data.row_values(j)

                for x in range(self.nclos):
                    #print("x",x)
                    #print("rows_values[j]=%s"%rows_values[j])
                    s[self.keys[x]] = rows_values[x]
                   # print("result_data[self.nrows[j]]=%s" %result_data[self.keys[j]])
                r.append(s)
                j += 1

            return r


if __name__ == "__main__":
    exclepath = "D:\\git\\Test_SePy_base1\\ddt\\dataoop_t1.xlsx"
    sheetname = 'Sheet1'

    data = ExcelDate(exclepath, sheetname)
    #print(data.getexceldata())
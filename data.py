# -*- coding: utf-8 -*-
import xlrd
import xlwt
import sys
from xlutils.copy import copy
L = []
M = []
N = []
K = []
W = []
a = 0
data = xlrd.open_workbook('data.xlsx')
for i in range(4):
    table = data.sheets()[i]
    nrows = table.nrows
    ncols = table.ncols
    for j in range(nrows):
        for k in range(1):
            aa = table.row_values(j)[k]
            L.append(aa)

            # print M
M = list(set(L))
#
for q in range(len(M)):
    for z in range(4):
        table = data.sheets()[z]
        nrows = table.nrows
        ncols = table.ncols
        for j in range(nrows):
            for k in range(2):
                aa = table.row_values(j)[k]
                if (aa == M[q]):
                    N.append(aa)
                    N.append(data.sheets()[z].row_values(j)[k + 1])
                    # print aa
                    # print data.sheets()[z].row_values(j)[k + 1]
# dic = dict(zip(N[::2],N[1::2]))
# print dic
# for i in dic:
#         print "dic[%s]=" % i,dic[i]
# for i in M:
#     for key in dic:
#         sum = dic[i]
#         a = a+sum
        # print i
        # print a
file = xlwt.Workbook()
tablesheet = file.add_sheet('111')
for x in range(len(N)):
    # print x
    # print x%2
    # sys.exit()
    tablesheet.write(x/2,x%2,N[x])
file.save('demo.xls')
data = xlrd.open_workbook('demo.xls')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
init = table.row_values(0)[0]
for i in range(nrows):
    aa = table.row_values(i)[0]
    if (aa != init):
        # print i
        K.append(i)
        init = table.row_values(i)[0]
a = 0
sum = 0
for i in K:
    for b in range(a,i):
        print b
        index = table.row_values(b)[1]
        print index
        sum = sum+index
    print sum
    W.append(sum)
    sum = 0
    a = i
W.append(35055)
file1 = xlwt.Workbook()
tablesheet1 = file1.add_sheet('1111')
# print (len(M))
# print (len(W))
for x in range(len(M)):
    # print x
    # print x%2
    # sys.exit()
    tablesheet1.write(x,1,W[x])
    tablesheet1.write(x,0,M[x])
file1.save('final.xls')
#!/usr/local/python/bin
# -*- coding: utf-8 -*-

import xlrd
import xlwt
from xlutils.copy import copy

data = xlrd.open_workbook('sperate.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
L = []
T = []
W = []
J = []
K = []
H = []
M = []
C = []
D = []
aa = table.row_values(0)[0]

for i in range(nrows):
    val = table.row_values(i)
    if val[0] != aa:
        aa = val[0]
        # print(i)
        T.append(i)
        continue
    if val[1] == 1.0:
        L.append(int(val[5]))
# print(len(T))
# print(sum(L))

for x in T:
    for y in range(x):
        if table.row_values(y)[1] == 1.0:
            num = int(table.row_values(y)[5])
            W.append(num)
    # print(len(W))
    # print(sum(W))
    J.append(sum(W))
    W = []
# print(J)

aaa = 0
for z in range(len(J)):
    num = J[z]-aaa
    aaa = J[z]
    K.append(num)
# print(K)
# print(T)

bb = 0
for q in range(len(T)):
    num = T[q] - bb
    bb = T[q]
    H.append(num)
# print(H)
#
# print(len(H))
# print(len(K))
for i in range(len(K)):
    for a in range(H[i]):
        M.append(K[i])
# print(H)
# print(nrows)
# print(len(M))
# for i in range(M):
wp = copy(data)
sheet = wp.get_sheet(0)
for i in range(len(M)):
    sheet.write(i,6,M[i])
wp.save('sperate.xls')
for i in range(len(M)):
    small = table.row_values(i)[5]
    C.append(small)
    # sheet.write(i, 7, C[i]/M[i])
# wp.save('sperate.xls')
# print(M)
# print(C)
for i in range(len(M)):
    a = C[i]/M[i]
    b = '%.2f%%' %(a*100)
    sheet.write(i,7,b)
wp.save('sperate.xls')
newData=xlwt.Workbook("newData.xls")
for i in T:
    # print(i)
    # print(table.row_values(i - 1)[0])
    D.append(table.row_values(i - 1)[0])
# for i in range(len(D)):
#     print(D[i])

tdata = xlrd.open_workbook('sperate.xls')
tsheet = tdata.sheets()[0]
index = 0
for x in range(len(T)):
    print(x)
    print(T[x])
    print(D[x])
    sheetname = newData.add_sheet(D[x])
    for z in range(index,T[x]):
        for g in range(8):
            copy = tsheet.row_values(z)[g]
            sheetname.write(z - index,g,copy)
    index = T[x]
    print(index)
newData.save("newData.xls")












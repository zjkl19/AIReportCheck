# -*- coding: utf-8 -*-
"""
Created on 2019/05/25

@author: lindinan
"""

#TODO:
#仪器有旧编号的要使用旧编号
#方案要有人员
#ReportError等添加修改建议

import os

import docx
import AIReportCheck


import win32com
from win32com.client import Dispatch

docName='hyl.docx'

#导入库
wordApp = win32com.client.Dispatch('Word.Application')
#调用word程序
wordApp.Visible = 0
wordApp.DisplayAlerts = 0
#不在前台显示文档及错误，在实际使用阶段可以全部关闭，提高运行速度，但是在调试时打开还是用处挺大的，可以对操作是否实现自己的需求进行直观的判断，比如说我们选中的内容是否已经高亮等等。
doc = wordApp.Documents.Open(u''+os.getcwd()+'\\'+docName)

try:
    document = docx.Document(docName)  #打开文件
except e:
    print(e.message)

r=AIReportCheck.AIReportCheck(document)
r.CheckReport()


doc.Close()
wordApp.Quit()

for e in r.ErrorList:
    print(e.Name)


#tables = document.tables #获取文件中的表格集
#table = tables[0]#获取文件中的第一个表格
#result=""
#for i in range(0,len(table.rows)):#从表格第二行开始循环读取表格数据
#    result = table.cell(i,j).text# + "" +table.cell(i,1).text+table.cell(i,2).text + table.cell(i,3).text
#    #cell(i,0)表示第(i+1)行第1列数据，以此类推
#    print(result)

#totalText=result+mainBody
#import re
#ret = re.findall(r'(Km/h)',totalText)
#if len(ret) > 0:
#   print("速度单位疑似存在错误")

#for i in range(0,len(document.paragraphs)):   
    #print(document.paragraphs[i].text)




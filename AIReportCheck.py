# -*- coding: utf-8 -*-

import ReportError
import re    #正则表达式

import enum


class InspType(enum.Enum):
    """
    检验类型
    """
    RegularPeriod=1
    StructurePeriod=2
    Loadtest = 3    #荷载试验
    

class AIReportCheck(object):
    """
    mocking a person to check report

    """

    def __init__(self,document):      
        self.document=document
        self.__InitVar()
        self.ErrorList=[]
    
    def __InitVar(self):
        """初始化变量
        
        """
        #TODO：处理找不到的情况
        #查找概况信息表格
        tables = self.document.tables
        for i in range(0,len(tables)):
            if tables[i].cell(0,0).text.find('委托单位')>=0:
                self.OverviewTable=tables[i]
                break
        
        self.BridgeName=self.OverviewTable.cell(2,2).text         

    def CheckReport(self):
        """校核报告
        
        """
     
        #errorFound=self.__FindUnitError(self.document.Range.text)
        #if len(errorFound)>0:
        #    e=ReportError.ReportError(1,"计量单位错误","使用了错误的计量单位","第"+str(i+1)+"段"+','.join(errorFound))
        #    self.ErrorList.append(e)
        for i in range(0,len(self.document.paragraphs)):
            errorFound=self.__FindUnitError(self.document.paragraphs[i].text)
            if len(errorFound)>0:
                e=ReportError.ReportError(1,"计量单位错误","使用了错误的计量单位","第"+str(i+1)+"段"+','.join(errorFound))
                self.ErrorList.append(e)
        flag=0
        for i in range(0,len(self.document.paragraphs)):
            ret=self.__FindNotExplainNoError(self.document.paragraphs[i].text)
            if len(ret)>0:
                flag=1
                break
        if flag==0:
            e=ReportError.ReportError(2,"未写构件编号说明","需要描写构件编号说明","请补充构件编号说明")
            self.ErrorList.append(e)        

    def __FindUnitError(self,text):
        """在正文中查找单位错误
        
        len(ret)
        ret[0].text
        """
        ret = re.findall(r'([0-9]Km/h)',text)
        return ret

    def __FindNotExplainNoError(self,text):
        """在正文中查找未写构件编号错误
        
        """
        ret = re.findall(r'(构件编号说明)',text)
        return ret

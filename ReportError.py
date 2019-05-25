# -*- coding: utf-8 -*-
class ReportError(object):
    """
    description of error in a report

    """

    def __init__(self,No,Name,Description,Position):      
        self.No=No
        self.Name=Name
        self.Description=Description
        self.Position=Position

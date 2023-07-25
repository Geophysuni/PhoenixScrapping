# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:12:14 2023

@author: Sergey Zhuravlev
"""

import os
import pandas as pd
import numpy as np

class pScrapp:
    def __init__(self, diriectory):
        # set main directory of search
        self.srcDict = diriectory
        # create dataframe
        self.data = pd.DataFrame(columns = ['file'])
        
    def findFiles(self, substr):
        # substr is a substring that is used to determine if file contains necessary data
        for path, subdirs, files in os.walk(self.srcDict):
            for name in files:
                try:
                    with open(os.path.join(path, name), 'r', encoding='utf8') as f:
                        tmp = f.read()
                    if tmp.find(substr)>0:
                        self.data.loc[len(self.data), 'file'] = os.path.join(path, name)
                except:
                    pass
                
    def scrapp(self, tag, substr, ending):
        # tag - short name of feature that you want to extract
        # sustr - substring that relates to the beginning of valuable data
        # ending - end symbol that always follows after valuable data
        self.data[tag] = np.nan            
        for i in range(len(self.data)):
            with open(self.data.loc[i, 'file'], 'r', encoding = 'utf8') as f:
                tmp = f.read()
            skip = len(substr)
            ind = tmp.find(substr)
            if ind>0:
                tmpVal = tmp[ind+skip:]
                for j, cv in enumerate(tmpVal):
                    if cv==ending:
                        break
                val = tmpVal[:j]
            else:
                val = 'empty'
            self.data.loc[i, tag] = val
        




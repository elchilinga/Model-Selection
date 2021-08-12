import numpy as np
import pandas as pd
import logging
import re
import sys
import os
from os import listdir
from os.path import isfile, join
#import argparse


class ModelSelection:
    def __init__(self, path):
        self.path = path
"""in readFile function reading .log files for needed path"""
    def readFile(self, dfLog, path):
        with open(path, 'r') as logFile:
            numRows = -1
            for line in logFile:
                tokens = line.split(' ')
                path = tokens[2]
                score = tokens[4]
                score = score.replace('\n', "")
                numRows += 1
                dfLog.loc[numRows] = [path, score]
        return dfLog

"""in logFile2DataFrame function from 4 .log files creating dataframe which includes the paths of videos and the IoU scores for each model """

    def logFile2DataFrame(self):
        self.logList = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        model1 = pd.DataFrame(columns=['Path', 'Model1'])
        model2 = pd.DataFrame(columns=['Path', 'Model2'])
        model3 = pd.DataFrame(columns=['Path', 'Model3'])
        release = pd.DataFrame(columns=['Path', 'Released'])
        for i in self.logList:
            if ".log" in i:
                path = self.path + i
                if "Released" in i:
                    release = self.readFile(release, path)
                elif "Model2" in i:
                    model2 = self.readFile(model2, path)
                elif "Model3" in i:
                    model3 = self.readFile(model3, path)
                elif "Model1" in i:
                    model1 = self.readFile(model1, path)
        df = pd.concat([release, model1, model2, model3], axis=1, join='inner')
        df = df.loc[:, ~df.columns.duplicated()]
        return df

"""in selectionDependingGender we can see mean, median, variance for each group which we want : man, woman, others (for comparing each other)"""

    def selectionDependingGender(self, args, dfLog):
        # args is array of path filter
        s = '|'.join(args)
        dfC = dfLog.loc[dfLog['Path'].str.contains(s, case=False)]

        dfr = pd.DataFrame(data=dfLog, columns=['Released'])
        df1 = pd.DataFrame(data=dfLog, columns=['Model1'])
        df2 = pd.DataFrame(data=dfLog, columns=['Model2'])
        df3 = pd.DataFrame(data=dfLog, columns=['Model3'])
        npData = np.array(pd.concat([dfr, df1, df2, df3], axis=1).astype(float))
        meanArr = np.mean(npData, axis=0)
        medianArr = np.median(npData, axis=0)
        varArr = np.var(npData, axis=0)
        return meanArr, medianArr, varArr


#path = 'C:/Users/chilinga/Desktop/krisp/'
path = "Please enter yout path"
obj = ModelSelection(path)
df = obj.logFile2DataFrame()
obj.selectionDependingGender(["man", "yout", "Serg"], df)
#obj.selectionDependingGender(["woman", "anush"], df)
#obj.selectionDependingGender(["M-", "real"], df)
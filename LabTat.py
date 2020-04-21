# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:05:13 2020

@author: Neeraj Kumar S J
"""
########################################importing the necassary modules########################################
import scipy
from scipy import stats
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#########################################Loading the data to a dataframe#######################################
labtat = pd.read_csv("E:\\Neeraj\\Exam and Careers\\DataScience\\Data Sets\\LabTAT.csv")
labtat.columns = "lab1" , "lab2" , "lab3", "lab4" #renaming the columns as per need.
labtat.describe()
#########################################Visualization and Editing of data#####################################
plt.hist(labtat['lab1'])
plt.boxplot(labtat['lab1'])
#labtat.iloc[66:0,0:1]=149.24
#To remove outliers, we shall assign upper outliers with highest quartile values and lower outliers with lowest quartile values.
labtat.loc[66,'lab1'] = labtat.loc[72,'lab1'] = labtat.loc[114,'lab1'] = labtat.loc[93,'lab1']
labtat.loc[48,'lab1'] = labtat.loc[84,'lab1']
plt.hist(labtat['lab1'])
plt.boxplot(labtat['lab1'])
#help(labtat.loc())
plt.hist(labtat['lab2'])
plt.boxplot(labtat['lab2'])
plt.hist(labtat['lab3'])
plt.boxplot(labtat['lab3'])
plt.hist(labtat['lab4'])
plt.boxplot(labtat['lab4'])
#To remove outliers, we shall assign upper outliers with highest quartile values and lower outliers with lowest quartile values.
labtat.loc[72,'lab4'] = labtat.loc[108,'lab4']
labtat.loc[109,'lab4'] = labtat.loc[32,'lab4']
plt.hist(labtat['lab4'])
plt.boxplot(labtat['lab4'])
########################################Normality test#########################################################
w = stats.shapiro(labtat.lab1)
P_value_lab1 = w[1]
t_stats_lab1 = w[0]
print(f'As P Value for Laboratory 1 or Sample Y1 :{P_value_lab1} is greater than 0.05, Hence Sample Y1 is normal')
x = stats.shapiro(labtat.lab2)
P_value_lab2 = x[1]
t_stats_lab2 = x[0]
print(f'As P Value for Laboratory 2 or Sample Y2 :{P_value_lab2} is greater than 0.05, Hence Sample Y2 is normal')
y = stats.shapiro(labtat.lab3)
P_value_lab3 = y[1]
t_stats_lab3 = y[0]
print(f'As P Value for Laboratory 3 or Sample Y3 :{P_value_lab3} is greater than 0.05, Hence Sample Y3 is normal')
z = stats.shapiro(labtat.lab4)
P_value_lab4 = z[1]
t_stats_lab4 = z[0]
print(f'As P Value for Laboratory 4 or Sample Y4 :{P_value_lab4} is greater than 0.05, Hence Sample Y4 is normal')
######################################Variance test##############################################################
scipy.stats.levene(labtat.lab1,labtat.lab2,labtat.lab3,labtat.lab4)
######################################On Way Anova Test########################
from statsmodels.formula.api import ols
mod = ols('lab1~lab2+lab3+lab4',data =  labtat).fit()
aov_table = sm.stats.anova_lm(mod, type=2)
print(aov_table)
######################################Printng the obained results################################################
u = aov_table.iloc[:1,4:]
print(f'As P Value for comparing lab1, lab2, lab3 & lab4 is :{u}, which is lesser than 0.05, Hence we can conclude Variances of Sample Y1, Y2, Y3 and Y4 are not same.\nHence Ho is acceptable. ')


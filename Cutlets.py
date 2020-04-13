# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:49:34 2020

@author: Neeraj Kumar S J
"""
########################################importing the necassary modules###############################################
import scipy
from scipy import stats
import statsmodels.api as sm
import pandas as pd
#######################################Importing the Cutlets.csv dataset #############################################
cutlet_size = pd.read_csv("E:\\Neeraj\\Exam and Careers\\DataScience\\Data Sets\\Cutlets.csv")
cutlet_size.columns = 'UnitA','UnitB' #Inordeer to rename the columns
#Normality Test.
x = stats.shapiro(cutlet_size.UnitA)
P_value_unitA = x[1]
t_stats_unitA = x[0]

y = stats.shapiro(cutlet_size.UnitB)
P_value_unitB = y[1]
t_stats_unitB = y[0]
print(f'As P Value for Unit A or Sample Y1 :{P_value_unitA} is greater than 0.05, Hence Sample Y1 is normal')
print(f'As P Value for Unit B or Sample Y1 :{P_value_unitB} is greater than 0.05, Hence Sample Y2 is normal')
#Variance Test
z = scipy.stats.levene(cutlet_size.UnitA,cutlet_size.UnitB)
print(f'As P Value for comparing Unit A or Sample Y1 and UnitB or Sample Y2 :{z[1]} is greater than 0.05, Hence we can conclude Variances of Sample Y1 and Y2 are same ')
#################################################Printng the obained results###############################################
t_test = scipy.stats.ttest_ind(cutlet_size.UnitA,cutlet_size.UnitB)
print(f'As P Value for t test on Unit A or Sample Y1 and UnitB or Sample Y2 :{t_test[1]} is greater than 0.05')


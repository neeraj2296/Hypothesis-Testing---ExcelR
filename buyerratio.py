# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:29:43 2020

@author: Neeraj Kumar S J
"""
########################################importing the necassary modules###############################################
import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm
#######################################Importing the BuyerRatio.csv dataset ##########################################
buyer=pd.read_csv('E:\\Neeraj\\Exam and Careers\\DataScience\\Data Sets\\BuyerRatio.csv')
buyer
Fbuyer = buyer.loc[0:2,['North','South','East','West']]
Fbuyer
#buyerdata=buyer.iloc[0:2, 1:4]
#help(buyer.iloc)
#################################################Applying Chi-Square Test#############################################
chisquare_out=scipy.stats.chi2_contingency(Fbuyer)
chisquare_out
#################################################Printng the obained results##########################################
Chi_square=[['','Test Statistic','p-value'],['Sample Data',chisquare_out[0],chisquare_out[1]]]
Chi_square

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:23:00 2020

@author: Admin
"""

import scipy
from scipy import stats
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fantaloons = pd.read_csv("E:\\Neeraj\\Exam and Careers\\DataScience\\Data Sets\\Faltoons.csv")
fantaloons

count1 = fantaloons['Weekdays'].value_counts()
count2 = fantaloons['Weekend'].values_counts()
count = {"Weekdays":count1,"Weekend":count2}
fanta = pd.DataFrame(count)

Chisquares_results=scipy.stats.chi2_contingency(fanta)

Chisquares = [['', 'Test statistics', 'p value'], ['sample', Chisquares_results[0], Chisquares_results[1]]]
u = Chisquares[1]
print(f'As P Value for comparing Weekdays & Weekend is :{u[2]}, which is lesser than 0.05.\nHence we conclude Ho has failed.')


# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:00:54 2020

@author: Admin
"""

########################################importing the necassary modules########
import scipy
from scipy import stats
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cust_ordform = cust_ord = pd.read_csv("E:\\Neeraj\\Exam and Careers\\DataScience\\Data Sets\\CostomerOrderForm.csv ")
cust_ord

cust_dummy = pd.get_dummies(cust_ord['Phillippines'])
cust_dummy.columns ='Def_Phil','Err_Phil'
cust_ordform = pd.concat((cust_ordform,cust_dummy),axis=1)
cust_ordform = cust_ordform.drop(['Phillippines','Def_Phil'],axis=1)

cust_dummy = pd.get_dummies(cust_ordform['Indonesia'])
cust_dummy.columns ='Def_Indo','Err_Indo'
cust_ordform = pd.concat((cust_ordform,cust_dummy),axis=1)
cust_ordform = cust_ordform.drop(['Indonesia','Def_Indo'],axis=1)

cust_dummy = pd.get_dummies(cust_ordform['Malta'])
cust_dummy.columns ='Def_Malta','Err_Malta'
cust_ordform = pd.concat((cust_ordform,cust_dummy),axis=1)
cust_ordform = cust_ordform.drop(['Malta','Def_Malta'],axis=1)

cust_dummy = pd.get_dummies(cust_ordform['India'])
cust_dummy.columns ='Def_Ind','Err_Ind'
cust_ordform = pd.concat((cust_ordform,cust_dummy),axis=1)
cust_ordform = cust_ordform.drop(['India','Def_Ind'],axis=1)

cust_ordform.columns = 'Phillippines','Indonesia','Malta','India'

count1=cust_ord["Phillippines"].value_counts()     #counting the value of Discrete Categorical Data(no error and defective)
count2=cust_ord["Indonesia"].value_counts()        #counting the value of Discrete Categorical Data(no error and defective)
count3=cust_ord["Malta"].value_counts()
count4=cust_ord["India"].value_counts()
count={"Phillipines":count1, "Indonesia":count2, "Malta":count3, "India":count4} #making dictionary of all counts
count_new=pd.DataFrame(count)

Chisquares_results=scipy.stats.chi2_contingency(count_new)
Chisquares_results

Chisquare=[['', 'Test statistics', 'p value'], ['sample', Chisquares_results[0], Chisquares_results[1]]]  
u = Chisquare[1]
print(f'As P Value for comparing Phillipines, Indonesia, Malta, India is :{u[2]}, which is greater than 0.05.\nHence we conclude Ho fails to accept.')

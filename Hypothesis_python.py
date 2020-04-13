import pandas as pd
import scipy 
from scipy import stats
import statsmodels.api as sm

#from plotly.tools import FigureFactory as FF

############2 sample T Test(Marketing Strategy) ##################

promotion=pd.read_csv("C:\\Users\\Vimod\\Downloads\\Promotion.csv")
promotion

##########Normality Test ############

print(stats.shapiro(promotion.InterestRateWaiver))    #Shapiro Test
print(stats.shapiro(promotion.StandardPromotion))
#################### Variance Test #############
scipy.stats.levene(promotion.InterestRateWaiver, promotion.StandardPromotion)

######## 2 Sample T test ################
scipy.stats.ttest_ind(promotion.InterestRateWaiver,promotion.StandardPromotion)

################Chi-Square Test ################

Bahaman=pd.read_csv("E:\\Neeraj\\Exam and Careers\\DataScience\\Data Sets\\Bahaman.csv")
Bahaman

count=pd.crosstab(Bahaman["Defective"],Bahaman["Country"])
count
Chisquares_results=scipy.stats.chi2_contingency(count)
Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]
#chisample_results=FF.create_table(Chi_square,index=True)

############# One - Way Anova ###################
from statsmodels.formula.api import ols
import pandas as pd
cof=pd.read_csv("C:\\Users\\Vimod\\Downloads\\ContractRenewal_Data.csv")
cof
cof.columns="SupplierA","SupplierB","SupplierC"

##########Normality Test ############

print(stats.shapiro(cof.SupplierA))    #Shapiro Test
print(stats.shapiro(cof.SupplierB))
print(stats.shapiro(cof.SupplierC))

############## Variance test #########
scipy.stats.levene(cof.SupplierA, cof.SupplierB)
scipy.stats.levene(cof.SupplierB, cof.SupplierC)
scipy.stats.levene(cof.SupplierC, cof.SupplierA)

############# One - Way Anova ###################

mod=ols('SupplierA~SupplierB+SupplierC',data=cof).fit()
aov_table=sm.stats.anova_lm(mod,type=2)
print(aov_table)


################# 2 proportion test ############
Johnytalkers = pd.read_csv("C:\\Users\\Vimod\\Downloads\\JohnyTalkers.mtw.csv")
count=pd.crosstab(Johnytalkers["Person"],Johnytalkers["Icecream"])
n1 = 58
p1 = .12
58/480
152/740
n2 = 152
p2 = .20
import numpy as np
population1 = np.random.binomial(1, p1, n1)
population2 = np.random.binomial(1, p2, n2)
sm.stats.ttest_ind(population1, population2)
sm.stats.ttest_ind(population1, population2,alternative = "smaller")

############### Mann-Whitney test(Vehicles with and without addictive) ############
data=pd.read_csv('C:\\Users\\Vimod\\Downloads\\Non-parametric additive.csv')
data
data.columns="Without_additive","With_additive"
#############Normality test###############
print(stats.shapiro(data.Without_additive))
print(stats.shapiro(data.With_additive))

############## Mann-Whitney test #############
import statsmodels.stats.descriptivestats as sd
from scipy.stats import mannwhitneyu
mannwhitneyu(data.Without_additive, data.With_additive)


############## 1 Sample Sign Test(Student_Scores) ################
#import statsmodels.stats.descriptivestats as sd
data=pd.read_csv("C:\\Users\\Vimod\\Downloads\\Signtest.csv")
data
#############Normality test###############
print(stats.shapiro(data.Scores))

###################1 Sample Sign Test #############
sd.sign_test(data.Scores,mu0=0)

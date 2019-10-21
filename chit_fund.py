# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:14:24 2019

@author: Murali
"""
#Usefull module like numpy and pandas as imported
import pandas as pd;
import numpy as np;

# data from excel sheet is readed as dataframe
data_set=pd.read_excel('chit_fund_data.xlsx');

#Amount Contributed By Each particant for each month is calculated 
data_set['totalAmountPaidByTheParticipant'] = data_set["Contribution"] - data_set["Amount returned to everyone in the group"]

#Total investment made by the participant in total 25 months
sum_of_investment = np.sum(data_set['totalAmountPaidByTheParticipant'])

# Absoulte return of amount by the person is calculated for 25 months
# Return amount =net amount got by bis winner - total amount investested
# if it is a positive value then it is profit else it is loss 
data_set['Amount returned'] =(data_set['Net amount recd by Bid winner']-sum_of_investment)

# Return percentage for each person is calculated and it is saved as Return percentage
data_set["Return percentage"] = (data_set["Amount returned"]/sum_of_investment)*100

# row and column values are saved in m and n
(m,n)=data_set.shape

#Annualized return for each participant is calculated
annualized_ret = []
for i in range(m):
    #Annualized return = ((1 + Absolute Rate of Return) ^ (12/no. of months)) – 1
    a=((((1 + (data_set["Return percentage"][i])/100)) ** (12/25)) - 1) * 100
    annualized_ret.append(a)
#Question 1
#The annualized return of participant who bids in the last Month is printed to the console
print("The annualized return of participant who bids in the last Month = "+str(annualized_ret[-1])+' %\n')

#Question 2
#The annualized return of participant who bids in the first Month is printed to the console
print("The annualized return of participant who bids in the first Month = "+str(annualized_ret[0])+' %\n')

#Question 3
#The annualized return of each participant is calculated and displayed 
for i in range(1,m+1):
    print("The annualized return of participant who bids in the "+str(i)+" Month = "+str(annualized_ret[i-1])+' %')
print('\n')  
for i in range(1,m+1):
    print("The Absolute return of participant who bids in the "+str(i)+" Month = "+str(data_set.loc[i-1,"Return percentage"])+' %')
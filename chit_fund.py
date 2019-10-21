# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:14:24 2019

@author: Murali
"""

import pandas as pd;
import numpy as np;



data_set=pd.read_excel('chit_fund_data.xlsx');
data_set['totalAmountPaidByTheParticipant'] = data_set["Contribution"] - data_set["Amount returned to everyone in the group"]
sum_of_investment = np.sum(data_set['totalAmountPaidByTheParticipant'])
data_set['Amount returned'] =(data_set['Net amount recd by Bid winner']-sum_of_investment)
data_set["Return percentage"] = (data_set["Amount returned"]/sum_of_investment)*100



# row and column values are 
(m,n)=data_set.shape
for i in range(m):
    #Annualized return = ((1 + Absolute Rate of Return) ^ (12/no. of months)) – 1
    a=((((1 + (data_set["Return percentage"][i])/100)) ** (12/25)) - 1) * 100
    print(a)
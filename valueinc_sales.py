#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:01:37 2024

@author: sreyabiswas
"""

#imorting panda library

import pandas as pd

#importing the csv file using panda

data = pd.read_csv('transaction2.csv')

#the imported csv file is using ; as separator

data = pd.read_csv('transaction2.csv', sep=';')

#creating summary of the data

data.info()

#working with calculations
#Mathematical Operations in Tableau

#CostPerTransaction Column calculation
#CostPerTransaction = CostPerItem * NumberOfItemsPurchased

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding a new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

#SalesPerTransaction Calculation

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup Calculation
#Markup = (cost -sales)/cost

data['Markup'] = ( data['ProfitPerTransaction'] ) / data['CostPerTransaction']

data['Markup'] = round(data['Markup'],2)

#changing datatype
day = data['Day'].astype(str)
year = data['Year'].astype(str)

#changing the date format
my_date = day+'-'+data['Month']+'-'+year

#creating a new column for new formatted date
data['Date'] = my_date

#using split() to split the ClientKeywords column

split_ClientKeywords = data['ClientKeywords'].str.split(',' , expand=True)

#Creating a new column in ClientKeywords

data['Client_Age'] = split_ClientKeywords[0]
data['Client_Type'] = split_ClientKeywords[1]
data['Client_YearOfContract'] = split_ClientKeywords[2]

#removing [ and ] from Client_Age and Client_YearOfContract

data['Client_Age'] = data['Client_Age'].str.replace('[' ,'')
data['Client_YearOfContract'] = data['Client_YearOfContract'].str.replace(']' , '')

#using lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#adding a new dataset

new_data = pd.read_csv('value_inc_seasons.csv',sep=';')

#merging two datasets into first imported file data

data = pd.merge(data,new_data, on ='Month')

#Dropping columns

data = data.drop('ClientKeywords',axis=1)
data = data.drop('Date',axis=1)
data = data.drop(['Year','Month'], axis=1)

#export to a new csv file

data.to_csv('CleanedFile.csv',index = False)

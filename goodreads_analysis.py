# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:56:00 2021

@author: Hanuska
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# I want my figures with white background and grid
sns.set_style('whitegrid')

# Creating dataframe
books = pd.read_csv('cms_scrape2.csv',encoding='latin-1')

# Gets basic info about our data set, not of the fields are null and we can see type of data
books.info()

# I saved links for specific books in csv file, but I dont need this information, so ill remove whole column
books.drop('Link',axis=1, inplace = True)

# We can get quick look at distribution of data with describe() function, we can see that 25% of books with highest number
# of votes has much more votes than 75 percentile
books['Number of votes'].describe()

# Next I am interested in number of pages across these books, again book with highest number of pages is 3x longer than 75 percentile
books['Number of pages'].describe()

# I want to see which books are the longest
books[books['Number of pages']>800]

# Bar chart for distinct genres, figsize was determined by testing, this size is well readable
plt.figure(figsize=(10,5))
langs = sns.barplot(x = books['Genre'].value_counts().index, y = books['Genre'].value_counts())
langs.set_xlabel("Genre")
langs.set_ylabel('Number of books')

# Most popular books according to number of votes
books[books['Number of votes']>10000]

# Is there corrolation between number of votes,rating and number of pages?
books[['Number of votes','Avg. Rating','Number of pages']].corr()

# Histogram for number of pages, I used range for x axis is divided into 200 increments by xticks
plt.hist(books['Number of pages'].value_counts().index,bins=20)
plt.xticks(range(0, 1600, 200))

# Histogram for number of votes
plt.figure(figsize=(10,5))
plt.hist(books['Number of votes'].value_counts().index,bins=20)
plt.xticks(range(0, 25000, 2500))

# Histogram for average rating, x axis is divided into 0.1 increments
plt.figure(figsize=(10,5))
plt.hist(books['Avg. Rating'].value_counts().index,bins=14)
plt.xticks(np.arange(3.3,4.7,.1))

















# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 10:55:28 2021

@author: Hanuska
"""

# Import the libraries I work with
from bs4 import BeautifulSoup
import requests
import csv
from itertools import islice
from urllib.parse import urljoin

# Created new csv, additional settings are for writting in csv without the blank rows
csv_file=open('cms_scrape.csv','w', newline='',encoding='cp1252')

# Created new writer that I use to actually write the information into csv file. Description row is created in order
# the description is written 
csv_write=csv.writer(csv_file)
csv_write.writerow(['Title','Link','Author','Avg. Rating','Score','Number of votes','Number of pages','Genre'])

# Created source object with requests that gets the content from the provided link
source=requests.get('https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once').content

# Created new BS4 object with defined html parser, in this instance I used 'lxml' and it works very well.
soup=BeautifulSoup(source,'lxml')

# Prepared empty lists that I'll fill with information about each book
title=[]
links=[]
author=[]
avg_rating=[]
score=[]
num_votes=[]
num_pages=[]
genre=[]

# In order to speed up scraping I looked only in part that contained relevant information instead of the whole html page
table=soup.find('table',{'class':'tableList js-dataTooltip'})

# In this for loop I get all the rows in above mentioned table
for tr in islice(table.find_all('tr'),100):
    
    # Using the class atribute I locate relevant information and use only text between the tags
    title_text=tr.find('a',{'class':'bookTitle'}).find('span').text
    
    # To get the links for specific titles I need to get the links and joined them with home website to get the full address
    title_link=tr.find('a',{'class':'bookTitle'}).attrs['href']
    link=urljoin('https://www.goodreads.com/', title_link)
    author_text=tr.find('a',{'class':'authorName'}).find('span').text
    
    # In this part I used split on ' ' to split text between the tags and get only the information I was looking for
    # Position of the information in the string in the html is always the same and I found it in the page source code
    avg_rating_text=tr.find('span',{'class':'greyText smallText uitext'}).text.split(' ')[1]
    score_text=tr.find('span',{'class':'smallText uitext'}).find('a').text.split(' ')[1]
    num_votes_text=tr.find('span',{'class':'smallText uitext'}).find_all('a')[1].text.split(' ')[0]
    
    # With all the information gathered I appended it to created lists
    title.append(title_text)
    links.append(link)   
    author.append(author_text)
    avg_rating.append(avg_rating_text)
    score.append(score_text)
    num_votes.append(num_votes_text)
    
    
    # In this for loop I scrape information that isn't available on the main page like number of pages or genre.
    # Inumerate is used for correct writing into csv file, because I gather some information in different loop 
    # This always pair the information to the right row
    
for i,link in enumerate(links):
    sub_page=requests.get(link).content
    
    # Here I used html5 parser, because 'lxml' was inconsistent
    sub_soup=BeautifulSoup(sub_page,'html5lib')
    
    # I specify part of html where the information is located
    content=sub_soup.find("div", {"class": "mainContentFloat"})
    
    # Number of pages is text formated like this " x pages" with strip I can get only the number from this string
    num_pages_text=content.find("div", {"class": "row"})
    num_pages_text=num_pages_text.find("span", {"itemprop": "numberOfPages"}).text.strip(' pages')
    
    # Genre is simple text between the tags so no further manipulation was needed
    genre_text=content.find("a", {"class": "actionLinkLite bookPageGenreLink"}).text

    # Appended information to the lists
    num_pages.append(num_pages_text)
    genre.append(genre_text)

    # Index is the same for both lists, csv_write writes rows in the defined order, this is the same as description row order
    csv_write.writerow([title[i],links[i],author[i],avg_rating[i],score[i],num_votes[i],num_pages[i],genre[i]])
        
# Closed the csv file so I could work with it    
csv_file.close()


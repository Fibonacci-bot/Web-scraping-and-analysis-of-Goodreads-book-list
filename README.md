# Web scraping and analysis of Goodreads book list
Web scraping Goodreads book list using Python and BeautifulSoup library along with quick data analysis in Python with pandas and matplotli

I was interested in what kinds of books are most often recommended in the most popular book list on Goodreads so I decided to use web scraping to gather information about top 100 books in [Books That Everyone Should Read At Least Once](https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once) . Below you can find all the information I decided to gather.


## Project overview
* Created a tool for scraping data from Goodreads book lists
* Saved all the data in csv file
* Looked at the distribution of the data and analysed it, below are a few highlights from this data set.

## Python version and packages used 
**Python Version:** 3.8  
**Packages:** pandas, numpy, matplotlib, seaborn, BeautifulSoup4

## Web Scraping
During the web scraping part of this project I decided what information I want to scrape and what would give me an interesting insight into these lists. Below you can find all the information I decided to gather.

1. Title
2. Link
3. Author
4. Average rating
5. Score
6. Number of pages
7. Genre

This data was then saved in csv file for further analysis. You can see commented python code here [scraper](https://github.com/Fibonacci-bot/Web-scraping-and-analysis-of-Goodreads-book-list/blob/main/goodreads_scraper.py).

## Data Analysis

Since I scraped only the data I needed there was almost no need for data cleaning besides deleting one column containing links for specific book pages. I looked at the distribution of the data and the value counts for each category and found some interesting highlights.

  ![Genres](/images/genres.png)
  ![Number of pages](/images/pages_hist.png)
  ![Average rating](/images/rating_hist.png)
  ![Number of votes](/images/votes_hist.png)
  
I also looked into correlation between the number of votes, average rating and number of pages with. Based on this books with higher number of votes have higher average rating and books with more pages have slightly lower number of votes but higher average rating. You can find more details in commented code here [analysis](https://github.com/Fibonacci-bot/Web-scraping-and-analysis-of-Goodreads-book-list/blob/main/goodreads_analysis.py)






import praw
import pandas as pd
from datetime import datetime as dt
import time, calendar
import psycopg2
import time
import pymongo
starttime=time.time()
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import scipy.stats as stats
from scipy.stats import linregress


def simple_reddit_scraper():
    reddit = praw.Reddit(client_id='YOUR CLIENT_ID', \
                     client_secret='YOUR CLIENT_SECRET', \
                     user_agent='Sub Scraper', \
                     username='YOUR USERNAME HERE', \
                     password='YOUR PASSWORD HERE')

    subreddit = reddit.subreddit('all')
    top_subreddit = subreddit.hot(limit=10000)

# Use list comprehension to create a list of lists representing each post
    df_rows = [[submission.id, submission.title, submission.selftext, submission.score, submission.url, submission.num_comments, dt.utcfromtimestamp(submission.created)] for submission in top_subreddit]
# Create df using rows, set column titles
    df = pd.DataFrame(df_rows, columns=['ID', 'Title', 'Body', 'Score', 'URL', 'Comments', 'Created'])
    return df

scraped_df = simple_reddit_scraper()

# Run this while loop to grab a new df selection each 60 seconds and then append it to the original scraped dataframe
while True:
    dataframe = simple_reddit_scraper()
    scraped_df = pd.concat([scraped_df, dataframe], join  = 'outer', axis = 0, ignore_index = True)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

file = "PATH TO CSV FILE"
cleaned_final.to_csv(file, sep='\t', encoding='utf-8', parse_dates = ['Created'])
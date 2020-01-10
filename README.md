# Simple Reddit Scraper: Analysis of Reddit Scores and Comments by Hour of Day
## Background
After 8 years of using reddit, I had always thought it was odd how their appeared to be a noticeable amount of posts that had a significant amounts of score points (simply the number of upvotes minus the number of downvotes ), but concurrently did not have a comparable amount of comments, and vice versa. With that in mind, I wanted to analyse reddit posts to see if their was any meaning behind my observation. 

This post https://np.reddit.com/r/BlackPeopleTwitter/comments/8m9hpq/stretch_it_out/ provides an excellent example of what im speaking to. The score value (~67.0k) is noticeably higher than the amount of comments it received (474) before being archived. While this is not even frequently the case, i came across posts like this often enough to notice it. 

While studying reddit to find information related to this idea, i also noticed that there was a distinct enough spike in the amount of upvotes and comments an average post would receive during night time. This is reasonable, considering that most of the reddit community is either engaging in school or work during the 'working hours' (9:00 to 18:00) of the day. 

Seeking to understand exactly what it is that ties these three factors together, I focused on these three categories for scraping. I chose to scrape from the hot post organization on r/all in order to get posts that were suitably “seen” and had been generally given a chance to receive upvotes and comments before scraping.

## First steps
I created my scraper using the reddit api with PRAW (Python Reddit API Wrapper) to scrape datetime,ID, number of comments, title text, score, bodytext, and URLs from reddit/r/all. The data was stored on my local machine in a csv.  

Immediately, i saw there was an error with the body text, so this was immediately dropped from the dataframe for this project. I also removed data from the dataframe under the columns ID, Unnamed:0 (this was an artifact of reading in the csv), Title, and URL. They were not needed for this analysis, but are still stored in the case of future interest. Rows were then dropped if they were missing any daya. Finally, the nature of my scraper created a large number of duplicate values, so it was necessary to drop duplicates. 

## Data Analysis

I scraped 69395 posts using my scraper. This was from reddit/r/all, so the posts came from a wide variety of the website's selected, popular subreddits. 

The average comment value was 27.23 and the average score was 699.77. Later on, i would use these values to determine which posts would be considered having been seen enough to merit further analyses. 

![Graph of number of average posts made per hour over the period of scraping](https://github.com/Jameshskelton/Simple-Reddit-Scraper/blob/master/Images/corrected_hist_dayshours.png?raw=true)

The data was binned into the number of hours scraped, from there we can see that there is distinct peaks and troughs that form around midnight each day and 13:00 each day, respectively



import pandas as pd     # To handle data
import numpy as np      # For number computing
from IPython.display import display

from TwitterConfig import *
from AnalysisFactory import *
from PieChartGenerator import showPieChart

extractor = twitter_init()

#Change the Query on q param

tweets = extractor.search(q="Muslim",lang="en",count="200")
print("Number of tweets extracted: {}.\n".format(len(tweets)))


# Panda dataframe
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
data['length']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])

display(data.head(200))

pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
print("Percentage of negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))

showPieChart(positive=len(pos_tweets),neutral=len(neu_tweets),negative=len(neg_tweets))
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import twitter as tw
OAUTH_TOKEN='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA'
OAUTH_SECRET='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A'
CONSUMER_KEY='HrI9pkJWwsdTL1jv9fDmg'
CONSUMER_SECRET='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI'

# <codecell>

t = tw.Twitter(auth=tw.OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET))

# <codecell>

fb_mentions = t.search.tweets(q='@facebook',lang='en',result_type='recent',count=100)

# <codecell>

print fb_mentions.keys()

# <codecell>

fb_mentions['search_metadata']

# <codecell>

fb_mentions['statuses'][0]

# <codecell>

fb_mention_tweets = []
for status in fb_mentions['statuses']:
    fb_mention_tweets.append(status['text'])

# <codecell>

fb_mention_tweets[0:5]

# <codecell>

fb_neg_tweets = t.search.tweets(q='facebook -"www.facebook" -@facebook :(',lang='en',result_type='recent',count=100)

# <codecell>

fb_neg_tweet_text = []
for status in fb_neg_tweets['statuses']:
    fb_neg_tweet_text.append(status['text'])

# <codecell>

fb_neg_tweet_text[0:5]

# <codecell>

neg_words = ['hate','terrible','awful','worse','worst','difficult','struggle','pain','annoy']
pos_words = ['love','like','great','easy','awesome','brilliant','interesting','fantastic','wonderful','amazing','stunning','charming']

# <codecell>

fb_neg_tweets = t.search.tweets(q='facebook -"www.facebook" -@facebook hate',lang='en',result_type='recent',count=100)

# <codecell>

fb_neg_tweet_text = []
for status in fb_neg_tweets['statuses']:
    fb_neg_tweet_text.append(status['text'])

# <codecell>

fb_neg_tweet_text[0:5]

# <codecell>

fb_neg_tweets = t.search.tweets(q='"hate facebook"',lang='en',result_type='recent',count=100)

# <codecell>

fb_neg_tweet_text = []
for status in fb_neg_tweets['statuses']:
    fb_neg_tweet_text.append(status['text'])

# <codecell>

fb_neg_tweet_text[0:5]

# <codecell>

fb_pos_tweets = t.search.tweets(q='"love facebook"',lang='en',result_type='recent',count=100)

# <codecell>

fb_pos_tweet_text = []
for status in fb_pos_tweets['statuses']:
    fb_pos_tweet_text.append(status['text'])

# <codecell>

fb_pos_tweet_text[0:5]

# <codecell>

import numpy as np
import pandas as pd

# <codecell>

timestring = fb_pos_tweets['statuses'][0]['created_at']

# <codecell>

print timestring

# <codecell>

from dateutil import parser as dateparser

# <codecell>

tweettime = dateparser.parse(timestring)

# <codecell>

tweettime

# <codecell>

pos_times = []
for status in fb_pos_tweets['statuses']:
    pos_times.append(dateparser.parse(status['created_at']))

# <codecell>

pos_times.sort()

# <codecell>

neg_times = []
for status in fb_neg_tweets['statuses']:
    neg_times.append(dateparser.parse(status['created_at']))

# <codecell>

neg_times.sort()

# <codecell>

tdeltas = np.empty([2,len(fb_pos_tweets['statuses'])-1])

# <codecell>

tstart = False
idx = 0
for tweettime in pos_times:
    if not tstart:
        tstart = tweettime
    else:
        tdelta = tweettime - tstart
        tdeltas[0,idx] = tdelta.seconds
        tstart = tweettime
        idx += 1  

# <codecell>

tstart = False
idx = 0
for tweettime in neg_times:
    if not tstart:
        tstart = tweettime
    else:
        tdelta = tweettime - tstart
        tdeltas[1,idx] = tdelta.seconds
        tstart = tweettime
        idx += 1  

# <codecell>

np.mean(tdeltas, axis=1)

# <codecell>

import scipy as sci

# <codecell>

from scipy import stats

# <codecell>

stats.ttest_ind(tdeltas[0,:],tdeltas[1,:])

# <codecell>

means = np.mean(tdeltas, axis=1)

# <codecell>

means_dict = {'Positive':means[0],'Negative':means[1]}

# <codecell>

stds= np.std(tdeltas, axis=1)

# <codecell>

import matplotlib.pyplot as plt

# <codecell>

np.arange(2)

# <codecell>

bar_width = 0.35
opacity = 0.5
error_config = {'ecolor':'0.3'}
rects = plt.bar([0.5,1.5], means, bar_width, bottom=0, alpha=opacity, color='b', yerr=stds, error_kw=error_config)
plt.xlabel('Sentiment')
plt.ylabel('Secs between posts')
plt.xticks([0.5,1.5], ('Positive','Negative'))
plt.show()

# <codecell>

import vincent
vincent.core.initialize_notebook()

# <codecell>

bar = vincent.Bar(means_dict)
bar.axis_titles(x='Valence', y='Inter-tweet time')
bar.scales['x'].padding = 0.2
bar.height=300
bar.width=300
bar.display()

# <codecell>

bar.to_json('intertweet.json', html_out=True, html_path='intertweet.html')

# <codecell>



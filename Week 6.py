# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# MySQL

# <markdowncell>

# install mysql + workbench: http://dev.mysql.com/downloads/mysql/
# 
# install pymysql: 'sudo pip install pymysql'

# <codecell>

import pymysql

dbuser = 'professor'
dbpass = 'Business1Q'

# <codecell>

conn = pymysql.connect(host='localhost', 
                       user=dbuser, 
                       passwd=dbpass, 
                       db='BIA660')

# <codecell>

cur = conn.cursor()    

# <codecell>

query = '''CREATE TABLE IF NOT EXISTS tweet (
                                id BIGINT UNSIGNED,
                                user BIGINT UNSIGNED,
                                text VARCHAR(140) CHARACTER SET utf8,
                                favorited TINYINT UNSIGNED,
                                created DATETIME,
                                in_reply_to_user_id BIGINT UNSIGNED,
                                in_reply_to_status_id BIGINT UNSIGNED,
                                PRIMARY KEY (id)
                            )'''

# <codecell>

cur.execute(query)

# <codecell>

query = '''CREATE TABLE IF NOT EXISTS user (
    id BIGINT UNSIGNED,
    name VARCHAR(140) CHARACTER SET utf8,
    screen_name VARCHAR(80),
    location VARCHAR(140) CHARACTER SET utf8,
    time_zone VARCHAR(40),
    description TEXT CHARACTER SET utf8,
    followers_count BIGINT,
    friends_count BIGINT,
    tweet_count BIGINT,
    updated TIMESTAMP,
    PRIMARY KEY (id))'''

# <codecell>

cur.execute(query)

# <codecell>

import twitter as tw
OAUTH_TOKEN='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA'
OAUTH_SECRET='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A'
CONSUMER_KEY='HrI9pkJWwsdTL1jv9fDmg'
CONSUMER_SECRET='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI'
t = tw.Twitter(auth=tw.OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET))
fb_mentions = t.search.tweets(q='@facebook',lang='en',result_type='recent',count=100)

# <codecell>

for status in fb_mentions['statuses']:
    user = status['user']
    tweet_vals = (status['id'],user['id'],
                  status['favorited'], 
                  status['in_reply_to_user_id'] or 0,
                  status['in_reply_to_status_id'] or 0)
    user_vals = (user['id'],user['screen_name'],
                 user['followers_count'],
                 user['friends_count'], user['statuses_count'])
    query = u'INSERT INTO tweet VALUES(%d, %d, "not the tweet", %d, NULL, %d, %d)' % tweet_vals
    cur.execute(query)
    is_user = cur.execute("SELECT id FROM user WHERE id=%d" % int(user['id']))
    if not is_user:
        query = "INSERT INTO user VALUES(%d,'None','%s','Location','TZ','DESC',%d,%d,%d,NOW())" % user_vals
        cur.execute(query)
conn.commit()

# <codecell>

conn.commit()

# <codecell>

query = 'SELECT tweet.id FROM tweet JOIN user ON tweet.user=user.id WHERE user.followers_count>100'
success = cur.execute(query)
tweet_ids = cur.fetchall()
for tweet_id in tweet_ids:
    print tweet_id

# <codecell>

cur.close()
conn.close()

# <headingcell level=2>

# MongoDB

# <markdowncell>

# install MongoDB: http://docs.mongodb.org/manual/installation/
# 
# 'sudo pip install pymongodb'

# <codecell>

from pymongo import MongoClient

# <codecell>

client = MongoClient()

# <codecell>

db = client.test_database

# <codecell>

collection = db.test_collection

# <codecell>

import datetime
datetime.datetime.utcnow()

# <codecell>

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

# <codecell>

posts = db.posts

# <codecell>

post_id = posts.insert(post)

# <codecell>

post_id

# <codecell>

db.collection_names()

# <codecell>

posts.find_one()

# <codecell>

posts.find_one({"author": "Mike"})

# <codecell>

posts.find_one({"author": "Winter"})

# <codecell>

new_posts = [{"author": "Mike",
            "text": "Another post!",
            "tags": ["bulk", "insert"],
            "date": datetime.datetime(2009, 11, 12, 11, 14)},
            {"author": "Eliot",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45)}]

# <codecell>

posts.insert(new_posts)

# <codecell>

for post in posts.find():
    print post

# <codecell>

posts.count()

# <codecell>

posts.find({"author": "Mike"}).count()

# <codecell>

d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print post

# <codecell>

print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]

# <codecell>

from pymongo import ASCENDING, DESCENDING
posts.create_index([("date", DESCENDING), ("author", ASCENDING)])

# <codecell>

print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]

# <codecell>

posts.update({"author": "Mike"}, { "$set": { "author": "Winter"} })

# <codecell>

posts.remove({"author":"Eliot"})

# <headingcell level=2>

# More on visualizations

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
import pylab

# <headingcell level=4>

# Bar chart

# <codecell>

numTests = 5
testNames = ['Pacer Test', 'Flexed Arm\n Hang', 'Mile Run', 'Agility',
            'Push Ups']
rankings = np.round(np.random.uniform(0, 1, numTests)*100, 0)

# <codecell>

rankings

# <codecell>

fig, ax1 = plt.subplots(figsize=(9,7))
plt.subplots_adjust(left=0.115, right=0.88)
fig.canvas.set_window_title('Fitness Chart')
pos = np.arange(numTests)+0.5    #Center bars on the Y-axis ticks
rects = ax1.barh(pos, rankings, align='center', height=0.5, color='m')
ax1.axis([0,100,0,5])
pylab.yticks(pos, testNames)

# <codecell>

np.arange(numTests)+0.5

# <headingcell level=4>

# Histogram

# <codecell>

#
# first create a single histogram
#
mu, sigma = 200, 25
x = mu + sigma*pylab.randn(10000)

# <codecell>

x[1:10,]

# <codecell>

# the histogram of the data with histtype='step'
n, bins, patches = pylab.hist(x, 50,  normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.15)

# <codecell>

# add a line showing the expected distribution
y = pylab.normpdf( bins, mu, sigma)
l = pylab.plot(bins, y, 'r.', linewidth=1.5)

# <codecell>

bins = [100,125,150,160,170,180,190,200,210,220,230,240,250,275,300]
# the histogram of the data with histtype='step'
n, bins, patches = pylab.hist(x, bins, normed=1, histtype='bar', rwidth=0.8)

# <headingcell level=4>

# Scatter plot

# <codecell>

# get friend and follower counts from db
query = "SELECT followers_count, friends_count FROM user LIMIT 100"
success = cur.execute(query)
counts = cur.fetchall()

# <codecell>

counts = array(counts)

# <codecell>

counts[1:10,0]

# <codecell>

fig, ax = plt.subplots()
ax.plot(log(counts[:,0]+1), log(counts[:,1]+1), 'o')
ax.set_title('Friends and Followers')
plt.show()

# <headingcell level=4>

# Line plot

# <codecell>

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

plt.errorbar(x, y, yerr=0.4)
plt.show()

# <codecell>

fnx = lambda : np.random.randint(5, 50, 10)
y = np.row_stack((fnx(), fnx(), fnx()))
x = np.arange(10)

y1, y2, y3 = fnx(), fnx(), fnx()

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3)
plt.show()

# <codecell>



import re

fh = open('Sample.txt','r')

wordcounts = {}
for line in fh:
    words = line.split(' ')
    for word in words:
        cleanword = re.sub('\W','',word).lower()
        if cleanword in wordcounts:
            wordcounts[cleanword] += 1
        else:
            wordcounts[cleanword] = 1

for key,value in wordcounts.iteritems():
    print key + ': ' + str(value)

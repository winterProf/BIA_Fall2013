# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

fh = open('testEmails.txt','r')
fh.read() # returns whole file

# <codecell>

fh = open('testEmails.txt','r')
fh.readline() # reads the first line (pointer to first line)

# <codecell>

fh.next() # reads the next line

# <codecell>

fh = open('testEmails.txt','r')
fh.readlines()

# <codecell>

fh = open('testEmails.txt','r')
for line in fh:
    print line

# <codecell>

fh.close()

# <codecell>

fh = open('testdoc.txt','w')

# <codecell>

fh.write('This is the first line\n')

# <codecell>

fh.writelines(['stringonee','string2','stringthree'])
fh.write('\n'.join(['stringonee','string2','stringthree']))

# <codecell>

fh.close()
fg = open('testdoc.txt','r')
fg.read()

# <codecell>

fg.close()

# <headingcell level=3>

# urllib

# <codecell>

import urllib

# <codecell>

f = urllib.urlopen('http://smallsocialsystems.com/')
for line in f:
    print line

# <codecell>

# GET method
params = urllib.urlencode({'p': 208, 'alpha':'a string & stuff'}) 

# <codecell>

print params

# <codecell>

f = urllib.urlopen('http://smallsocialsystems.com/blog/?%s' % params)
f.read()

# <codecell>

# POST method
params = urllib.urlencode({'p': 208}) 
f = urllib.urlopen('http://smallsocialsystems.com/blog/', params)
f.read()

# <headingcell level=3>

# Beautiful Soup

# <codecell>

import BeautifulSoup as bs4

# <codecell>

f = urllib.urlopen('http://smallsocialsystems.com')
sss_html = f.read()
sssoup = bs4.BeautifulSoup(sss_html)

# <codecell>

print(sssoup.prettify())

# <codecell>

sssoup.title

# <codecell>

sssoup.title.string

# <codecell>

for elem in sssoup.findAll('a',class_='buttonlabel'):
    print elem

# <codecell>

f = urllib.urlopen('http://smallsocialsystems.com/blog/?%s' % params)
sss_html = f.read()
sssoup = bs4.BeautifulSoup(sss_html)
for link in sssoup.findAll('a'):
    print(link.get('href'))

# <headingcell level=3>

# mechanize

# <codecell>

import mechanize

# <codecell>

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# <codecell>

r = br.open('http://smallsocialsystems.com/blog/?p=208')

# <codecell>

r.read()

# <codecell>

for link in br.links():
    print link.url

# <codecell>

r2 = br.follow_link(text_regex=r"\s*",nr=1)

# <codecell>

print r2.geturl()

# <codecell>

r3 = br.back()

# <codecell>

r3.geturl()

# <codecell>

print r2.info()

# <headingcell level=3>

# Live Journal example

# <codecell>

jstr = """
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
"""

# <codecell>

import json

# <codecell>

try:
    objs = json.loads(jstr)
except ValueError:
    print 'error'
else:
    print 'acceptable json'

# <codecell>

objs['glossary']['GlossDiv']['GlossList']

# <codecell>

from twitter import *
OAUTH_TOKEN='19202628-1t97auu1YH1zxtIOB4rQ3F056TEZPlUqUs3LoFCTa'
OAUTH_SECRET='kuAD2MAExNlu7IwImoRAm1wbpdm5xc9gCGctL83c'
CONSUMER_TOKEN='kXPnvcf4UzGUi57e6LaLw'
CONSUMER_SECRET='HHlRwgG0F6qY0DYFH8yIUaRiDgvOkphoijamueJvjwY'

# <codecell>

t = Twitter(auth=OAuth(OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_TOKEN,CONSUMER_SECRET))

# <codecell>

jstr = t.statuses.retweets_of_me()

# <codecell>

for tweet in jstr:
    print tweet['text']

# <codecell>



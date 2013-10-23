# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep
import boto.emr

# <codecell>

### Adding and deleting files from S3

#s3con = S3Connection('<aws access key>', '<aws secret key>')
s3con = S3Connection('AKIAJRV3RN6NXQTSSTBA', '3e212d6rs99xtiPgwKnfN1QD30WZk2hJwCWjMcGc')

# <codecell>

#b = s3con.create_bucket('winteram-boto-example')
b = s3con.get_bucket('wambia660fall2013')

# <codecell>

k = Key(b)
k.key = 'mapper.py'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/mapper.py')
k.close()

# <codecell>

k = Key(b)
k.key = 'reducer.py'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/reducer.py')
k.close()

# <codecell>

for word in b.list():
    print word

# <codecell>

### Running code with EMR

#emrcon = EmrConnection('<aws access key>', '<aws secret key>')
emrcon = EmrConnection('AKIAJRV3RN6NXQTSSTBA', '3e212d6rs99xtiPgwKnfN1QD30WZk2hJwCWjMcGc')

# <codecell>

# Using EMR's wordcount example
step = StreamingStep(name='My wordcount example',
	mapper='s3n://elasticmapreduce/samples/wordcount/wordSplitter.py',
	reducer='aggregate', 
	input='s3n://elasticmapreduce/samples/wordcount/input',
	output='s3n://wambia660fall2013/output/wordcount_output')

# <codecell>

jobid = emrcon.run_jobflow(name='Word Count Example', 
                           log_uri='s3://wambia660fall2013/logs',
                           steps=[step])

# <codecell>

print jobid

# <codecell>

import re

# <codecell>

for word in b.list():
    keystring = str(word.key)
    if re.match(keystring,'part-00000'):
        word.get_contents_to_filename('/Users/winteram/Documents/Teaching/wordcount_output.txt')

# <codecell>

# Doing our own word counts
step = StreamingStep(name='Alcohol Step',
	mapper='s3n://bia660-winter/mapper.py',
	reducer='s3n://bia660-winter/reducer.py', 
	input='s3://datasets.elasticmapreduce/ngrams/books/20090715/eng-us-all/3gram/data',
	output='s3n://bia660-winter/output')

# <codecell>

jobid = emrcon.run_jobflow(name='Alcohol Religion 6', log_uri='s3://bia660-winter/logfiles',steps=[step],num_instances=4)

# <codecell>

jobid

# <codecell>

status = emrcon.describe_jobflow(jobid)
print status.state

# <codecell>



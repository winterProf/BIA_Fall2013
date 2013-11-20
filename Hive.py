# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.emr.connection import EmrConnection
import boto.emr.step as step
import boto.emr

# <codecell>

### Create connection to own bucket
s3con = S3Connection('AKIAJRV3RN6NXQTSSTBA', '3e212d6rs99xtiPgwKnfN1QD30WZk2hJwCWjMcGc')

# <codecell>

b = s3con.get_bucket('wambia660fall2013')

# <codecell>

k = Key(b)
k.key = 'fullNgramNamesBoto.hql'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/BIA_Fall2013/fullNgramNamesBoto.hql')
k.close()

# <codecell>

### Will run Hive via EMR
emrcon = EmrConnection('AKIAJRV3RN6NXQTSSTBA', '3e212d6rs99xtiPgwKnfN1QD30WZk2hJwCWjMcGc')

# <codecell>

install_hive_step = step.InstallHiveStep(hive_versions='0.11.0.1')

# <codecell>

names1gram = step.HiveStep("fullNgramNamesBoto",
                           's3://wambia660fall2013/fullNgramNamesBoto.hql',
                           hive_args=['-d INPUT=s3://datasets.elasticmapreduce/ngrams/books/20090715/eng-us-all/1gram/', 
                                      '-d OUTPUT=s3://wambia660fall2013/output/'])

# <codecell>

jobid = emrcon.run_jobflow(name='Names 1gram boto v3', 
                           log_uri='s3://wambia660fall2013/logs/',
                           steps=[install_hive_step,
                                  names1gram], 
                           enable_debugging=True,
                           master_instance_type='m1.medium', 
                           slave_instance_type='m1.medium',
                           num_instances=4,
                           hadoop_version='1.0.3')

# <codecell>

print jobid

# <codecell>

status = emrcon.describe_jobflow(jobid)
print status.state

# <codecell>

k = Key(b)
k.key = 'namesInBooks.hql'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/BIA_Fall2013/namesInBooks.hql')
k.close()

# <codecell>

k = Key(b)
k.key = 'inputBooksTable.hql'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/BIA_Fall2013/inputBooksTable.hql')
k.close()

# <codecell>

k = Key(b)
k.key = 'splitBooks.hql'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/BIA_Fall2013/splitBooks.hql')
k.close()

# <codecell>

k = Key(b)
k.key = 'findNames.hql'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/BIA_Fall2013/findNames.hql')
k.close()

# <codecell>

### Will run Hive via EMR
emrcon = EmrConnection('AKIAJRV3RN6NXQTSSTBA', '3e212d6rs99xtiPgwKnfN1QD30WZk2hJwCWjMcGc')

# <codecell>

install_hive_step = step.InstallHiveStep(hive_versions='0.11.0.1')

# <codecell>

inputBooksTable = step.HiveStep("inputBooks",
                                's3n://wambia660fall2013/inputBooksTable.hql',
                           hive_args=['-d INPUT=s3://datasets.elasticmapreduce/ngrams/books/20090715/eng-us-all/1gram/'])

# <codecell>

splitBooks = step.HiveStep("splitBooks",
                           's3n://wambia660fall2013/splitBooks.hql')

# <codecell>

findNames = step.HiveStep("findNames",
                          's3n://wambia660fall2013/findNames.hql',
                           hive_args=['-d OUTPUT=s3://wambia660fall2013/output/'])

# <codecell>

jobid = emrcon.run_jobflow(name='Names in Books v2', 
                           log_uri='s3n://wambia660fall2013/logs/',
                           steps=[install_hive_step,
                                  inputBooksTable,
                                  splitBooks,
                                  findNames], 
                           enable_debugging=True,
                           master_instance_type='m1.medium', 
                           slave_instance_type='m1.medium',
                           num_instances=4,
                           hadoop_version='1.0.3')

# <codecell>

print jobid

# <codecell>

status = emrcon.describe_jobflow(jobid)
print status.state

# <codecell>



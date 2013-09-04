# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import scipy 

# <codecell>

a = np.array([1,4,5],float)
a

# <codecell>

A = np.array([[1,4,7],[3,6,9],[2,5,8]])
A

# <codecell>

np.cross(a,A)

# <codecell>

vals, vecs = np.linalg.eig(A)

# <codecell>

vecs

# <codecell>

B = np.array([[7,5,6,4,1,2,3],[2,1,3,5,8,9,7]])

# <codecell>

np.corrcoef(B)

# <codecell>

np.cov(B)

# <codecell>

np.std(a)

# <codecell>

np.random.rand(5)

# <codecell>

np.random.random()

# <codecell>

for i in range(10):
    print round(np.random.normal(68,5))

# <codecell>

li = ['a','b','c','d','e','f','g','h']
np.random.shuffle(li)
li

# <codecell>

from scipy import stats

# <codecell>

norm.cdf(0)

# <codecell>

stats.gamma(1, scale=2).rvs(size=5)

# <codecell>

import pandas

# <codecell>

d = pandas.DataFrame([{'a':1,'b':2},{'a':3,'b':4,'c':0}])

# <codecell>

data2 = [{'a':1,'b':2},{'a':3,'b':4,'c':0}]

# <codecell>

f = pandas.DataFrame(data2, index=['row1','row2'])

# <codecell>

f

# <codecell>



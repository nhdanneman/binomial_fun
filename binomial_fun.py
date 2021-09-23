from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

'''
The Binomial distribution describes the number of success, out of a 
certain number of trials, given a certain underlying probability.

It is often used to model sampling *with replacement*, but as the 
number of trials grows that doesn't realy matter.
'''

# getting acquainted
# What's the probability of a fair coin coming up heads?
binom.pmf(1, 1, 0.5) # one success, one flip, 0.5 probability of "success"
# 0.5

# What's the probability of having 1 out of 2 kids be girls?
binom.pmf(1, 2, 0.5) # one success, two tries, probabilty = 0.5
# 0.5
# (boy,boy), (boy,girl), (girl,girl), (girl,boy)
# exactly half of those have precisely 1 girl

# If Jordan is an 84% free-throw shooter, how likely is he to make these two in a row?
binom.pmf(2, 2, 0.84)
# about 71% likely

# If Shaq is a 53% free-throw shooter, how likely is he to make tow in a row?
binom.pmf(2, 2, 0.53)
# 28%

'''
Get to the point!
Suppose we check k out of x files on a computer system for consistency.
We can assess the support for various probabilities.
'''

# What's the likelihood of 1000 of 1000 files being cool if only 98% of files are good?
binom.pmf(1000, 1000, .99)
# 4e-5  (read: four times ten to the negative fifth; i.e. 0.00004)
# very, very unlikely

# What about 0.999
binom.pmf(1000, 1000, .999)
# 0.37

# We can use this to check out the support for various probabilities
# only going to bother with those from 0.98 - 1.0
probs = np.arange(0.98, 1.0, 0.001)

# likelihood of seeing 1000 of 1000 under various probabilities:
likelihoods = []
for i in probs:
    likelihoods.append(binom.pmf(1000, 1000, i))

plt.scatter(probs, likelihoods)




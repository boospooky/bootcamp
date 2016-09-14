import numpy as np
import scipy.stats
import bootcamp_utils

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18,
'axes.titlesize': 18}
sns.set(rc=rc)

wt_lac = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',')
wt_lac = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',')

import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# We will use Seaborn styling to make plots look nicer Commented out
# here for demonstration later in this lesson
# import seaborn as sns

# The following is specific Jupyter notebooks
# %matplotlib inline
# %config InlineBackend.figure_formats = {'png', 'retina'}

# In our IPython terminal do:
#%matplotlib

# Load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Generate the histogram for the low-density fed mother
_ = plt.hist(xa_low)

# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')
plt.show()
plt.close()

# You need this is you didn't use %matplotlib in IPython shell
# plt.show()

import seaborn as sns
sns.set()

# Generate the histogram for the low-density fed mother
_ = plt.hist(xa_low)

# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')
plt.show()

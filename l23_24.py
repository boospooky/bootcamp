import numpy as np
#% matplotlib
# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)
iptg = data_txt[:,0]
gfp = data_txt[:,1]

# _ = plt.plot(iptg, gfp, marker='.', linestyle='none')
# # Add axis labels
# plt.xlabel('IPTG (µm$^2$)')
# plt.ylabel('GFP (normalized)')
# plt.savefig('collins_switch.pdf')
# plt.show()
#
# plt.figure()
# plt.title('loglog')
# _ = plt.loglog(iptg, gfp, marker='.', linestyle='none')
# # Add axis labels
# plt.xlabel('IPTG (µm$^2$)')
# plt.ylabel('GFP (normalized)')
# #plt.show()
#
# plt.figure()
# _ = plt.semilogx(iptg, gfp, marker='.', linestyle='none')
# # Add axis labels
# plt.title('logx')
# plt.xlabel('IPTG (µm$^2$)')
# plt.ylabel('GFP (normalized)')
# #plt.show()
#
# plt.figure()
# plt.title('logy')
# _ = plt.semilogy(iptg, gfp, marker='.', linestyle='none')
# # Add axis labels
# plt.xlabel('IPTG (µm$^2$)')
# plt.ylabel('GFP (normalized)')
# #plt.show()

sem = data_txt[:,2]

plt.figure()
plt.title('w/error')
#_ = plt.semiloglog(iptg, gfp, marker='.', linestyle='none')
_ = plt.errorbar(iptg, gfp, yerr=sem, marker='.', linestyle='none',
                 markersize=20)
# Add axis labels
plt.xscale('log')
plt.xlabel('IPTG (µm$^2$)')
plt.ylabel('GFP (normalized)')
plt.show()

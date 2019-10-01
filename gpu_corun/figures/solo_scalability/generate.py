#!/usr/bin/env python3
import numpy as np
import matplotlib
matplotlib.use('agg') 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def setAxLinesBW(ax):
    """
    Take each Line2D in the axes, ax, and convert the line style to be 
    suitable for black and white viewing.
    """
    MARKERSIZE = 3

    COLORS = [
        # grayscale
        #{'marker': None, 'dash': (None,None)},
        #{'marker': None, 'dash': [5,5]},
        #{'marker': None, 'dash': [5,3,1,3]},
        #{'marker': None, 'dash': [1,3]},
        #{'marker': None, 'dash': [5,2,5,2,5,10]},
        #{'marker': None, 'dash': [5,3,1,2,1,10]},
        #{'marker': 'o', 'dash': (None,None)} #[1,2,1,10]}
        {'marker': 'o', 'dash': (None, None)},
        {'marker': '^', 'dash': (None, None)},
        {'marker': 's', 'dash': (None, None)},
        {'marker': '*', 'dash': (None, None)},
        {'marker': '+', 'dash': (None, None)},
        ]


    lines_to_adjust = ax.get_lines()
    try:
        lines_to_adjust += ax.get_legend().get_lines()
    except AttributeError:
        pass
    mapping = dict()
    idx = 0
    for line in lines_to_adjust:
        oc = line.get_color()
        if oc not in mapping:
            mapping[oc] = COLORS[idx]
            idx += 1
            idx %= len(COLORS)
        #line.set_color('black')
        line.set_dashes(mapping[oc]['dash'])
        line.set_marker(mapping[oc]['marker'])
        line.set_markersize(MARKERSIZE)
        

def setFigLinesBW(fig):
    """
    Take each axes in the figure, and for each line in the axes, make the
    line viewable in black and white.
    """
    for ax in fig.get_axes():
        setAxLinesBW(ax)

apps = ['mm', 'nn', 'spmv', 'lbm']

sm_data = np.loadtxt('sm.txt')
bl_data = np.loadtxt('bl.txt')

fig, axes = plt.subplots(1, 2, figsize=(7, 2.5), dpi=300)
#gs = gridspec.GridSpec(nrows=1, ncols=2)
#axes = [ fig.add_subplot(gs[0, i]) for i in range(2) ]

# by sms
#fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
for app,idx in zip(apps, range(len(apps))):
    vec = sm_data[idx,:]
    sms = np.array([ x+1 for x in range(20) ])
    perf = vec.min() / vec
    axes[0].plot(sms, perf, label=app)
    axes[0].set_ylabel('Normalized Performance')
    axes[0].set_xlabel('SMs Used')
    axes[0].set_xticks(np.arange(0, 21, 5))
    axes[0].set_yticks(np.arange(0, 1.01, 0.2))
legend = axes[0].legend(loc='lower right')
#setFigLinesBW(fig)
#plt.xticks(range(0, 21))
#plt.tight_layout()
#fig.savefig('sm.png')

# by blocks
#fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
for app,idx in zip(apps, range(len(apps))):
    vec = bl_data[idx,:]
    sms = np.array([ x+1 for x in range(8) ])
    perf = vec.min() / vec
    axes[1].plot(sms, perf, label=app)
    axes[1].set_xlabel('Blocks Used')
    axes[1].set_xticks(range(9))
    axes[1].set_yticks(np.arange(0, 1.01, 0.2))
legend = axes[1].legend(loc='lower right')
setFigLinesBW(fig)
#plt.xticks(range(0, 9))
#plt.tight_layout()
#fig.savefig('bl.png')

plt.tight_layout()
plt.savefig('sm_bl.png')
#plt.show()

fig, axes = plt.subplots(1, 1, figsize=(5, 3), dpi=300)
for app,idx in zip(apps, range(len(apps))):
    vec = sm_data[idx,:]
    sms = np.array([ x+1 for x in range(20) ])
    perf = vec.min() / vec
    axes.plot(sms, perf, label=app)
    axes.set_ylabel('Normalized Performance')
    axes.set_xlabel('SMs Used')
    axes.set_xticks(np.arange(0, 21, 5))
    axes.set_yticks(np.arange(0, 1.01, 0.2))
legend = axes.legend(loc='lower right')
setFigLinesBW(fig)
plt.tight_layout()
plt.savefig('sm.png')

fig, axes = plt.subplots(1, 1, figsize=(5, 3), dpi=300)
for app,idx in zip(apps, range(len(apps))):
    vec = bl_data[idx,:]
    sms = np.array([ x+1 for x in range(8) ])
    perf = vec.min() / vec
    axes.plot(sms, perf, label=app)
    axes.set_ylabel('Normalized Performance')
    axes.set_xlabel('Blocks Used')
    axes.set_xticks(range(9))
    axes.set_yticks(np.arange(0, 1.01, 0.2))
legend = axes.legend(loc='lower right')
setFigLinesBW(fig)
plt.tight_layout()
plt.savefig('bl.png')


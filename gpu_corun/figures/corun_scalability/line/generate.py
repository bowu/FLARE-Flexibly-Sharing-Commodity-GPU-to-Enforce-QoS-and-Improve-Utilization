#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def setAxLinesBW(ax):
    """
    Take each Line2D in the axes, ax, and convert the line style to be 
    suitable for black and white viewing.
    """
    MARKERSIZE = 3

    COLORS = [
        {'marker': None, 'dash': (None,None)},
        {'marker': None, 'dash': [5,5]},
        {'marker': None, 'dash': [5,3,1,3]},
        {'marker': None, 'dash': [1,3]},
        {'marker': None, 'dash': [5,2,5,2,5,10]},
        {'marker': None, 'dash': [5,3,1,2,1,10]},
        {'marker': 'o', 'dash': (None,None)} #[1,2,1,10]}
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
        line.set_color('black')
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

apps = ['spmv(mm)', 'spmv(nn)', 'lbm(mm)', 'lbm(nn)']

sm_data = np.loadtxt('sm.txt')
bl_data = np.loadtxt('bl.txt')

# by sms
fig, ax = plt.subplots()
for app,idx in zip(apps, range(len(apps))):
    vec = sm_data[idx,:]
    sms = np.array([ x+1 for x in range(20) ])
    perf = np.nanmin(vec) / vec
    ax.plot(sms, perf, label=app)
legend = ax.legend(loc='lower right')
setFigLinesBW(fig)
plt.xticks(range(0, 21))
fig.savefig('sm.png')

# by blocks
fig, ax = plt.subplots()
for app,idx in zip(apps, range(len(apps))):
    vec = bl_data[idx,:]
    sms = np.array([ x+1 for x in range(8) ])
    perf = np.nanmin(vec) / vec
    ax.plot(sms, perf, label=app)
legend = ax.legend(loc='lower right')
setFigLinesBW(fig)
plt.xticks(range(0, 9))
fig.savefig('bl.png')

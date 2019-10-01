#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

apps = ['mm_lbm', 'mm_spmv', 'nn_lbm', 'nn_spmv']
qos_solo = [290.086, 262.965, 290.086, 262.965]

def plot_qos(app, ax):
    qos_data = np.loadtxt('qos_' + app + '.txt')
    qos_data[np.isnan(qos_data)] = max(np.nanmax(qos_data), 5 * solo)
    qos_data[7,19] = solo
    qos_norm = solo / qos_data
    ax.imshow(qos_norm)#, cmap='gray')
    ax.set_xticks(np.arange(0, 20, 1))
    ax.set_yticks(np.arange(0, 8, 1))
    ax.set_xticklabels(np.arange(1, 21, 1))
    ax.set_yticklabels(np.arange(1, 9, 1))
    #ax.set_xlabel('SMs Yielded')
    #ax.set_ylabel('Blocks Yielded')
    ax.invert_yaxis()
    ax.set_title('Latency', fontsize=14)

def plot_tpt(app, ax):
    tpt_data = np.loadtxt('tpt_' + app + '.txt')
    tpt_data[np.isnan(tpt_data)] = 0
    tpt_data[7,19] = np.max(tpt_data)
    tpt_norm = 1 - tpt_data
    ax.imshow(tpt_norm)#, cmap='gray')
    ax.set_xticks(np.arange(0, 20, 1))
    ax.set_yticks(np.arange(0, 8, 1))
    ax.set_xticklabels([ str(x) + '\n' for x in np.arange(1, 21, 1) ])
    ax.set_yticklabels(np.arange(1, 9, 1))
    ax.set_xlabel(app, fontsize=22)
    #ax.set_ylabel('Blocks Yielded')
    #ax.xaxis.tick_top()
    ax.invert_yaxis()
    ax.set_title('Throughput', fontsize=14)

widths = [1, 1, 1, 1, 0.3]
fig = plt.figure(figsize=(20, 5.2), dpi=300)
gs = gridspec.GridSpec(nrows=2, ncols=5, width_ratios=widths)
axes = [[ fig.add_subplot(gs[i, j]) for j in range(4) ] for i in range(2) ]
#plt.savefig('test.png')

#fig, axes = plt.subplots(2, 4, figsize=(18, 5), dpi=300)
for app,solo,idx in zip(apps, qos_solo, range(len(apps))):
    plot_qos(app, axes[0][idx])
    plot_tpt(app, axes[1][idx])
    #axes[1,idx].annotate(app, xy=(-10,0))
    #axes[2,idx].text(0, 0, app)

r_ax = fig.add_subplot(gs[:, -1])
r_ax.imshow(np.reshape(np.arange(0, 1, 0.1), (10,1)), interpolation='gaussian')
r_ax.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)
#r_ax.set_yticks([-0.5, 9.5])
#r_ax.text(-0.5, -0.5, )
r_ax.margins(5)
r_ax.set_title('High Latency\nLow Bandwidth', fontsize=16)
r_ax.set_xlabel('Low Latency\nHigh Bandwidth', fontsize=16)
#r_ax.set_yticklabels(['Low Latency\nHigh Bandwidth', 'High Latency\nLow Bandwidth'])

#fig.colorbar()
#plt.tight_layout(pad=1.5, w_pad=1, h_pad=4)
plt.tight_layout(h_pad=4.5)
plt.savefig('all.png')

#plt.show()

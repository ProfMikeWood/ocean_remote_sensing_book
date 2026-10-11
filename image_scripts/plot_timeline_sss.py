

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arrow
import matplotlib.dates as mdates

# define the landsat program dates
sat_dates = {'SMOS':(np.datetime64('2009-01-01'),np.datetime64('2026-01-01')),
             'Aquarius/SAC-D':(np.datetime64('2011-01-01'),np.datetime64('2015-12-31')),
             'SMAP':(np.datetime64('2015-01-01'),np.datetime64('2026-01-01'))}
sat_names = list(sat_dates.keys())

# make a figure
fig = plt.figure(figsize=(8, np.ceil(len(sat_names)/2)))

# plot the date boxes
for s in range(len(sat_names)):
    launch_date = sat_dates[sat_names[s]][0]
    decommission_date = sat_dates[sat_names[s]][1]
    sat_rect = Rectangle((launch_date,s*0.5),
                          decommission_date - launch_date,
                          0.25, facecolor='darkblue')
    plt.gca().add_patch(sat_rect)
    if s==0:
        plt.text(launch_date - np.timedelta64(4,'W'), s * 0.5 -0.05, sat_names[s], ha='left', va='bottom')
    else:
        if decommission_date<np.datetime64('2017-02-01'):
            plt.text(decommission_date + np.timedelta64(4,'W'), s*0.5+0.125, sat_names[s], ha='left', va='center')
        else:
            plt.text(launch_date - np.timedelta64(4,'W'), s*0.5+0.125, sat_names[s], ha='right', va='center')

# format the axes
plt.gca().set_xlim([np.datetime64('2005-02-01'),np.datetime64('2026-01-01')])
plt.gca().set_ylim([np.ceil(len(sat_names)/2)-0.5,-0.5])
myFmt = mdates.DateFormatter('%Y')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.gca().set_yticks([])
plt.title('Common Satellites for Passive Microwave SSS Retrievals')
plt.grid(linestyle='--', linewidth=0.5, alpha=0.5)

plt.savefig('../images/sss/timeline_sss.png',bbox_inches='tight')
plt.close(fig)




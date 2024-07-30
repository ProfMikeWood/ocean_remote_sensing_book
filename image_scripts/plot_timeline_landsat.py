

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arrow
import matplotlib.dates as mdates

# define the landsat program dates
sat_dates = {'Landsat 1':(np.datetime64('1972-01-01'),np.datetime64('1978-01-21')),
             'Landsat 2':(np.datetime64('1975-01-01'),np.datetime64('1982-01-21')),
             'Landsat 3':(np.datetime64('1978-01-01'),np.datetime64('1983-01-21')),
             'Landsat 4':(np.datetime64('1982-01-01'),np.datetime64('1993-01-21')),
             'Landsat 5':(np.datetime64('1984-01-01'),np.datetime64('2013-01-21')),
             'Landsat 7':(np.datetime64('1999-01-01'),np.datetime64('2022-01-21')),
             'Landsat 8':(np.datetime64('2013-01-01'),np.datetime64('2024-12-31')),
             'Landsat 9':(np.datetime64('2021-01-01'),np.datetime64('2024-12-31'))}
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
    if decommission_date<np.datetime64('2017-02-01'):
        plt.text(decommission_date + np.timedelta64(4,'W'), s*0.5+0.125, sat_names[s], ha='left', va='center')
    else:
        plt.text(launch_date - np.timedelta64(4,'W'), s*0.5+0.125, sat_names[s], ha='right', va='center')

# format the axes
plt.gca().set_xlim([np.datetime64('1972-02-01'),np.datetime64('2025-01-01')])
plt.gca().set_ylim([np.ceil(len(sat_names)/2),-0.25])
myFmt = mdates.DateFormatter('%Y')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.gca().set_yticks([])
plt.title('Landsat Program Satellites')
plt.grid(linestyle='--', linewidth=0.5, alpha=0.5)

plt.savefig('../images/timeline_landsat.png',bbox_inches='tight')
plt.close(fig)






import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arrow
import matplotlib.dates as mdates

# define the landsat program dates
sat_dates = {'AVHRR (NOAA-7 to NOAA-19)':(np.datetime64('1981-06-23'),np.datetime64('2026-01-01')),
             'ATSR (ERS-1/2)':(np.datetime64('1991-01-01'),np.datetime64('2011-12-01')),
             'VIIRS (Terra)':(np.datetime64('1999-12-18'),np.datetime64('2022-01-01')),
             'VIIRS (Aqua)':(np.datetime64('2002-05-04'),np.datetime64('2026-01-01')),
             'VIIRS (Suomi NPP)':(np.datetime64('2011-11-28'),np.datetime64('2026-01-01')),
             'VIIRS (NOAA-20 and -21)':(np.datetime64('2022-11-10'),np.datetime64('2026-01-01')),
             'TIRS (Landsat 8/9)':(np.datetime64('2013-01-01'),np.datetime64('2026-01-01'))}
sat_names = list(sat_dates.keys())

# make a figure
fig = plt.figure(figsize=(8, np.ceil(len(sat_names)/2)))

# plot the date boxes
for s in range(len(sat_names)):
    launch_date = sat_dates[sat_names[s]][0]
    decommission_date = sat_dates[sat_names[s]][1]
    sat_rect = Rectangle((launch_date,s*0.5),
                          decommission_date - launch_date,
                          0.25, facecolor='red')
    plt.gca().add_patch(sat_rect)
    if s==0:
        plt.text(launch_date - np.timedelta64(4,'W'), s * 0.5 -0.05, sat_names[s], ha='left', va='bottom')
    else:
        if decommission_date<np.datetime64('2017-02-01'):
            plt.text(decommission_date + np.timedelta64(4,'W'), s*0.5+0.125, sat_names[s], ha='left', va='center')
        else:
            plt.text(launch_date - np.timedelta64(4,'W'), s*0.5+0.125, sat_names[s], ha='right', va='center')

# format the axes
plt.gca().set_xlim([np.datetime64('1980-02-01'),np.datetime64('2026-01-01')])
plt.gca().set_ylim([np.ceil(len(sat_names)/2)-0.5,-0.5])
myFmt = mdates.DateFormatter('%Y')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.gca().set_yticks([])
plt.title('Common Thermal Infrared Sensors (Satellites) for SST')
plt.grid(linestyle='--', linewidth=0.5, alpha=0.5)

plt.savefig('../images/sst/timeline_sst.png',bbox_inches='tight')
plt.close(fig)




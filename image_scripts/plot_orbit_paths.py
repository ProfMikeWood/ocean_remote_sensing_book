

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arrow
from matplotlib.gridspec import GridSpec
import matplotlib.dates as mdates
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def create_prograde_points(inclination):
    # see here: https://space.stackexchange.com/questions/43414/analytical-expression-for-the-ground-track-of-the-international-space-station
    twopi = 2 * np.pi
    to_degs, to_rads = 180 / np.pi, np.pi / 180.

    omega = twopi / (92 * 60)  #
    omega_E = twopi / (23 * 3600 + 56 * 60 + 4)

    time = 60 * np.arange(92.)  # 100 minutes

    t0 = 1400  # arbitrary, you can fit this later
    inc = inclination
    const = 1.0  # arbitrary, you can fit this later

    x = np.cos(omega * (time - t0))
    y = np.sin(omega * (time - t0)) * np.cos(to_rads * inc)
    z = np.sin(omega * (time - t0)) * np.sin(to_rads * inc)

    lon = np.arctan2(y, x) - omega_E * (time - t0) + const
    lat = np.arcsin(z)

    lon = to_degs * lon
    lat = to_degs * lat

    # prograde points
    prograde_points = np.column_stack([lon, lat])
    for i in range(np.shape(prograde_points)[0] - 1):
        if prograde_points[i, 0] > 0 and prograde_points[i + 1, 0] < 0:
            index = i
    prograde_points_p = prograde_points[:index + 1, :]
    prograde_points_n = prograde_points[index + 1:, :]
    prograde_points_n[:, 0] += 360
    prograde_points = np.vstack([prograde_points_p,
                                 prograde_points_n])
    return(prograde_points)

def create_retrograde_points(inclination):
    # see here: https://space.stackexchange.com/questions/43414/analytical-expression-for-the-ground-track-of-the-international-space-station
    twopi = 2 * np.pi
    to_degs, to_rads = 180 / np.pi, np.pi / 180.

    omega = twopi / (92 * 60)  #
    omega_E = twopi / (23 * 3600 + 56 * 60 + 4)

    time = 60 * np.arange(92.)  # 100 minutes

    t0 = -1400  # arbitrary, you can fit this later
    inc = inclination
    const = 1.0  # arbitrary, you can fit this later

    x = np.cos(omega * (time - t0))
    y = np.sin(omega * (time - t0)) * np.cos(to_rads * inc)
    z = np.sin(omega * (time - t0)) * np.sin(to_rads * inc)

    lon = np.arctan2(y, x) - omega_E * (time - t0) + const
    lat = np.arcsin(z)

    lon = -1*to_degs * lon
    lat = to_degs * lat

    retrograde_points = np.column_stack([lon, lat])
    for i in range(np.shape(retrograde_points)[0] - 1):
        if retrograde_points[i+1, 0] > 0 and retrograde_points[i, 0] < 0:
            index = i
    retrograde_points_n = retrograde_points[:index + 1, :]
    retrograde_points_p = retrograde_points[index + 1:, :]
    retrograde_points_n[:, 0] += 360
    retrograde_points = np.vstack([retrograde_points_n,
                                 retrograde_points_p])
    return(retrograde_points)

def plot_orbits(prograde_points_51, retrograde_points_51,
                prograde_points_88, retrograde_points_88, projection_name):

    # subset
    if projection_name=='orthographic':
        fig = plt.figure(figsize=(8, 4))
        # proj = ccrs.Orthographic(central_longitude=50)
        # fig, axes = plt.subplots(
        #     1, 2, figsize=(8, 4),
        #     subplot_kw={'projection': proj},  # ,"aspect": 2
        #     gridspec_kw={'wspace': 0.03, 'hspace': 0.03, 'left': 0.11, 'right': 0.9, 'top': 0.95, 'bottom': 0.05},
        # )
        arrow_width = 10

    if projection_name=='platecarree':
        fig = plt.figure(figsize=(12,4))
        # proj = ccrs.PlateCarree()
        # fig, axes = plt.subplots(
        #     1, 2, figsize=(12, 4),
        #     subplot_kw={'projection': proj},  # ,"aspect": 2
        #     gridspec_kw={'wspace': 0.03, 'hspace': 0.03, 'left': 0.11, 'right': 0.9, 'top': 0.95, 'bottom': 0.05},
        # )
        arrow_width = 15

    gs = GridSpec(1,2, figure=fig)

    if projection_name=='orthographic':
        ax1 = fig.add_subplot(gs[:, 0], projection=ccrs.Orthographic(central_longitude=50))
    if projection_name=='platecarree':
        ax1 = fig.add_subplot(gs[:, 0], projection=ccrs.PlateCarree())

    ax1.add_feature(cfeature.LAND, zorder=0, facecolor='silver')
    ax1.coastlines()
    ax1.plot(prograde_points_51[:,0], prograde_points_51[:,1], linewidth=4, color='blue',
             transform=ccrs.PlateCarree())
    for i in range(10,90,10):
        ax1.arrow(prograde_points_51[i,0], prograde_points_51[i,1],
                  prograde_points_51[i+1,0]-prograde_points_51[i,0],
                  prograde_points_51[i+1,1]-prograde_points_51[i,1],
                  color='blue',transform=ccrs.PlateCarree(),
                  head_width=arrow_width, head_length=arrow_width)
    ax1.plot(prograde_points_88[:, 0], prograde_points_88[:, 1], linewidth=4, color='green',
             transform=ccrs.PlateCarree())
    for i in range(10,90,10):
        ax1.arrow(prograde_points_88[i,0], prograde_points_88[i,1],
                  prograde_points_88[i+1,0]-prograde_points_88[i,0],
                  prograde_points_88[i+1,1]-prograde_points_88[i,1],
                  color='green',transform=ccrs.PlateCarree(),
                  head_width=arrow_width, head_length=arrow_width)
    ax1.set_global()
    ax1.set_title('Prograde Orbit')

    if projection_name == 'orthographic':
        ax2 = fig.add_subplot(gs[:, 1], projection=ccrs.Orthographic(central_longitude=-30))
    if projection_name == 'platecarree':
        ax2 = fig.add_subplot(gs[:, 1], projection=ccrs.PlateCarree())

    ax2.add_feature(cfeature.LAND, zorder=0, facecolor='silver')
    ax2.coastlines()

    ax2.plot(retrograde_points_51[:, 0], retrograde_points_51[:, 1], linewidth=4, color='blue',
             transform=ccrs.PlateCarree())
    for i in range(10,90,10):
        ax2.arrow(retrograde_points_51[i,0], retrograde_points_51[i,1],
                  retrograde_points_51[i+1,0]-retrograde_points_51[i,0],
                  retrograde_points_51[i+1,1]-retrograde_points_51[i,1],
                  color='blue',transform=ccrs.PlateCarree(),
                  head_width=arrow_width, head_length=arrow_width)
    ax2.plot(retrograde_points_88[:, 0], retrograde_points_88[:, 1], linewidth=4, color='green',
             transform=ccrs.PlateCarree())
    for i in range(10,90,10):
        ax2.arrow(retrograde_points_88[i,0], retrograde_points_88[i,1],
                  retrograde_points_88[i+1,0]-retrograde_points_88[i,0],
                  retrograde_points_88[i+1,1]-retrograde_points_88[i,1],
                  color='green',transform=ccrs.PlateCarree(),
                  head_width=arrow_width, head_length=arrow_width)
    ax2.set_global()
    ax2.set_title('Retrograde Orbit')

    output_file = '../images/orbits_'+projection_name+'.png'
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)


prograde_points_51 = create_prograde_points(inclination = 51.6)
retrograde_points_51 = create_retrograde_points(inclination = 51.6)

prograde_points_88 = create_prograde_points(inclination = 88)
retrograde_points_88 = create_retrograde_points(inclination = 88)

# plt.plot(retrograde_points[:,0], retrograde_points[:,1])
# plt.show()

plot_orbits(prograde_points_51, retrograde_points_51,
            prograde_points_88, retrograde_points_88,
            'orthographic')
plot_orbits(prograde_points_51, retrograde_points_51,
            prograde_points_88, retrograde_points_88,
            'platecarree')

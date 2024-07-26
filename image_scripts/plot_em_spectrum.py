
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# https://stackoverflow.com/questions/44959955/matplotlib-color-under-curve-based-on-spectral-color
def wavelength_to_rgb(wavelength, gamma=0.8):
    ''' taken from http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
    This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    Additionally alpha value set to 0.5 outside range
    '''
    wavelength = float(wavelength)
    # if wavelength >= 380 and wavelength <= 750:
    A = 1.
    if wavelength < 380:
        wavelength = 380.
    if wavelength >750:
        wavelength = 750.
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R,G,B,A)

#######################################################################
# Plot metadata

# define some bounds for the plot
fig = plt.figure(figsize=(10,4))

min_x = -13.5
max_x = 2.5
min_y = -0.5
max_y = 3.5
tick_size = 0.2

#######################################################################
# Wavelength bar

wavelength_dict = {-13:'0.0001 nm',
                   -11:'0.01 nm',
                   -8:'10 nm',
                   -6:'1 $\mu$m',
                  -3:'1 mm',
                  -2:'1 cm',
                  0:'1 m',
                  2:'100 m'}

plt.plot([min_x,max_x],[max_y-1, max_y-1], 'k-', linewidth = 1)
plt.plot([min_x,max_x],[max_y-2, max_y-2], 'k-', linewidth = 1)

for tick_loc in list(wavelength_dict.keys()):
    plt.plot([tick_loc, tick_loc],[max_y-1, max_y-1+tick_size], 'k-')
    plt.text(tick_loc, max_y-0.9+tick_size, wavelength_dict[tick_loc], ha='center')

#######################################################################
# Wavelength classification bar

wavelength_bar_list = [-13.5,
                       -11,
                       -8,
                       np.log10(400e-9),
                       np.log10(700e-9),
                       -3,
                       2.5]

for bar_loc in wavelength_bar_list:
    plt.plot([bar_loc, bar_loc],[max_y-1, max_y-2], 'k-')


wavelength_bar_label_dict = {0:'Radio',
                             -4.5:'Infrared',
                             -7.2:'UV',
                             -9.6:'X-Ray',
                             -12.3:'Gamma'}

for tick_loc in list(wavelength_bar_label_dict.keys()):
    plt.text(tick_loc, max_y-1.9, wavelength_bar_label_dict[tick_loc], ha='center')



#######################################################################
# Visible bar

clim=(380,750)
norm = plt.Normalize(*clim)
wl = np.arange(clim[0],clim[1]+1,2)
colorlist = list(zip(norm(wl),[wavelength_to_rgb(w) for w in wl]))
spectralmap = LinearSegmentedColormap.from_list("spectrum", colorlist)

x = np.linspace(min_x+1,max_x-3)
y = np.array([0,1])
X, Y = np.meshgrid(x,y)

min_wavelength = 380
max_wavlength = 751

W = (X-np.min(X))/(np.max(X)-np.min(X))*(max_wavlength-min_wavelength)+min_wavelength
C = plt.contourf(X, Y, W, 500, cmap=spectralmap)
# plt.colorbar(C)

w = (x-np.min(x))/(np.max(x)-np.min(x))*(max_wavlength-min_wavelength)+min_wavelength
index_400 = np.argmin(np.abs(w-400))
index_500 = np.argmin(np.abs(w-500))
index_600 = np.argmin(np.abs(w-600))
index_700 = np.argmin(np.abs(w-700))

# plot ticks on visible colorbar
plt.plot([x[index_400],x[index_400]],[0,1],'k-', linewidth = 1)
plt.plot([x[index_500],x[index_500]],[0,1],'k-', linewidth = 1)
plt.plot([x[index_600],x[index_600]],[0,1],'k-', linewidth = 1)
plt.plot([x[index_700],x[index_700]],[0,1],'k-', linewidth = 1)
plt.text(x[index_400],-0.1,'400 nm', va='top', ha='center')
plt.text(x[index_500],-0.1,'500 nm', va='top', ha='center')
plt.text(x[index_600],-0.1,'600 nm', va='top', ha='center')
plt.text(x[index_700],-0.1,'700 nm', va='top', ha='center')

# make an outline
plt.plot([np.min(x), np.min(x)],[0,1],'k-', linewidth = 1)
plt.plot([np.max(x), np.max(x)],[0,1],'k-', linewidth = 1)
plt.plot([np.min(x), np.max(x)],[0,0],'k-', linewidth = 1)
plt.plot([np.min(x), np.max(x)],[1,1],'k-', linewidth = 1)

# title
plt.text(np.mean(x), 1.05, 'Visible', ha='center', va='bottom')

#######################################################################
# Draw lines between main bar and visible bar

plt.plot([np.log10(400e-9), np.min(x)],[max_y-2,1],'k-', linewidth = 1)
plt.plot([np.log10(700e-9), np.max(x)],[max_y-2,1],'k-', linewidth = 1)

#######################################################################
# Final Formatting

plt.gca().set_xlim([min_x, max_x])
plt.gca().set_ylim([min_y, max_y])
plt.axis('off')

output_file = '/Users/mike/Documents/Teaching/Github/ocean_remote_sensing_book/images/em_spectrum.png'
plt.savefig(output_file, bbox_inches='tight')
plt.close(fig)
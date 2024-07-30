
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc4

band_images = {}

bands = np.arange(1,12).tolist()
bands.pop(bands.index(8))

# read in the data
ds = nc4.Dataset('../data/monterey_landsat.nc')
for band in bands:
    band_images[band] = ds.variables['band_'+str(band)][:, :]
ds.close()

# make an RGB array
RGB = np.stack([band_images[4], band_images[3], band_images[2]], axis=-1)

# clip high and low values to show colors in range
minval = np.percentile(RGB, 5)
maxval = np.percentile(RGB, 70)
RGB = np.clip(RGB, minval, maxval)

# rescale so that numbers are 8 bit
RGB = ((RGB - minval) / (maxval - minval)) * 255
RGB = RGB.astype(int)

# make a figure
fig =plt.figure(figsize=(10,8), dpi=300)

plt.subplot(3,4,1)
plt.imshow(RGB)
plt.title('"Natural Color"')
plt.xticks([])
plt.yticks([])

for band in bands:
    img = band_images[band]
    if band<10:
        minval = np.percentile(img, 5)
        maxval = np.percentile(img, 70)
        img = np.clip(img, minval, maxval)

    if band<8:
        plt.subplot(3, 4, band+1)
        plt.imshow(img, cmap='Greys_r')
        # plt.axis('off')
    else:
        plt.subplot(3, 4, band)
        plt.imshow(img, cmap='Greys_r')
        # plt.axis('off')
    if band==1:
        plt.title('Band '+str(band)+' (Violet/Blue)')
    elif band==2:
        plt.title('Band '+str(band)+' (Blue)')
    elif band==3:
        plt.title('Band '+str(band)+' (Green)')
    elif band==4:
        plt.title('Band '+str(band)+' (Red)')
    elif band==5:
        plt.title('Band '+str(band)+' (NIR)')
    elif band==6:
        plt.title('Band '+str(band)+' (SWIR 1)')
    elif band==7:
        plt.title('Band '+str(band)+' (SWIR 2)')
    elif band==9:
        plt.title('Band '+str(band)+' (SWIR 3)')
    elif band==10:
        plt.title('Band '+str(band)+' (TIR 1)')
    elif band==11:
        plt.title('Band '+str(band)+' (TIR 2)')
    else:
        plt.title('Band '+str(band))

    plt.xticks([])
    plt.yticks([])

# plt.title('"Natural Color" Image of Mount Taranaki')
plt.savefig('../images/monterey_landsat_bands.png', dpi=300, bbox_inches='tight')
plt.close(fig)






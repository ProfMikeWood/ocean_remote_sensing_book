# Lab 3: Remote Sensing Indices

In this lab, we will investigate difference indices using Landsat data. As a case study, we will examine seasonal differences in snow cover and vegetation in Yosemite National Park which had a particularly wet winter in 2023. In particular, we will compare difference indices for snow and vegetation. This is a decidedly terrestrial example in a set of notes otherwise focused on marine applications, but it provides a convenient approach to examine two types of normalized-difference indices in the same location.

## Step 1: Data Gathering and Preparation

### Download Landsat Data and Generate Natural Color Layers

Begin by downloading the following two Landsat scenes from EarthExplorer: 

|**LC08_L2SP_042034_20230414_20230428_02_T1**|**LC09_L2SP_042034_20230828_20230830_02_T1**|
|---|---|
|Band 2 (blue)|Band 2 (blue)|
|Band 3 (green)|Band 3 (green)|
|Band 4 (red)|Band 4 (red)|
|Band 5 (NIR)|Band 5 (NIR)|
|Band 6 (SWIR)|Band 6 (SWIR)|

When searching on EarthExplorer, you can find these scenes by selecting the Landsat 8/9 product from the Collection 2 Level 2 products on the Data Sets tab, and then inputting the identifiers above in the **Landsat Product Identifier L2** entry on the Additional Criteria tab.

```{note}
It’s recommended to download these layers into individual folders inside your directory for `Lab 3/Raster Files`. For example, create two folders named `LC09_L2SP_042034_20230828` and `LC08_L2SP_042034_20230414` and store the individual band files there according to their file names. Then, load these files in QGIS into the same folder structure using the "Group" feature.
```

Once your download is complete, merge the Red, Green, and Blue bands into a “Natural Color” image following the steps in the previous lab. Save the new image in the folders you’ve created above.  

```{figure} ../images/labs/lab03/layer_organization.png
---
width: 100%
name: lab03-layer-organization
---
Screenshot of the layer organization from the spring and summer scenes from 2023.
```

### Create a Shapefile for the Boundary of Yosemite National Park

Next, download the National Park boundary shapefile by navigating to the Department of the Interior website [HERE](https://public-nps.opendata.arcgis.com/search?q=boundaries%20yosemite) and selecting the Shapefile download option from the **Yosemite National Park - Administrative Boundary - Open Data** source. Save the shapefile into your Lab 3/Vector Layers folder.

Unzip the file and load into QGIS. Then, save to a new individual shapefile, reprojecting into the same projection as the Landsat layers (EPSG: 32611). 

## Step 2: Calculating Environmental Indices

### Calculate NDSI and NDVI using the Raster Calculator tool

Using the data you downloaded for the two different time periods, generate layers for the Normalized Difference Snow Index (NDSI) and the Normalized Difference Vegetation Index (NDVI). The two indices are defined as follows:

$$
NDSI=  \frac{Green-SWIR}{Green+SWIR} =  \frac{Band_3-Band_6}{Band_3+Band_6}
$$

and

$$
NDVI=  \frac{NIR-Red}{NIR+Red}=  \frac{Band_5-Band_4}{Band_5+Band_4}
$$

However, we need to be careful about the calculations because the pixel values stored in the Landsat files do not directly correspond to the surface reflectances as described in the following note:

```{note}
According to the [Landsat Collection 2 Level 2 documentation](https://www.usgs.gov/landsat-missions/landsat-collection-2-surface-reflectance) the digital numbers (DN) in Landsat scenes are converted to surface reflectances (SR) with the following formula:

$$
SR = (DN \times m) +b
$$

where $m=0.0000275$ and $b=-0.2$
```

With a little algebra, we can see that NDSI as computed with Landsat pixels is computed as:

$$
\begin{align*}
NDSI=  \frac{Green-SWIR}{Green+SWIR} &=  \frac{[(Band_3 \times m) +b]-[(Band_6 \times m) +b]}{[(Band_3 \times m) +b]+[(Band_6 \times m) +b]} \\
& = \frac{(Band_3 \times m)-(Band_6 \times m)}{(Band_3 \times m) +(Band_6 \times m) +2b}
\end{align*}
$$

An analogous formula is used for NDVI with the same values for $m$ and $b$. 

Using the formula above, generate these layers using the Raster Calculator tool available from the Raster drop-down. To run the calculations, use the buttons for the calculation procedure (e.g. the buttons for the parentheses and the division symbol) and the layer names for the variables. See the screenshot below for an example.

```{figure} ../images/labs/lab03/raster_calculation.png
---
width: 100%
name: lab03-map-example
---
Screenshot of the Raster Calculator tool showing the calculation of an NDSI layer.
```

As you create each layer, save them with the suffix NDSI or NDVI, similar to the steps for your naming convention of the Natural Color images generated above. 

### Format the Index Layers with Diverging Color Map

A diverging color map uses one color for negative values and one color for positive values. Set the bounds for your difference index layers to be the same magnitude in the positive direction as in the negative direction and choose an appropriate color map for your data. For example, your NDVI map may use a brown color for negative values, a green color for positive values, and span the values -0.5 to 0.5. 

```{figure} ../images/labs/lab03/ndvi_example.png
---
width: 100%
name: lab03-ndvi-example
---
Screenshot of the NDVI layer computed and formatted for the spring scene.
```

#### &#129300; Consider this!
Take a look at the values of NDSI and NDVI between the two different seasons. Where do you see high values? How about low values?

## Step 3: Calculating Raster Statistics

### Sample NDSI and NDVI in the Yosemite National Park area

Next, we'll investigate mean values within Yosemite National Park. Begin by sampling your NDSI and NDVI layers with your reprojected boundary for the park. To access the sampling tool, open the Processing Toolbox (View → Panels → Processing Toolbox), expand the GRASS → Vector menu, and select the v.rast.stats tool. Select your index layer (NDSI or NDVI) as your raster layer and your Yosemite National Park polygon as your vector layer. Then, input the layer type (NDSI or NDVI) into the column suffix box. If you intend to save your statistics for later use, you can save the output as a new file. For this lab, it is sufficient to use a temporary layer and copy the contents manually. When you're all set, hit Run!

When the sampling is complete, the statistics are available in the Attribute Table of the new layer. Open up the Attributes of the new layer and record the values in a table as follows:

|   | Spring NDVI | Spring NDSI | Summer NDVI | Summer NDSI |
|---|-------------|-------------|-------------|-------------|
|Average| -0.0762 | " | " | " |
|Median| 0.0480 | " | " | " |

Be sure to fill in this table, computing the statistics for each layer.


## Step 4: Masking Rasters and Calculating Threshold Statistics

### Create an NDSI Threshold Mask 

It is often convenient to "mask" a raster layer using another raster layer. For example, you may choose to remove the clouds from an image before calculating time series or statistics. In this problem, we will see how to generate a mask using the Raster Calculation tool. Specifically, we will create a threshold mask for our NDSI layers by identifying pixels in the NDSI field which are greater than 0.5. Note that this is not a universal definition of snow but is useful as an approximation in this lab. Using this mask, we can count the pixels which are covered in snow and determine the total snow-covered area in the park.

Open the Raster Calculator tool and create a Boolean layer by identifying pixels above the given threshold. You can store your layer to your Lab 3 folder or just use a temporary file to retrieve the statistics (next step). The following screenshot shows an example calculation:

```{figure} ../images/labs/lab03/snow_mask_calculation.png
---
width: 100%
name: lab03-snow-mask-calc
---
Screenshot of the mask calculation in the Raster Calculation tool.
```

This new layer will have a value of 1 where the threshold indicates snow is present and a value of 0 where there is no snow.

```{figure} ../images/labs/lab03/snow_mask.png
---
width: 100%
name: lab03-snow-mask
---
Screenshot of a snow mask computed with NDSI.
```

### Calculate the Total Snow-Covered Area 

Using the NDSI mask generated in the previous step, next we will calculate the total snow-covered area by determining the number of cells that have met our snow threshold and then converting this number to an area.

Following the steps above for computing statistics, find the sum of all pixel values within the Yosemite National Park polygon that have met the NDSI threshold. Then, compute the total snow-covered area using the nominal resolution of 30 m for each Landsat pixel, i.e.


$$
A_{\text{snow}}​=N_{\text{snow pixels}} ​(30 \text{ m} \times 30 \text{ m})= N_{\text{snow pixels}}​\times 900 \text{ m}^2
$$

Record your values for both scenes and compare with a partner.


## Group Activity: Generating a Snow Cover Time Series as a Group

In the final component of this lab, we will pool our collective resources to generate a time series of snow cover for Yosemite National Park.

Each person in the lab will be responsible for finding 2 images in a given 3-month span. At the end of this lab, we will have a 1-year time series to analyze the changes in Yosemite National Park after the wet winter of 2023 showing the seasonal cycle of changes.
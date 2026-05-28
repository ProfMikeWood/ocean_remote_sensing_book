# Lab 3: Remote Sensing Indices

In this lab, we will investigate the impact of the wet winter of 2023 on the snowpack and vegetation in Yosemite National Park. In particular, we will compare difference indices for snow and vegetation. 

## Step 1: Data Gathering and Preparation

### Download Landsat Data and Load Natural Color Layers

Begin by downloading the following Landsat scenes from Earth Explorer: **LC09_L2SP_042034_20230828_20230828** and **LC08_L2SP_042034_20230414_20230428**. For each of these scenes, download the files for bands 2, 3, 4, 5, and 6.

Note: It’s recommended to download these layers into individual folders inside your directory for `Lab 3/Raster Files`. For example, create two folders named `LC09_L2SP_042034_20230828` and `LC08_L2SP_042034_20230414` and store the individual band files there according to their file names.

Once your download is complete, merge the Red, Green, and Blue bands into a “Natural Color” image following the steps in the previous lab. Save the new image in the folders you’ve created above.  

### Create a Shapefile for the Boundary of Yosemite National Park

Next, download the National Park boundary shapefile from the Department of the Interior website at [HERE](https://public-nps.opendata.arcgis.com/search?q=boundaries%20yosemite). Save the shapefile into your Lab 3/Vector Layers folder.

Unzip the file and load into QGIS. Then, save to a new individual shapefile, reprojecting into the 32611 projection. 

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

Generate these layers using the Raster Calculator tool in QGIS. As you create each layer, save them with the suffix NDSI or NDVI, similar to the steps for your naming convention of the Natural Color images generated above. 

### Format the Index Layers with Divergent Color Map

A divergent color map uses one color for negative values and one value for positive values. Set the bounds for your difference index to be the same magnitude in the positive direction as in the negative direction and choose an appropriate color map for your data. For example, your NDVI map may use a brown color for negative values, a green color for positive values, and span the values -1 to 1.

## Step 3: Calculating Raster Statistics

### Sample NDSI and NDVI in the Yosemite National Park area

Next, sample your NDSI and NDVI layers with your reprojected boundary for Yosemite National Park. To access the sampling tools, find the raster statistics tool by opening the Processing Toolbox and selecting the v.rast.stats tool from the GRASS → Vector menu. Select your NDSI or NDVI layer as your raster layer and your Yosemite National Park polygon as your vector layer.
- If you intend to save your statistics: save the output as a new file.
- If not: use a temporary layer and copy the contents manually.
When the sampling is complete, the statistics are available in the Attribute Table of the new layer.

## Step 4: Masking Rasters and Calculating Threshold Statistics

### Create an NDSI Threshold Mask 

It is often convenient to mask a raster layer using another raster layer. For example, you may choose to remove the clouds from an image before calculating timeseries or statistics. In this problem, we will create a threshold mask for our NDSI layers by identifying points in the NDSI field which are greater than equal to 0.5. 

Open the Raster Calculator tool and create a Boolean layer by identifying points above the given threshold. You can store your layer to your Lab 3 folder or just use a temporary file to retrieve the statistics (next step).

### Calculate the Total Snow-Covered Area 

Using the NDSI mask generated in the previous step, next we will calculate the total snow-covered area by determining the number of cells that have met our snow threshold and then converting this number to an area.

Following the steps above, find the sum of all points within the Yosemite National Park polygon that have met the NDSI threshold. Then, compute the total snow-covered area using the nominal resolution of 30 m for each Landsat imagery cell. (Hint: your units should be in m$^2$.)


### Group Activity: Generating a Snow Cover Time Series as a Group

In the final component of this lab, we will pool our collective resources to generate a time series of snow cover for Yosemite National Park.

Each person in the lab will be responsible for finding 2 images in a given 3-month span. At the end of this lab, we will have a 1-year timeseries to analyze the changes in Yosemite National Park after the wet winter of 2023.




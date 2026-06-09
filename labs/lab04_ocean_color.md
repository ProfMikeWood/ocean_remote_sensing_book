# Lab 4: Ocean Color in QGIS

In this lab, we will explore NASA’s Ocean Color Products. A list of all levels of ocean color data is provided on NASA's Ocean Biology DAAC [HERE](https://oceandata.sci.gsfc.nasa.gov/directdataaccess/)

**Learning Objectives:**
By the end of this lab, you should be able to
- Find and access NASA ocean color data
- Perform calculations with raster data
- Sample raster data using point vector layers

## Motivation

NASA’s ocean-color record began in 1978 with CZCS. After a major gap following CZCS, additional ocean-color missions, including OCTS, SeaWiFS, MODIS, and others, have supported a largely continuous multi-mission record since the late 1990s. In this lab, we'll explore how to obtain, visualize, and interpret seasonal changes using this record.

## Getting Started

As for previous labs in QGIS, start up QGIS and begin a New Project. In your file system, create the following folder structure in your Lab folder:

```
Labs
 |-Lab 1
 |-Lab 2
 |-Lab 3
 |-Lab 4
   |-Lab 4 Ocean Color.qgz
   |-Raster Layers
   |-Vector Layers
```

## Part 1: Data Gathering and Preparation

### Download MODIS Chlorophyll-a Data

To get a feel for ocean color data, we will look at Level-3 chlorophyll-a data. To explore the available data, navigate to the Level 3 & 4 Browser at https://oceancolor.gsfc.nasa.gov/l3/. This link is different from the DAAC link above. It provides access to fewer datasets, but it has a convenient interface for downloading data.

In this browser, choose the following options:
- Instrument: Aqua-MODIS
- Product: Chlorophyll Concentration
- Period: Monthly
- Resolution: 4 km
- Dates: 2015-01-01 to 2015-12-31

To download the files for the query, select the Extract or Download Data option. Be sure the **Mapped** checkbox is selected and click Download. This will bring you to a page with links to 12 files – download all 12 into your `Lab 4/Raster Files` folder by copying the link and pasting it into your browser's URL bar (in a separate window).

## Part 2: Visualizing Ocean Color Data

### Visualize the data with a linear color map

When your download is complete, load in one of the monthly files as a Raster File. In the pop-up box, choose the `chlor_a` layer. Then, in the Symbology tab of the Properties menu, change the Render Type to be **Singleband pseudocolor** and change the colormap to use the **turbo** colormap. 

It is likely that the colormap will be stretched to include very large values - it’s recommended that you visualize the data in a range of approximately 0.01-20 mg/m$^3$. Change the bounds of your colormap accordingly.

```{figure} ../images/labs/lab04/linear_ocean_color.png
---
height: 300px
name: global-ocean-color-linear
---
Screenshot of the QGIS with an ocean color layer.
```

#### 🤔 Consider the following
Explore the global map of chlorophyll-a and consider the following questions:
- Where do we find exceptionally high values of chlorophyll-a?
- Where do we find very low values?
- Where are we missing data? Why?

### Convert data to visualize in a logarithmic scale

As you may have noticed, chlorophyll-a values in the global ocean span several orders of magnitude from about 0.01 mg/m$^3$ up to something on the order of 100 mg/m$^3$. As a result, global chlorophyll-a maps are often displayed on a logarithmic scale. Unfortunately, QGIS does not have a built-in method to scale colors logarithmically. However, we can use the **Raster Calculator** to generate our own converted values to generate this type of visualization.

Open the Raster Calculator and use the `log10` expression to compute the compute the base-10 logarithm of the chlorophyll-a data. Store your calculation in a new layer with the suffix `_log`. 

```{figure} ../images/labs/lab04/raster_calculator.png
---
height: 400px
name: raster-calculator
---
Screenshot of the QGIS Raster Calculator when computing logarithmic values of chlorophyll-a.
```

Once your layer is complete and loaded into the QGIS canvas, change the colormap to turbo again. Next, we would like to stretch the colors to reflect 0.01-20 mg/m$^3$ range we used previously. However, our data reflects the logarithm of the data value, not the data values themselves. In this case, what values should be used to present the data in the 0.01-20 mg/m$^3$ range?

#### 🤔 Consider the following
- How does this new view of the data change your perception of the global distribution of chlorophyll-a?
- Are there any new features you notice that were not immediately perceptible when the map was stretched linearly?

## Part 3: Computing a Time Series of Chlorophyll-a

### Create a point shapefile layer at a sample location

To generate a time series of chlorophyll-a, we will create a point shapefile layer that will be used to sample our raster data. Begin by selecting the New Shapefile Layer Tool and create a Point layer in the same coordinate system as the MODIS data (EPSG: 4326). Add a new field for Location and delete the default id field. Save the file as **MODIS Sample Point** in your Lab 4/Vector Layers folder. Click OK to create the layer. 


```{figure} ../images/labs/lab04/modis_sample_point.png
---
height: 400px
name: modis-sample-point
---
Screenshot of the QGIS vector layer creation tool.
```

Edit the shapefile and add a point on the map near Monterey Bay and enter `Monterey Bay` in the Location field. Once you’ve added a point to the map, you can always adjust it using the Vertex Tool. Use this tool to move your point near **-122.08°E** and **36.7°N** in Monterey Bay. Then, save the layer by clicking on the yellow pencil.


### Install the Point sampling tool plugin

QGIS, as an open source project, has a huge number of available Plugins that are created by QGIS users around the world. You can access these plugins from the Plugins → Manage and Install Plugins from the top menu bar. Open this tool, search for the **Point sampling tool** and install it. Once you’ve installed the plugin, you’ll find it on your QGIS toolbar. (If it doesn’t show up, ensure the Plugins toolbar is visible under the View → Toolbars menu.)

### Add all 12 of your chlorophyll-a layers to the map

In the next step, we will sample the 12 monthly chlorophyll-a fields we downloaded using the Point sampling tool. Add all files to the map and adjust their values to be in the range 0.01-20 mg/m$^3$ with turbo colormap (no need to convert the data using the logarithmic function). Then, group the layers into a subgroup by selecting all of the layers in the Layers panel, right-clicking, and choosing Group Selected. Name the group *Monthly Chlorophyll-a Data* and then rename each layer with a 3-letter prefix for the month (e.g. Jan, Feb, etc).

```{figure} ../images/labs/lab04/monthly_modis_layers.png
---
height: 300px
name: monthly-modis-layers
---
Screenshot of the QGIS with monthly chlorophyll-a layers renamed with monthly prefixes.
```

#### 🤔 Consider the following

Shuffle through the monthly data layers and consider how the chlorophyll-a concentrations change from month to month. When do we see the largest values in chlorophyll-a?

### Use the plugin to sample the monthly fields

Open the sampling tool and choose your MODIS Sample Point layer for vector layer, , and select all 12 monthly raster layers, Jan–Dec, as the layers to sample. Then, save your shapefile in your Lab 4/Vector Layers folder with the file name **MODIS Sample Point – 2015**. Be sure to select `.shp` as your output type.


#### 🤔 Consider the following
Open up the **Attribute Table** of your new layer - you should see the chlorophyll-a estimates for each month. When do we see the highest values for chlorophyll-a in 2015? Does this align with your visual assessment of the files? Why might these patterns have occurred?

**Try it for yourself:** Choose another location in the ocean and sample the shapefile at a new point. Store the output as a `csv` this time.

## Part 4: Assessing the Estimates of Remotely-Sensed Chlorophyll-a

In this step of the lab, we will compare our remotely-sensed chlorophyll-a estimates with real *in situ* data.

### Download in situ 2015 chlorophyll-a values

MODIS Level-3 data provides estimates of chlorophyll-a in the surface of the ocean. However, it is always good to compare with real *in situ* data to determine whether there are any temporal or spatial biases in the data. To assess the estimates in the monthly products, we will compare with real measurements from the global ocean.

Download the [WOD Chlorophyll 2015.csv](https://github.com/ProfMikeWood/ocean_remote_sensing_book/raw/refs/heads/main/labs/data/lab04/WOD%20Chlorophyll%202015.csv) provided with this lab (right-click the link and choose Save Link As...). This file contains all measurements of chlorophyll-a near the ocean surface from the NCEI [World Ocean Database](https://www.ncei.noaa.gov/products/world-ocean-database) during 2015 – an online collection of in situ oceanographic measurements from around the globe. The file for this lab was generated by querying the database for all available values in 2015 in the top 1m of the ocean.

After your download is complete, load in the file as a Delimited Text Layer using the Layer → Add Layer menu. When the file is loaded, the X field and Y fields should be populated with the Longitude and Latitude columns of the `csv` file.

### Subsetting the Vector Layer by Month

In the next steps, we would like to compare the *in situ* data to the satellite-derived data but there’s a catch – the *in situ* data is for the entire year while the satellite data represents one month. To compare data within the same month, open the attribute table for the WOD chlorophyll-a data and select the **Select/filter features using form** tool. Make a query to choose only those values which pertain to particular month (e.g. Month = 7) and choose Select Features. Then, save the new subsetted layer as a point shapefile layer with the suffix for the month (e.g. Jul) by right-clicking on the layer name and choosing **Export → Save Selected Features As...**.

### Sampling the Month Layer on the Raster Data

Next, we will again use the **Point sampling tool** to sample the MODIS raster data corresponding to the monthly subset of the *in situ* data. Save the file as a comma separated value (`csv`) file called `MODIS Chlorophyll 2015 Jul.csv` into a folder in your Lab 4 folder. This will create a single column of chlorophyll-a values from the monthly dataset at the same points where the *in situ* samples were taken.

```{figure} ../images/labs/lab04/in_situ_point_comparison.png
---
height: 300px
name: in-situ-point-comparison
---
Screenshot of the QGIS point sampling tool to gather satellite-derived estimates of chlorophyll-a at in situ sampling locations.
```

For comparison, also export the `WOD Chlorophyll 2015 Jul.shp` layer as a `csv` file into the same folder by right-clicking on the `WOD Chlorophyll 2015 Jul.shp`, choosing **Export →  Save Features As**, and selecting options to output the data as `csv` file. The rows in this file will correspond to the rows in the previous `csv` file for one-to-one comparison.

### Compute the Root Mean Square Error of MODIS Satellite Data vs In Situ Data
In the final step of this lab part, compute the root mean square error (RMSE) between the in situ data and the corresponding ocean color estimates. The root mean square error is given by 

$$
RMSE= \sqrt{\sum_{i=1}^N \frac{(O_i - E_i)^2}{N}}
$$

Where $N$ is the number of observations,  $O_i$ is the $i$th in situ observation, and $E_i$ is the $i$th estimated value from MODIS.

To complete this calculation, you can write some code in a Jupyter notebook or you can use built-in Excel functions - choose whichever option you are more comfortable with! We will begin using Python for analysis in the following lab.

#### 🤔 Consider the following
After you complete your calculation, consider what would lead to differences between observed values and satellite-derived values? List at least two different reasons why the two datasets may differ.

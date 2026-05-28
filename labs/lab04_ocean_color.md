# Lab 4: Ocean Color in QGIS

In this lab, we will explore NASA’s Ocean Color Products. A list of all levels of ocean color data is provided at:
https://oceandata.sci.gsfc.nasa.gov/directdataaccess/

## Motivation


## Part 1: Data Gathering and Preparation

### Download MODIS Chlorophyll-a Data

To get a feel for ocean color data, we will look at Level-3 Chlorophyll-a Data. To explore the available data, navigate to the Level 3 & 4 Browser at https://oceancolor.gsfc.nasa.gov/l3/

In this browser, choose the following options:
- Instrument: Aqua-MODIS
- Product: Chlorophyll Concentration
- Period: Monthly
- Resolution: 4 km
- Dates: 2015-01-01 to 2015-12-31

To download the files for the query, select the Extract or Download Data option. Be sure the “Mapped” checkbox is selected and click Download. This will bring you to a page with links to 12 files – download all 12 into your Lab 4/Raster Files folder by copying the link and pasting it into your browser url bar (in a separate window).

## Step 2: Visualizing Ocean Color Data

### Examine the data with a linear color map

When your download is complete, open up QGIS and start at new project for Lab 5. Load in one of the monthly files and change the colormap to use the turbo colormap.

It is likely that the colormap will be stretch to include very large values – it’s recommended that you examine the data in a range of approximately 0.01-20 mg/m3. Change the bounds of your colormap accordingly. 

Explore the data map and consider the following questions:
- Where do we find exceptionally high values of chlorophyll-a?
- What do we find very low values?
- Where are we missing data? Why?

### Converting data to visualize in a log scale

As you may have noticed, chlorophyll-a values in the global ocean span several orders of magnitude from about 0.01 mg/m3 up to 100 mg/m3 or more. As a result, global chlorophyll-a maps are often displayed on a logarithmic scale. Unfortunately, QGIS does not have a built-in method to scales colors logarithmically. However, we can use the **Raster Calculator** to generate our own converted values to generate this type of visualization.

Open the Raster Calculator and use the log10 expression to compute the log of the chlorophyll-a data. Store your calculation in a new layer with the suffix *_log*. 

Once your layer is complete and loaded into the QGIS Canvas, change the colormap to turbo again. Next, we would like to stretch the colors to reflect 0.01-20 mg/m3 range we used previously. However, our data reflects the logarithm of the data value, not the data values themselves. In this case, what values should be used to present the data in the 0.01-20 mg/m3 range?

Consider the following questions:
- How does this new view of the data change your perception of the global distribution of chlorophyll-a?
- Are there any new features you notice that were not immediately perceptible when the map was stretched linearly?

## Part 3: Computing timeseries of Ocean Color Data

### Create a point shapefile layer at a sample location

To generate a timeseries of Chlorophyll-a, we will create a point shapefile layer that will be used to sample our raster data. Begin by selecting the New Shapefile Layer Tool and create a Point layer in the same coordinate system as the MODIS data. Add a new field for Location and delete the default id field. Save the file as MODIS Sample Point in your Lab 4/Vector Layers folder. Click OK to create the layer. 

Edit the shapefile and add a point on the map near Monterey Bay and enter Monterey Bay in the Location field. Once you’ve added a point to the map, you can always adjust it using the Vertex Tool. Use this tool to move your point to -122.08°E and 36.7°N near Monterey Bay. Then, save the layer by clicking on the yellow pencil.


### Install the Point sampling tool plugin

QGIS, as an open source project, has a huge number of available Plugins that are created by QGIS users around the work. You can access these plugins from the Plugins → Manage and Install Plugins for the top menu bar. Open this tool, search for the Point sampling tool and install it. Once you’ve installed the plugin, you’ll find it on your QGIS toolbar. (If it doesn’t show up, ensure the Plugins toolbar is visible under the View → Toolbars menu.)

### Add all 12 of your Chlorophyll-a fields to the map

In the next step, we will sample the 12 monthly chlorophyll-a fields we downloaded using the Point sampling tool. Add all files to the map and adjust their values to be in the range 0.01-20 mg/m3 with turbo colormap (no need to convert the data to using the logarithmic function). Then, group the layers into a subgroup and rename each layer with a 3-letter prefix for the month (e.g. Jan, Feb, etc).

Shuffling through the data, when do we see the largest values in chlorophyll-a?

### Use the plugin to sample the monthly fields

Open the sampling tool and choose your MODIS Sample Point layer for vector layer and select all of your fields (Jan – Dec) for the Layers. Then, save your shapefile in your Lab 5/Shapefiles folder with the file name MODIS Sample Point – 2015. Be sure to select .shp as your output type.

When do we see the highest values for chlorophyll-a in 2015? Why might this have occurred?

**Try it for yourself:**

choose another location in the ocean and sample the shapefile at a new point. Store the output as a csv and submit on Canvas. We will look at plots of everyone’s timeseries together.

## Part 4: Assessing the accuracy of monthly chlorophyll-a products

### Download in situ 2015 Chlorophyll-a values

MODIS Level-3 data provides estimates of chlorophyll-a in the surface of the ocean. However, it is always good to compare with real in situ data to determine whether there are any temporal or spatial biases in the data. To assess the estimates in the monthly products, we will compare with real measurements from the global ocean.

Begin by downloading the **WOD Chlorophyll 2015.csv** file from Canvas. This file contains all measurements of chlorophyll-a from the World Ocean Database during 2015 – an online collection of in situ oceanographic measurements from around the globe. The file for this lab was generated by querying the database for all available values in 2015 in the top 1m of the ocean.

After your download is complete, load in the file as a Delimited Text Layer.

### Subsetting the Vector Layer by Month

In the next steps, we would like to compare the in situ data to the satellite-derived data but there’s a catch – the in situ data is for the entire year while the satellite data represents one month. To compare data within the same month, open the attribute table for the WOD Chlorophyll Data and make a query to choose only those values which pertain to particular month (e.g. Month = 7). Save the new layer as a point shapefile layer with the suffix for the month (e.g. Jul).

### Sampling the Month Layer on the Raster Data

Next, use the point layer for the monthly subset of WOD Chlorophyll to sample the MODIS raster data corresponding to the month you chose. Save the file as a comma separated value (csv) file called MODIS Chlorophyll 2015 [month] into a folder in your Lab 5 folder called CSV Layers. This will create a single column of chlorophyll values from the monthly dataset.

For comparison, also export the WOD Chlorophyll 2015 [month] layer as a csv into the same folder.

### Compute the Root Mean Square Error of MODIS Satellite Data vs In Situ Data
Finally, compute the root mean standard error in the csv files using Python. The root mean square error is given by 

$$
RMSE= \sqrt{\sum_{i=1}^N \frac{(O_i - E_i)^2}{N}}
$$

Where $N$ is the number of observations,  $O_i$ is the $i$th in situ observation, and $E_i$ is the $i$th estimated value from MODIS.

To complete this calculation, open the Jupyter notebook from Canvas and complete the cells.

**Consider the following question:**
What would lead to differences between observed values and satellite-derived values? List at least two different reasons why the two datasets may differ.

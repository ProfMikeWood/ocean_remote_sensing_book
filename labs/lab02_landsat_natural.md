# Lab 2: “Natural Color” Landsat Layers

**Learning Objectives:**
By the end of this lab, you should be able to
- Identify and obtain Landsat imagery in a time and region of interest
- Add raster layers to a map and modify their appearance
- Identify source projections for vectors and reproject them to new coordinate systems
- Mask raster layers with shapefiles

## Motivation

When making maps, we often want to use two or more raster files from separate sources. In oceanography, a common scenario is that we have some information in a raster over the ocean and other information in a different raster file over the land - for example, perhaps we want to show the bathymetry of a given region relative to different towns or land features. See, for example, the following screenshot from Google Earth:

```{figure} ../images/labs/lab02/monterey_bay_google_earth.png
---
height: 400px
name: lab02-map-example
---
Screenshot of the bathymetry and natural color imagery of the Monterey Bay area shown on Google Earth.
```


## Part 1: Accessing Individual Landsat Scenes

For the land imagery this lab, we'll explore how to download Landsat scenes from EarthExplorer and create “Natural Color” images in QGIS. The [EarthExplorer](https://earthexplorer.usgs.gov/) portal, hosted by the US Geological Survey, is a convenient tool to search for available Landsat imagery (as well as data from a variety of other satellites). Navigate to the portal use the link above and sign in with your EROS credentials. 

### Identifying Landsat Images for your Region of Interest

The EarthExplorer portal is formatter with four panels to narrow down your data search.

#### Step 1: Search Criteria

The first tab for the search criteria is designed to identify the location and time for your query. For this lab, start by choosing a location in the Monterey Bay area (the "Region of Interest? or "ROI"). The easiest way to identify a location for your data search is to simply click on the map to add a location. If the location is not ideal, delete it and add a new one. If desired, you can also choose a timespan of interest (the default is all available data for your source). Once you're happy with the query, click Data Sets to continue.

```{figure} ../images/labs/lab02/monterey_bay_earthdata.png
---
height: 400px
name: earthdata-query
---
Screenshot of the the Monterey Bay query on Earthdata.
```

#### Step 2: Data Sets

On the data sets tab, you'll find that there are lots of different options available for different types of data. Scroll down through the list of sensors and expand the **Landsat** menu and **choose Landsat Collection 2 Level 2** for imagery. For recent imagery, choose the set pertaining to **Landsat 8-9 OLI/TIRS CS L2**. Then click Results to view the options (you can skip the Additional Criteria tab).


#### Step 3: Downloading Data

On the results page, you'll get a list of available Landsat images that span the Monterey Bay area. Scroll through the available options and consider the following question:
- Is the image from Landsat 8 or Landsat 9?
- What is the approximate temporay spacing between the images?
- Are there clouds in the image? Hint: you can get a closer look at the image by clicking on the thumbnail of the image

After browsing the images, choose a relatively cloud-free image of your ROI. Once you have identified an image, download the Blue, Green, and Red Bands for your scene by clicking on the Download button (grey disk with the green arrow). Since we're working with Landsat 8 and 9, these bands are B2, B3, and B4. For Landsat 4-5, these would be bands B1, B2, and B3.

To download the individual bands, click on the bands in the expanded menu for the Level-2 Surface Reflectance Bands:

```{figure} ../images/labs/lab02/earthdata_download.png
---
height: 400px
name: lab02-map-example
---
Screenshot of the bathymetry and natural color imagery of the Monterey Bay area shown on Google Earth.
```




## Part 2: Creating a "Natural Color" Landsat Image in QGIS

To generate a “Natural Color” image in QGIS, it’s necessary to “merge” the Red, Green, and Blue Landsat bands into a single image and then render the image accordingly.

Step 1: Merge the Image in QGIS
•	From the Raster drop-down, choose Miscellaneous -> Merge
•	Click the option to “Place each input file into a separate band”
•	In the Input Layers tab, choose to Add Files… and add the files for the red, green, and blue bands
•	Save the file as a tif with the suffix “Natural”

Step 2: Assign Bands to the Correct Colors
•	Ensure the red band is assigned to band 3, green to band 2, and blue to band 1
o	QGIS stores images in RGB format but Landsat labels bands by their position on the EM spectrum
•	It is often helpful to scale the colors to the same numerical extent

Step 3: Render the Image
•	Adjust the contract, brightness, saturation, and gamma levels to visualize the image as desired.

## Part 3: Masking Raster Layers with Vectors



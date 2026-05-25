# Lab 2: “Natural Color” Landsat Layers

**Learning Objectives:**
By the end of this lab, you should be able to
- Identify and obtain Landsat imagery in a time and region of interest
- Add raster layers to a map and modify their appearance
- Identify source projections for vectors and reproject them to new coordinate systems
- Mask raster layers with shapefiles

## Motivation

When making maps, we often want to use two or more raster files from separate sources. In oceanography, a common scenario is that we have some information in a raster over the ocean and other information in a different raster file over the land - for example, perhaps we want to show the bathymetry of a given region relative to different towns or land features. See, for example, the following screenshot from Google Earth:



## Part 1: Accessing Individual Landsat Scenes

In this lab, we'll explore how 

This handout outlines how to download Landsat scenes from Earth Explorer and create “Natural Color” images in QGIS.

The EarthExplorer portal, hosted by the US Geological Survey, is a convenient tool to search for available Landsat imagery (as well as data from a variety of other satellites).

To begin, register for an account on the EROS Registration System. The accounts are free – just sign up with your institutional email. Once you’ve created an account, sign in and navigate to the EarthExplorer portal.

Identifying Landsat Images for your Region of Interest

Step 1: Search Criteria
•	Choose a location for your Region of Interest (ROI)
o	The easiest way to identify a location for your data search is to simply click on the map to add a location. If the location is not ideal, delete it and add a new one.
o	If desired, choose a timespan of interest (default is all available data for your source)
•	Click Data Sets to continue

Step 2: Data Sets
•	Scroll down through the list of sensors and expand the Landsat menu
o	Choose Landsat Collection 2 Level 1 for imagery
	For recent imagery, choose the set pertaining to Landsat 8 or 9 
•	Click Results to view the options

Step 3: Downloading Data
•	Browse data and search for a cloud-free image of your ROI
•	Once you have identified an image, download the Blue, Green, and Red Bands pertaining to the Landsat satellite you chose
o	For Landsat 7-9, these bands are B2, B3, and B4
o	For Landsat 4-5, these bands are B1, B2, and B3
o	For more information, see the USGS website
•	To download the individual bands, click on the bands grey download square and expand the menu for bands.






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



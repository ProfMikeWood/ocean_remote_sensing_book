# Registering For Accounts

The notebooks in this "book" use satellite data from a variety of sources. Much of this data will be downloaded from public repositories that require a log in credentials. Register for credentials on the following systems.

## USGS Earth Resources Observation and Science (EROS) Center

The [EarthExplorer](https://earthexplorer.usgs.gov/ portal, hosted by the US Geological Survey, is a convenient tool to search for available Landsat imagery (as well as data from a variety of other satellites). To access data from this tool, register for an account on the EROS Registration System. The accounts are free – just sign up with your institutional email [HERE](https://ers.cr.usgs.gov/register). 

## NASA Earthdata

NASA provides access to a wide range of satellite data through [Earthdata](https://www.earthdata.nasa.gov/). To access these resources, create an account [HERE](https://urs.earthdata.nasa.gov/users/new). 

```{warning}
When setting up your credentials for these accounts, do not use a password that you use for other senstive applications. This password will be saved in profile file on your machine. 
```

### Setting Up a netrc File on MacOS
On a Mac, open up the **Terminal** from the Utilities menu. To use the automatic Earthdata download tools from PODAAC, the first thing we will need to do is store our Earthdata credentials in our home directory. You can find this directory on a Mac using the following command in the terminal:

```
echo $HOME
```

Once you have identified your home directory, create a `.netrc` file in that directory using the
following command:

```
open -a TextEdit .netrc
```

Inside this file, add the following contents:

```
machine urs.earthdata.nasa.gov
    login <your username>
    password <your password>
```

Note that this the second two lines should be indented by 4 spaces and the `<>` symbols should not be present around your username and password.

Finally, be sure this file cannot be read by anyone else using the following command:

```
chmod 700 .netrc
```

### Setting Up a netrc File on Windows
On Windows, open up the **Windows Powershell** from the Start menu. To use the download tools, the first thing we will need to do is store our Earthdata credentials in our home directory. You can find this directory on a Windows using the following command in your shell:

```
echo $HOME.
```

You can be sure you are in your home directory by typing `pwd` and ensuring that the path matches the output of the previous command. Once you have identified your home directory, create a `netrc` file in that directory. Create this file by typing the following command in your shell:

```
notepad.exe .netrc
```

Inside this file, add the following contents:
```
machine urs.earthdata.nasa.gov
    login <your username>
    password <your password>
```

Note that this the second two lines should be indented by 4 spaces and the `<>` symbols should not be present around your username and password.

Next type `dir` and ensure you can see your `.netrc` file in the list of files. If it has a `.txt` extension, rename it to remove the extension with the following command:

```
mv .netrc.txt .netrc
```

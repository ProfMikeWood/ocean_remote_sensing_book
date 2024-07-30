
# be sure to use the py6s environment for this component
from Py6S import *
import numpy as np
import netCDF4 as nc4
import os

def calculate_transmission_data(folder, wavelengths):

    if 'molecular_transmission.nc' not in os.listdir(folder):

        water_vapor = []
        co2 = []
        oxygen = []
        ozone = []
        n2o = []
        ch4 = []
        rayleigh = []
        total_gases = []

        for wavelength in wavelengths.tolist():
            s = SixS()
            s.atmos_profile = AtmosProfile.Tropical
            s.wavelength = Wavelength(wavelength)
            s.run()

            water_vapor.append(s.outputs.trans['water'].downward)
            co2.append(s.outputs.trans['co2'].downward)
            oxygen.append(s.outputs.trans['oxygen'].downward)
            ozone.append(s.outputs.trans['ozone'].downward)
            n2o.append(s.outputs.trans['n2o'].downward)
            ch4.append(s.outputs.trans['ch4'].downward)
            rayleigh.append(s.outputs.trans['rayleigh_scattering'].downward)
            total_gases.append(s.outputs.trans['global_gas'].downward)

        ds = nc4.Dataset(os.path.join(folder,'Molecular Transmission.nc'),'w')
        ds.createDimension('wavelength',len(wavelengths))

        w = ds.createVariable('wavelength','f4',('wavelength'))
        w[:] = wavelengths

        h2o = ds.createVariable('water_vapor', 'f4', ('wavelength'))
        h2o[:] = np.array(water_vapor)

        co2v = ds.createVariable('carbon_dioxide', 'f4', ('wavelength'))
        co2v[:] = np.array(co2)

        o2 = ds.createVariable('oxygen', 'f4', ('wavelength'))
        o2[:] = np.array(oxygen)

        o3 = ds.createVariable('ozone', 'f4', ('wavelength'))
        o3[:] = np.array(ozone)

        n2ov = ds.createVariable('nitrous_oxide', 'f4', ('wavelength'))
        n2ov[:] = np.array(n2o)

        ch4v = ds.createVariable('methane', 'f4', ('wavelength'))
        ch4v[:] = np.array(ch4)

        ray = ds.createVariable('rayleigh_scattering', 'f4', ('wavelength'))
        ray[:] = np.array(rayleigh)

        gas = ds.createVariable('global_gas', 'f4', ('wavelength'))
        gas[:] = np.array(total_gases)

        ds.close()

    ds = nc4.Dataset(os.path.join(folder, 'Molecular Transmission.nc'))
    water_vapor = ds.variables['water_vapor'][:]
    co2 = ds.variables['carbon_dioxide'][:]
    oxygen = ds.variables['oxygen'][:]
    ozone = ds.variables['ozone'][:]
    n2o = ds.variables['nitrous_oxide'][:]
    ch4 = ds.variables['methane'][:]
    rayleigh = ds.variables['rayleigh_scattering'][:]
    gas = ds.variables['global_gas'][:]
    ds.close()

    return(water_vapor, co2, oxygen, ozone, n2o, ch4, rayleigh, gas)

folder = '../data'


wavelengths = np.arange(0.2,4.00,0.01)

# print('Calculating Molecular Constituent Radiation')
h2o, co2, o2, o3, n2o, ch4, rayleigh, gas = calculate_transmission_data(folder, wavelengths)


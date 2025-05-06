import xarray as xr
import numpy as np
import pandas as pd

# TODO read data from era5
filepath = "era5_folder/era5_Data.nc"
ds = xr.open_dataset(filepath)
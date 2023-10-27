import xarray as xr
import numpy as np
import os


def main():
    target = "/glade/work/dmeidan/WACCM_forcast_files/Daphne-emission_x3/"
    file_loc = "/glade/work/jinmuluo/CanadianFire2023/EmissionInventory/"
    t_start = '2023-01-01'
    t_end = "2023-12-31"
    he_date = "2023-06-06"
    var = "bb"

    finn = [f for f in os.listdir(target) if os.path.isfile(os.path.join(target, f))]

    dsCMIP = xr.open_dataset("/glade/p/cesmdata/cseg/inputdata/atm/cam/chem/emis/CMIP6_emissions_2010climo/emissions-cmip6_bc_a4_bb_surface_2010climo_0.9x1.25_c20170322.nc")

    for f in finn:
        ds = xr.open_dataset(os.path.join(target, f))
        ds2 = ds.sel(time=slice(t_start, t_end))
        ds.close()

        higest_emi = np.zeros((len(ds2.time), len(ds2.lat), len(ds2.lon)))
        #zero_emi = np.zeros((len(ds2.time), len(ds2.lat), len(ds2.lon))) 
        higest_emi[:] = ds2[var].sel(time=he_date)
        ds2[var].values = higest_emi
       
        # into monthly dataset
        ds2 = ds2.sel(time=ds2.time.dt.day == 15)
        ds2['time'] = dsCMIP['time']
        ds2['date'] = dsCMIP['date']

        ds2.to_netcdf(path=os.path.join(file_loc, f), mode="w", format="NETCDF3_64BIT") 
        ds2.close() 
        print("Coverting", f, "successfully!")


if __name__ == "__main__":
   main()

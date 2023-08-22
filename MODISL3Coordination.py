import numpy as np

# m, the radius of the idealized sphere representing the Earth;
R = 6371007.181

# m, the height and width of each MODIS tile in the projection plane;
T = 1111950

# m, the western limit of the projection plane;
xmin = -20015109

# m, the northern limit of the projection plane;
ymax = 10007555

# m, the actual size of a “500-m” MODIS sinusoidal grid cell.
w = 463.31271653

def modis_500m_coor(i, j, H, V):
    # i, j are the row and column of in MODIS tile H, V
    # Return the lat, lon in radiant
    x = (j + 0.5) * w + H*T + xmin 
    y = ymax - (i + 0.5)*w -V*T
    lat = y/R
    lon = x/(R*np.cos(lat))
    
    return lat, lon
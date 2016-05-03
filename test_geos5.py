#!/usr/bin/env python
 
import sys
import numpy as np
import netCDF4 as nc4
import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap
 
rootgrp = nc4.Dataset('c1440_NR.inst01hr_3d_T_Cv.20060918_0900z.nc4', 'r')
print "rootgrp.variables['T'].shape", rootgrp.variables['T'].shape
 
# read global air temperature for all levels
print 'Reading T...',; sys.stdout.flush()
T = rootgrp.variables['T'][0,:,:,:]
print 'done.'; sys.stdout.flush()
print 'T.shape:', T.shape
 
# min/max
print 'min(T): %.4f' % np.min(T)
print 'max(T): %.4f' % np.max(T)
 
# set up cylindrical map
m = Basemap(projection='cyl',llcrnrlat=-90, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180,resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawmapboundary()
 
# plot contour
level = 71 # surface
X = np.arange(-180.0, 180.0, .5)
Y = np.arange(-90.0, 90.1, .5) # 90 is the last element
cp = plt.contour(X, Y, T[level,:,:], 20, zorder=2)
plt.clabel(cp, inline=1, fontsize=9)
plt.title('Air temperature at the surface')
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:23:47 2015

@author: jacopo
"""
import json
from pprint import pprint
import h5py

#
# TO DOs
#
# 1. Add the reference to Sensors ontology


# ACOS LITE file
f = h5py.File('ACOSv3.4r02_L3_20100101_000000_20130515_000000.h5', libver='earliest')

xco2 = f['xco2']
lon = f['lon']
lat = f['lat']
lon_bnds = f['lon_bnds']
lat_bnds = f['lat_bnds']

xco2_set = xco2[0,0,0,:]



geo = {"type" : "FeatureCollection",
           "features" : [
               {
                "type" : "Feature",
                "geometry" : {"type": "Point",
                              "coordinates" : [lat[0], lon[0]]
                              }
                },
               {
                "type" : "Feature",
                "geometry" : {
                "type" : "polygon",
                "coordinates" : [[lon_bnds[0,0], lat_bnds[0,0]], [lon_bnds[0,0], 
                              lat_bnds[0,1]], [lon_bnds[0,1], lat_bnds[0,0]], 
                             [lon_bnds[0,1], lat_bnds[0,1]] ]
                             },
               "properties": {
                   "xco2" : xco2_set[12]        
               }
              }               
        ]
      }


#with open('geo.json', 'w') as outfile:
    #json.dump(geo, outfile)

# print a JSON with the quantity of xco2 for the given geometry
pprint(json.dumps(geo))


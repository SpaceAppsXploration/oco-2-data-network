# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:23:47 2015

@author: jacopo
"""
import json
from pprint import pprint

# http://docs.h5py.org/en/latest/high/file.html
import h5py

#
# Links:
# https://confluence.slac.stanford.edu/display/PSDM/How+to+access+HDF5+data+from+Python#HowtoaccessHDF5datafromPython-GetinformationaboutHDF5item
#
# TO DOs
#
# 1. Add the reference to Sensors ontology


# OCO-2 file in the same directory
f = h5py.File('oco2_L2StdGL_02675a_150101_B6000r_150411233719.h5', 'r', libver='earliest')

for item in f.keys():
    #if item == 'Metadata':
    #    for i in item:
    #        print(f['Metadata'])
    print("name: " + str(item) + "  |  " + "type: " + str(f[item]))

print('-----------------------------------------------------------------')

for i in f['AerosolResults']:
    print(f['AerosolResults'][i][0])
    print(f['AerosolResults'][i][1])

print('-----------------------------------------------------------------')

for i in f['Metadata']:
    print(f['Metadata']['ProducerAgency'])

f.close()

# print a JSON with the quantity of xco2 for the given geometry
#print(json.dumps(geo, indent=4))


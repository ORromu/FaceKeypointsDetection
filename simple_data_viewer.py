# -*- coding: utf-8 -*-
"""
Description
-----------
Super simple script viewing the images with their annotation on the unprocessed
dataset.
 
Else
----
@author: Romuald Ait Bachir
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os 
import utils as us

data_path = ['./data/300W/01_Indoor', './data/300W/02_Outdoor'] 

# Simply reading the two subdatasets: Indoor and Outdoor
all_files_indoor = [os.path.join(data_path[0], f) for f in os.listdir(data_path[0]) if os.path.isfile(os.path.join(data_path[0], f))]
all_files_outdoor = [os.path.join(data_path[1], f) for f in os.listdir(data_path[1]) if os.path.isfile(os.path.join(data_path[1], f))]

# Associating the annotation to the image and making a total pairs list
indoor_pair = us.make_pair_list(all_files_indoor)
outdoor_pair = us.make_pair_list(all_files_outdoor)

pairs_in_out = indoor_pair + outdoor_pair

#%%
index_to_display = 433 #Choose between 0 and 599

image = plt.imread(pairs_in_out[index_to_display][0])
points = us.read_pts(pairs_in_out[index_to_display][1])

plt.figure(1)
plt.imshow(image)
plt.scatter(points[:,0], points[:,1])
plt.show()
     
        
        
        
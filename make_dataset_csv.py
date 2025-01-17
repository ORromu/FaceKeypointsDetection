# -*- coding: utf-8 -*-
"""
Description
-----------
Simple script making a .csv file to be later read as a dataset. Consists in the 
pairing of the image with its corresponding annotation. 

The dataset is obtained by downloading the part 1 of the 300W dataset. 

Else
----
@author: Romuald Ait Bachir
"""

import os 
import utils as us
import random as rd
import pandas as pd

train_ratio = 0.8
random_seed = 42
rd.seed(random_seed)

data_path = ['./data/300W/01_Indoor', './data/300W/02_Outdoor'] 

#%%
# Simply reading the two subdatasets: Indoor and Outdoor
all_files_indoor = [os.path.join(data_path[0], f) for f in os.listdir(data_path[0]) if os.path.isfile(os.path.join(data_path[0], f))]
all_files_outdoor = [os.path.join(data_path[1], f) for f in os.listdir(data_path[1]) if os.path.isfile(os.path.join(data_path[1], f))]

# Associating the annotation to the image and making a total pairs list
indoor_pair = us.make_pair_list(all_files_indoor)
outdoor_pair = us.make_pair_list(all_files_outdoor)

# Setting the train/validation elements on each subdataset.
# Parameters
N_indoor = len(indoor_pair)
N_outdoor = len(outdoor_pair) 

probabilities = [train_ratio, 1 - train_ratio]  # Probabilities for 0 and 1

# Generate the list
indoor_rand = rd.choices(["Train", "Validation"], probabilities, k = N_indoor)
outdoor_rand = rd.choices(["Train", "Validation"], probabilities, k = N_outdoor)

indoor_pair = [(indoor_pair[k][0], indoor_pair[k][1], indoor_rand[k]) for k in range(N_indoor)]
outdoor_pair = [(outdoor_pair[k][0], outdoor_pair[k][1], outdoor_rand[k]) for k in range(N_outdoor)]

pairs_in_out = indoor_pair + outdoor_pair

# Simply converting into a Dataframe
# Column names:
columns = ['Image path', 'Annotation path', 'Set']

# Convert to DataFrame
df = pd.DataFrame(pairs_in_out, columns = columns)
df = df.sample(frac=1, random_state = random_seed) # Simply shuffling so that indoor and outdoor are mixed
df.sort_values(by = 'Set', inplace = True)
df.reset_index(drop = True, inplace = True)

# Next we save it as a .csv 
df.to_csv("./data/dataset.csv")


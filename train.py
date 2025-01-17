# -*- coding: utf-8 -*-
"""
Description
-----------
Script used to train the model.

Else
----
@author: Romuald Ait Bachir
"""

# Simple test of the dataset.
import dataset as ds

train_dataset = ds.FaceDataset("./data/dataset.csv", None, "Train")

## Checking the correct length 
# print(len(train_dataset))

## Checking the correct information in the dataframe loaded
# print(train_dataset.pairs)

## Checking the element at idx = 0
# print(train_dataset[0])
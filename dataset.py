# -*- coding: utf-8 -*-
"""
Description
-----------
Definition of the pytorch dataset with the preprocessing and the data augmentation

Else
----
@author: Romuald Ait Bachir
"""

import numpy as np
import pandas as pd

from torch.utils.data import Dataset

import utils as us

class FaceDataset(Dataset):
    """
    Description
    -----------
    Implementation of a torch.utils.data.Dataset for the Face Dataset.
    
    Attributes
    ----------
    path : str
        Path to the .csv dataset.
    transf : ???
        TODO
    split : str
        Choose between "Train" and "Validation".
    pairs : pandas.DataFrame
        pandas.DataFrame with 3 columns (Image path, Annotation path, Set) containing the path
        to the image, to the annotation and the split.
    """
    
    def __init__(self, csv_path, transf, split):
        """
        Description
        -----------
        Constructor of the ModisDatasetB class.
        
        Parameters
        ----------
        csv_path : str
            Typical path: "./data/dataset.csv"
        transf : ???
            Transformation object applying the data preprocessing.
        split : str, optional
            Choose between "Train", "Test", "Val". The default is 'Train'
        """

        self.path = csv_path
        df = pd.read_csv(self.path, sep = ',')
        df.drop(columns=df.columns[0], axis=1, inplace=True)
        
        self.transf = transf
        self.split = split
        
        # Choosing only the split wanted
        df = df.loc[df['Set'] == self.split]
        self.pairs = df        
        
    def __len__(self):
        """
        Description
        -----------
        Method returning the number of element inside the Dataset.

        Returns
        -------
        len : int
            Length of the dataset.
        """
        
        return len(self.pairs)
    
    
    def __getitem__(self, idx):
        """ 
        Description
        -----------
        Method returning the image and the corresponding annotation 
        located at line idx inside the dataset located in self.pairs.
        
        Parameters
        ----------
        idx : int
            Index of the line read
        
        Returns
        -------
        image : np.array
            Image containing a face. Shape: (3, N, M)
        annot : np.array
            Corresponding annotation
        """
        
        line_read = self.pairs.iloc[idx]
        image = 0
        annot = 0
        
        # Need to add the code readinig the data ## simple data viewer. 
        # and adding the preprocessing.
        
        return image, annot
        
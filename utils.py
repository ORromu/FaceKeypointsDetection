# -*- coding: utf-8 -*-
"""
Description
-----------
Utilitary file containing some function's definitions.
 
Else
----
@author: Romuald Ait Bachir
"""

import numpy as np
import os

def make_pair_list(img_pts_list: list) -> list:
    """
    TODO 

    Parameters
    ----------
    img_pts_list : list
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """
    pair_list = []
    while len(img_pts_list) > 0:
        # Taking the file, finding the corresponding one and removing it from the initial list 
        file1 = img_pts_list[0]
        img_pts_list.remove(file1)
        for i in range(len(img_pts_list)):
            if img_pts_list[i].split(os.sep)[-1][:-4] == file1.split(os.sep)[-1][:-4]:
                file2 = img_pts_list[i]
                img_pts_list.remove(file2)
                break
            # else case shouldnt happen
            
        # Adding the tuple into the list of tuples. 
        if file1.endswith('png'):
            pair_list.append((file1, file2))
        else: 
            pair_list.append((file2, file1))
            
    return pair_list

def read_pts(filename):
    """
    TODO

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return np.loadtxt(filename, comments=("version:", "n_points:", "{", "}"))

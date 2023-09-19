from sklearn.base import BaseEstimator, TransformerMixin


import pandas as pd 
import os 
import numpy as np 
import sys 
from src.logger import logging


class Data_Cleaning(BaseEstimator , TransformerMixin):
    
    
    
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        # take a copy of the data
        logging.info('1-- First Pipeline Started: Clean and Replace the X with np.nan ---')
        # Replace All X with np.nan 
        X['FirstTimeHomebuyer'] = X['FirstTimeHomebuyer'].replace('X', np.nan) 
        X['MSA'] = X['MSA'].replace('X    ', np.nan)
        X['PPM'] = X['PPM'].replace('X', np.nan)
        X['PropertyType'] = X['PropertyType'].replace('X ', np.nan)
        X['NumBorrowers'] = X['NumBorrowers'].replace('X ', np.nan)
        # Dealing With date features 
        return X 

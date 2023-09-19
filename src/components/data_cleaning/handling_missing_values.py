from sklearn.base import BaseEstimator, TransformerMixin


import pandas as pd 
import os 
import numpy as np 
import sys 

from src.logger import logging

class Handling_Missing_Values(BaseEstimator , TransformerMixin):
    
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        
        logging.info('3---Handling Missing Values Started: Detect and Handle Missing Data --')

        # Hnadling missing categorial values  
        X['SellerName'] = X['SellerName'].fillna(X['SellerName'].dropna().mode().values[0])
        X['FirstTimeHomebuyer'] = X['FirstTimeHomebuyer'].fillna(X['FirstTimeHomebuyer'].dropna().mode().values[0])
        X['MSA'] = X['MSA'].fillna(X['MSA'].dropna().mode().values[0])
        X['PPM'] = X['PPM'].fillna(X['PPM'].dropna().mode().values[0])
        X['NumBorrowers'] = X['NumBorrowers'].fillna(X['NumBorrowers'].dropna().mode().values[0])
        X['PropertyType'] = X['PropertyType'].fillna(X['PropertyType'].dropna().mode().values[0])
        
        # Converting the type of the column to int
        X['NumBorrowers'] = X['NumBorrowers'].astype('int64')
        
        return X

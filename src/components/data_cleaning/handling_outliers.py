
from sklearn.base import BaseEstimator, TransformerMixin


import pandas as pd 
import os 
import numpy as np 
import sys 

from src.logger import logging

class Handling_Outliers(BaseEstimator, TransformerMixin):
    def handle_outlier(self, col):
        sorted_col = sorted(col)
        Q1, Q3 = col.quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower = Q1 - (1.5 * IQR)
        upper = Q3 + (1.5 * IQR)
        return lower, upper

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        logging.info('2-- Handling Outliers Started: Detect and Treat Outliers --')
        # Handle outliers in 'Units', 'OrigInterestRate', and 'OrigUPB' columns
        for col_name in ['Units', 'OrigInterestRate', 'OrigUPB' ]:
            lower, upper = self.handle_outlier(X[col_name])
            X[col_name] = X[col_name].apply(lambda x: lower if x < lower else (upper if x > upper else x))
        
        return X
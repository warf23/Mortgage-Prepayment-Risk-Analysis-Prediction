
from sklearn.base import BaseEstimator, TransformerMixin


import pandas as pd 
import os 
import numpy as np 
import sys 
from src.logger import logging


class Drop_Unused_Features(BaseEstimator , TransformerMixin):
    
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        logging.info('4-- Dropping Unused Features First Starting ::: \n %s --- ', ', '.join(['MSA', 'PostalCode', 'PropertyState', 'ServicerName', 'SellerName', 'LoanSeqNum', 'ProductType']))
        return X.drop(['MSA' ,'PostalCode' , 'PropertyState' , 'ServicerName' , 'SellerName' , 'LoanSeqNum' , 'ProductType'  ], axis=1 , inplace=True)
        
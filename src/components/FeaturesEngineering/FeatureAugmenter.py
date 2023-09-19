

import pandas as pd 
import os 
import numpy as np 
import sys 

from sklearn.base import BaseEstimator, TransformerMixin      # Base classes for custom transformers

from src.exception import CustomException 
from src.logger import logging

from datetime import datetime 

class AddNewColumnsTransformer(BaseEstimator, TransformerMixin):
    
    try :
        def calculate_num_months(self, start_date, end_date):
            start =   datetime.strptime(start_date, "%Y%m")
            end   =   datetime.strptime(end_date, "%Y%m")
            num_months = (end.year - start.year) * 12 + (end.month - start.month)
            return num_months
        
        def determine_credit_range(self, credit_score):
            credit_ranges = {
                range(0, 650): 'Poor',
                range(650, 700): 'Fair',
                range(700, 750): 'Good',
                range(750, 900): 'Excellent'
            }
            for score_range, credit_range in credit_ranges.items():
                if credit_score in score_range:
                    return credit_range
            return 'Unknown'
        
        def determine_ltv_range(self, ltv):
            ltv_ranges = {
                range(0, 25): 'LOW',
                range(25, 50): 'MEDIUM',
                range(50, 1000): 'HIGH'
            }
            for ltv_range, ltv_category in ltv_ranges.items():
                if ltv in ltv_range:
                    return ltv_category
            return 'Unknown'


        def fit(self, X, y=None):
            return self

        def transform(self, X):
            

            # Change type of FirstPaymentDate and MaturityDate to string
            X['FirstPaymentDate'] = X['FirstPaymentDate'].astype(str)
            X['MaturityDate'] = X['MaturityDate'].astype(str)

            # Calculate LoanTermMonths and add it as a new column
            X['LoanTermMonths'] = X.apply(
                lambda row: self.calculate_num_months(row['FirstPaymentDate'], row['MaturityDate']),
                axis=1
            )
            
            # Determine LTV_Range based on LTV and add it as a new column
            X['LTV_Range'] = X['LTV'].apply(self.determine_ltv_range)
            
            # Determine Credit_Range based on Credit_Score and add it as a new column
            X['Credit_Range'] = X['CreditScore'].apply(self.determine_credit_range)
            
            # Apply the function to the 'MonthsInRepayment' column and create the new 'RepaymentPeriod' column
            X['Repay_Range'] = (X['MonthsInRepayment']/12).round().replace(
                {range(0, 4): '0-4yrs', 
                range(4, 8): '4-8yrs', 
                range(8, 12): '8-12yrs', 
                range(12, 16): '12-16yrs', 
                range(16, 20): '16-20yrs'}) 
            
            return X

            
        
    except Exception as e :
        raise CustomException(e , sys )
            

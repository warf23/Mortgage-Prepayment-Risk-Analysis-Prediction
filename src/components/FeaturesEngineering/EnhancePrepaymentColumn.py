


import pandas as pd 
import os 
import numpy as np 
import sys 

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline      # Base classes for custom transformers

from src.exception import CustomException 
from src.logger import logging

from datetime import datetime 

class CreatePrepaymentColumn(BaseEstimator, TransformerMixin):
    
    try :
        def calculate_emi(self, principal, annual_interest_rate, loan_term_months):
            monthly_interest_rate = (annual_interest_rate / 12) / 100
            emi_numerator = principal * monthly_interest_rate * (1 + monthly_interest_rate)**loan_term_months
            emi_denominator = ((1 + monthly_interest_rate)**loan_term_months - 1)
            emi = emi_numerator / emi_denominator
            return emi
    
        def principal(self, monthly_rate, amount, emi, month):
            for i in range(month):
                interest = monthly_rate * amount
                p = emi - interest
                amount -= p 
            return amount
        
        def prepay(self, dti, income):
            if dti < 40:
                p = income / 2
            else:
                p = income * (3/4)
            return p
        
    
        def fit(self, X, y=None):
            return self
        
        def transform(self, X):
            # Calculate EMI for each row in the DataFrame
            X['EMI'] = X.apply(lambda row: self.calculate_emi(row['OrigUPB'], row['OrigInterestRate'], row['OrigLoanTerm']), axis=1)
            
            # Calculate total payment
            X['total_payment'] = X['EMI'] * X['OrigLoanTerm']
            
            # Calculate interest amount
            X['interest_amount'] = X['total_payment'] - X['OrigUPB']
            
            X['Monthly_Income'] = X['EMI'] / (X['DTI'] / 100)
            X["monthlyInterest"] = X["interest_amount"] / X["OrigLoanTerm"]
            
            # Calculate current principal balance
            X['cur_principal'] = np.vectorize(self.principal)(
                ((X['OrigInterestRate'] / 12)) / 100, X['OrigUPB'], X['EMI'], X['MonthsInRepayment']
            )
            
            # Calculate prepayment amount
            X['prepayment'] = np.vectorize(self.prepay)(X['DTI'], X['Monthly_Income'] * 24)
            
            # Adjust prepayment for 2 years (24 months)
            X['prepayment'] = X['prepayment'] - (X['EMI'] * 24)
            
        
            X["ScheduledPrincipalPayments"] = (X["EMI"]-X["monthlyInterest"]) * X['OrigLoanTerm']  # Or : X["totalPayment"] - X["interestAmount"]
            X["ActualPrincipalPayments"] = (X["EMI"]) * X['MonthsInRepayment'] + X["prepayment"]
            X["OutstandingPrincipalBalance"] = X["cur_principal"]
            X["PPR"] = abs(X["ScheduledPrincipalPayments"] - X["ActualPrincipalPayments"]) / X["OutstandingPrincipalBalance"]
            
            return X
        
    except Exception as e :
        raise CustomException(e , sys )
    


# # Create Pip
# Enhance_dd = Pipeline([
#     ('prepayment_transformer', CreatePrepaymentColumn())
# ])

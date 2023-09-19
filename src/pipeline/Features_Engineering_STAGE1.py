import pandas as pd 
import os 
import numpy as np 
import sys 

from sklearn.base import BaseEstimator, TransformerMixin      # Base classes for custom transformers
from sklearn.compose import ColumnTransformer                 # Compose transformations on columns
from sklearn.pipeline import Pipeline, make_pipeline         # Pipeline for modeling


#importing the dataclass
from dataclasses import dataclass

from src.exception import CustomException 
from src.logger import logging

from datetime import datetime 



from src.config.entity_config import FeaturesEngineeringConfig

from src.exception import CustomException 
from src.logger import logging

    
class FeaturesEngineering: 
    
    def __init__(self ) : 
        self.EnhancedFeaturesPipeline = FeaturesEngineeringConfig()
        
    
    def initiate_Features_Engineering(self ): 
    
        
        
        
        try : 
            

            logging.info('----------------->Read Data After Cleaning<---------------------------------') 

            df = pd.read_csv("artifacts\My_Data_After_Cleaning\clean_data.csv")

            # Create directories if they don't exist
            os.makedirs(os.path.dirname(self.EnhancedFeaturesPipeline.feature_engineering_output_path),exist_ok=True)

            logging.info('----------------->Start Ading new Features <---------------------------------') 

             # Apply the data cleaning pipeline to the data
            New_Data = self.EnhancedFeaturesPipeline.Features_Engineering_Total_Pipeline.fit_transform(df)
            PPR_Features = [ 'EMI', 'total_payment'	,'interest_amount'	,'Monthly_Income'	,'monthlyInterest'	,'cur_principal'	,'prepayment'	,'ScheduledPrincipalPayments'	,'ActualPrincipalPayments'	,'OutstandingPrincipalBalance'	]
            logging.info('----------------->End Ading new Features <---------------------------------') 
            
            logging.info('----------------->Drop Columns \n -> CreditScore, FirstPaymentDate , MonthsInRepayment ,  MaturityDate , LTV  , Units <---------------------------------') 
            
            New_Data.drop(['CreditScore' , 'FirstPaymentDate' , 'MonthsInRepayment' ,  'MaturityDate' , 'LTV'  , 'Units' , 'MonthsDelinquent' , 'EMI', 'total_payment'	,'interest_amount'	,'Monthly_Income'	,'monthlyInterest'	,'cur_principal'	,'prepayment'	,'ScheduledPrincipalPayments'	,'ActualPrincipalPayments'	,'OutstandingPrincipalBalance' ] , axis = 1 , inplace = True)
            
            logging.info('----------------->Save data After Features Enginner <---------------------------------') 
            
            New_Data = New_Data[New_Data['DTI'] != 0]
            
            New_Data.to_csv(self.EnhancedFeaturesPipeline.feature_engineering_output_path,index=False,header=True)
            
            
            
            return self.EnhancedFeaturesPipeline.feature_engineering_output_path
           

        
        
        except Exception as e :
            logging.error('Adding Features Failed ........Failed: %s', str(e))
            raise CustomException(e , sys ) 
        

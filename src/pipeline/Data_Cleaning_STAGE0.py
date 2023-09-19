


import pandas as pd 
import os 
import numpy as np 
import sys 




#importing the dataclass
from dataclasses import dataclass

from src.config.entity_config import DatacleaningConfig

from src.exception import CustomException 
from src.logger import logging



class Datacleaning: 
    
    def __init__(self) : 
        
        self.Data_Cleaning = DatacleaningConfig() 
    
    def initiate_data_cleaning(self): 
        
        """
        initiate_data_cleaning: Method to perform data cleaning and save the cleaned data.

        Returns:
            str: Path to the cleaned data CSV file.
        """
        
        
        
        try : 
            
            logging.info('-------Read the Data From My Notebook  -----------')
            # Read the original CSV data
            df = pd.read_csv("Notebook\data\LoanExport.csv")
            
            # Create directories if they don't exist
            os.makedirs(os.path.dirname(self.Data_Cleaning.clean_data_path),exist_ok=True)
            
            # Apply the data cleaning pipeline to the data
            self.Data_Cleaning.data_cleaning_pipeline.fit_transform(df)
            
            
            # Save the cleaned data to a CSV file
            df.to_csv(self.Data_Cleaning.clean_data_path,index=False,header=True)
            
            logging.info('Cleaned data saved to: %s', self.Data_Cleaning.clean_data_path)
            
            logging.info('-------Data Cleaning Completed------------')
            
            return self.Data_Cleaning.clean_data_path
            
            

        
        
        except Exception as e :
            logging.error('Data Cleaning Failed: %s', str(e))
            raise CustomException(e , sys ) 
        


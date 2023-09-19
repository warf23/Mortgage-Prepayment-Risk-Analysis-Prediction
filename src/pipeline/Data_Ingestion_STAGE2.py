import os 
import sys 

import pandas as pd
import numpy as np 

# import sklearn 
from sklearn.model_selection import train_test_split 
from src.config.entity_config import DataIngestionConfig


from src.logger import logging
from src.exception import CustomException


class DataIngestion: 
     
    def __init__(self) : 
         self.data_ingestion_config = DataIngestionConfig() # Default configuration 
         
    def initiate_data_ingestion(self , data_path) : 
        """
        initiate_data_ingestion: Method to initiate data ingestion.
        """
        try : 
            logging.info("---------->Initiating data ingestion...<----------")
            
            df = pd.read_csv(data_path)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.all_data_path), exist_ok=True)
            
            logging.info('Train & test intialised')
            
            train_all , test_all = train_test_split(df , test_size = 0.2 , random_state = 42)
            
            train_all.to_csv(self.data_ingestion_config.train_data_path , index = False , header = True)
            test_all.to_csv(self.data_ingestion_config.test_data_path , index = False , header = True)
            
            logging.info('Train & test saved')
            
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path 
            )
            
            
            
            
            
        except Exception as e : 
            logging.info('Error in initiating data ingestion')
            raise CustomException(e , sys)
         
    
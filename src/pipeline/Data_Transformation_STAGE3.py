import sys 
import numpy as np
import pandas as pd
from dataclasses import dataclass
import os

#  ------------------------- Sciket learn  ------------------------- 
from sklearn.base import BaseEstimator, TransformerMixin      # Base classes for custom transformers
from sklearn.compose import ColumnTransformer                 # Compose transformations on columns
from sklearn.pipeline import Pipeline, make_pipeline         # Pipeline for modeling


####################### Data preprocessing ########################################

from src.config.entity_config import DataPreprocessingConfig

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object_joblib


class DataTransformation : 
    
    def __init__(self) :
        self.data_transormation_config = DataPreprocessingConfig() # Default configuration
        
   
    def initiale_data_transormation(self , train_path , test_path ) : 
        
        try: 
            
            
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
            
            preprocessing_obj = self.data_transormation_config.preprocessor_obj
            
            Classification_target_column_name_ = 'EverDelinquent' # Target column name for Classification Trainning
            Regression_target_column_name_ = 'PPR'# Target column name fro Regression Trainning
            
            logging.info("split our data into X_Classification , X_reggrrssion , y_reg , y_class ")
            
            logging.info("Drop PPR features ")
            
            
            input_feature_train_df=train_df.drop(columns=[Classification_target_column_name_ ,Regression_target_column_name_ ] ,axis=1)
            Classification_target_feature_train_df_=train_df[Classification_target_column_name_]
            Regression_target_feature_train_df_=train_df[Regression_target_column_name_]
            
            
            input_feature_test_df=test_df.drop(columns=[Classification_target_column_name_ ,Regression_target_column_name_ ],axis=1)
            Classification_target_feature_TEST_df_=test_df[Classification_target_column_name_]
            Regression_target_feature_TEST_df_=test_df[Regression_target_column_name_]
            
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df) # fit and transform on training data
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df) # fit on test data
            
            train_array_classification = np.c_[
                
                input_feature_train_arr  , np.array(Classification_target_feature_train_df_)
            ]
            
            
            test_array_classification = np.c_[
            
                input_feature_test_arr ,  np.array(Classification_target_feature_TEST_df_)
            ]
            
            train_array_Regression  = np.c_[
                
                input_feature_train_arr  , np.array(Regression_target_feature_train_df_)
            ]
            
            
            test_array_Regression = np.c_[
            
                input_feature_test_arr ,  np.array(Regression_target_feature_TEST_df_)
            ]
            
            logging.info(f"Saved preprocessing object.")
            
            save_object_joblib(
                
                file_path= self.data_transormation_config.preprocessor_obj_path ,
                obj=self.data_transormation_config.preprocessor_obj
                
            )
            
            return (
                train_array_classification,
                test_array_classification,
                train_array_Regression,
                test_array_Regression,
                self.data_transormation_config.preprocessor_obj_path
            ) 
            
            
        except Exception as e:
            raise CustomException(e, sys)
        



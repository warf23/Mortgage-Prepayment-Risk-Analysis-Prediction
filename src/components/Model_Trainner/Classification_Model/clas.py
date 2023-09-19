import os 
import numpy as np 
import sys 



from sklearn.metrics import (
    accuracy_score
    
)

from xgboost import XGBClassifier

from src.utils import save_object_joblib

from imblearn.over_sampling import SMOTE
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

from src.config.entity_config import Classification_ModelTrainerConfig


    
class Classification_ModelTrainer:
    def __init__(self):
        self.model_trainer_config=Classification_ModelTrainerConfig()
        
    def initiate_model_trainer(self,train_array,test_array):
        
        try: 
            logging.info('Model training started')
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            logging.info('Balnce the data using smote')
            
            
            X_train_resampled , y_train_resampled = SMOTE(random_state=42).fit_resample(X_train , y_train)
            
            logging.info('Smote balance done')
            
            
            model = XGBClassifier()
            
            model.fit(X_train_resampled , y_train_resampled)
            
            logging.info('Model training done')
            
            y_pred = model.predict(X_test)
            
            logging.info('Model prediction done')
            
            accuracy = accuracy_score(y_test , y_pred)
            logging.info('Accuracy : {} '.format(accuracy))
            
            # Saving the model 
            save_object_joblib(self.model_trainer_config.Cla_trained_model_file_path , model)
            
            logging.info('Model saved')
            
            return accuracy
            
            
        except Exception as e : 
            
            raise CustomException(e , sys) 
        

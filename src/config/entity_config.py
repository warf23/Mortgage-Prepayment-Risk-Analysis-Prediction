import os
from sklearn.pipeline import Pipeline

# Import DATA CLEANING Library
from src.components.data_cleaning.data_cleaning import Data_Cleaning
from src.components.data_cleaning.handling_outliers import Handling_Outliers
from src.components.data_cleaning.handling_missing_values import Handling_Missing_Values
from src.components.data_cleaning.drop_unused_features import Drop_Unused_Features


from src.components.FeaturesEngineering.EnhancePrepaymentColumn import CreatePrepaymentColumn
from src.components.FeaturesEngineering.FeatureAugmenter import AddNewColumnsTransformer


from src.components.Data_Preprocessor.get_preproceced_obj import Preprocessing

from dataclasses import dataclass

@dataclass
class DatacleaningConfig:
    
    """
    DatacleaningConfig: Configuration class for data cleaning settings.
    
    Attributes:
        clean_data_path (str): Path to the clean data CSV file.
        data_cleaning_pipeline (Pipeline): A pipeline for data cleaning tasks.
    """
    
    
    clean_data_path : str = os.path.join('artifacts' ,'My_Data_After_Cleaning' , 'clean_data.csv')
    
    data_cleaning_pipeline: Pipeline = Pipeline([
        ('Replace_X_WithNaN', Data_Cleaning()), 
        ('Handling_Outliers', Handling_Outliers()), 
        ('Handling_Missing_Values', Handling_Missing_Values()), 
        ('Drop_Unused_Features', Drop_Unused_Features())
    ])
    
    
    
@dataclass
class FeaturesEngineeringConfig:
    
    feature_engineering_output_path : str = os.path.join('artifacts' ,'Columns_Engine' , 'New_Data_after_FeaturesEngineer.csv')

    FeatureAugmenter_Pipeline : Pipeline = Pipeline([
        ('Creating New Features', AddNewColumnsTransformer()) 
        ])

    EnhancePrepaymentColumn_Pipeline : Pipeline = Pipeline([ 
         ('Create  Prepayment Column', CreatePrepaymentColumn())                                                   
                                                            ])
    
    Features_Engineering_Total_Pipeline : Pipeline = Pipeline([
        ('Feature Augmenter', FeatureAugmenter_Pipeline),
        ('Prepayment Enhancer', EnhancePrepaymentColumn_Pipeline)
        
    ])
    
    

@dataclass
class DataIngestionConfig:
    """
    DataIngestionConfig: Configuration class for data ingestion settings.
    
    Attributes:
        train_data_path (str): Path to the training data CSV file.
        test_data_path (str): Path to the test data CSV file.
    """

    train_data_path: str = os.path.join("artifacts", 'Data_Ingestion' ,"train_all.csv") # Default: "artifacts/train.csv"
    test_data_path: str = os.path.join("artifacts",'Data_Ingestion' , "test_all.csv") # "artifacts/test.csv"
    all_data_path: str = os.path.join("artifacts",'Data_Ingestion' , "data.csv") # "artifacts/my_data.csv"
    
@dataclass 
class DataPreprocessingConfig: 
    
    
    preprocessor_obj_path = os.path.join("artifacts", "preprocessor.joblib") # "artifacts/preprocessor_obj.pkl"
    preprocessor_obj =  Preprocessing.get_preprocessed_obj(Preprocessing())


@dataclass
class Regression_ModelTrainerConfig:
    Reg_trained_model_file_path=os.path.join("artifacts","Models","Regression","reg_model01.joblib")

@dataclass
class Classification_ModelTrainerConfig:
    Cla_trained_model_file_path=os.path.join("artifacts","Models","Classification","clas_model01.joblib")

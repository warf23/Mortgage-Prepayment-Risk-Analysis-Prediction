
from sklearn.compose import ColumnTransformer
from src.components.Data_Preprocessor.Columns import numerical_features_  , one_hote_categorical_features_ , ordinal_categories_features_
from src.components.Data_Preprocessor.Transformations import numerical_transformer , one_hote_categorical_features__transformer , ordinal_categories_features_transformer 

import sys
from src.logger import logging
from src.exception import CustomException

class Preprocessing:
    def __init__(self ):
        # Assuming you have your numerical and categorical column names
        self.numerical_features_ = numerical_features_
        self.one_hot_categorical_features_ = one_hote_categorical_features_
        self.ordinal_categories_features_ = ordinal_categories_features_
        
        self.numerical_transformer = numerical_transformer
        self.one_hote_categorical_features__transformer = one_hote_categorical_features__transformer
        self.ordinal_categories_features_transformer = ordinal_categories_features_transformer
        
        

    def get_preprocessed_obj(self):
        try:
            # Create the preprocessing pipelines for both numeric and categorical data
          

            logging.info(f"Categorical columns: {self.one_hot_categorical_features_ + self.ordinal_categories_features_}")
            logging.info(f"Numerical columns: {self.numerical_features_}")

            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', self.numerical_transformer, self.numerical_features_),
                    ('label_encoding',self.ordinal_categories_features_transformer , self.ordinal_categories_features_),
                    ('cat', self.one_hote_categorical_features__transformer, self.one_hot_categorical_features_)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        


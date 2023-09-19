import joblib
import pandas as pd
from pathlib import Path
import os 
import sys 
from src.components.FeaturesEngineering.EnhancePrepaymentColumn import CreatePrepaymentColumn 
# Specify the paths for the model and preprocessor
# model_path_reg = Path('artifacts\Models\Regression/reg_model01.joblib')
# model_path_clas = Path('artifacts\Models\Classification\clas_model01.joblib')
# preprocessor_path = Path('artifacts\preprocessor.joblib')
# print("Before Loading")
# model = joblib.load(model_path_reg)
# model_class = joblib.load(model_path_clas)

# preprocessor = joblib.load(preprocessor_path)
# print("After Loading")

sample_test = {
    "FirstTimeHomebuyer": "N",
    "MIP":5,
    "Occupancy": "O",
    "OCLTV": 57,
    "DTI": 9,
    "OrigUPB": 200000.0,
    "OrigInterestRate": 1,
    "Channel": "T",
    "PPM": "N",
    "PropertyType": "CO",
    "LoanPurpose": "P",
    "OrigLoanTerm": 360,
    "NumBorrowers": 2,
    "LoanTermMonths": 359,
    "LTV_Range": "HIGH",
    "Credit_Range": "Good",
    "Repay_Range": "0-4yrs" ,
    
}



# # Make predictions
from src.pipeline.predict_pipeline_STAGE_FINAL import PredictPipeline

model_reg , model_class , predictions_deliquent  , predictions_prepayment = PredictPipeline().predict(sample_test )


# predictions = model_class.predict(X)
if predictions_deliquent[0] == 1 : 
    print("Classification : EverDelinquent")
else :
    
    print(f"the loan in not ever deliquent and have prepayment value of : {round(predictions_prepayment[0],2)}")






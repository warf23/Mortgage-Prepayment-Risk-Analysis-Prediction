import sys
import joblib
import pandas as pd
from src.exception import CustomException
from src.utils import load_object_joblib 

from pathlib import Path
from src.components.FeaturesEngineering.EnhancePrepaymentColumn import CreatePrepaymentColumn 








class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features ):
        try: 
                model_path_reg = Path('artifacts\Models\Regression/reg_model01.joblib')
                model_path_clas = Path('artifacts\Models\Classification\clas_model01.joblib')
                preprocessor_path = Path('artifacts\preprocessor.joblib')
                
                model_reg = joblib.load(model_path_reg) 
                model_class = joblib.load(model_path_clas)
                preprocessor = joblib.load(preprocessor_path)
                
        
                # prepayment_transformer = CreatePrepaymentColumn()
                # preprocessed_sample = prepayment_transformer.transform(pd.DataFrame([features]))
                # preprocessed_sample=preprocessed_sample.drop(columns=['prepayment'] , axis=1)
                        
                print("Before Loading")

                print("After Loading")

                
                X = preprocessor.transform(pd.DataFrame([features]))
                
                predictions_deliquent = model_class.predict(X)
                predictions_prepayment = model_reg.predict(X)
                return model_reg , model_class , predictions_deliquent  , predictions_prepayment
        
        except Exception as e:
            raise CustomException(e, sys)
        
        

class CustomData:
    def __init__(self,
                 FirstTimeHomebuyer: str,
                 MIP: int,
                 Occupancy: str,
                 OCLTV: int,
                 DTI: int,
                 OrigUPB: float,
                 OrigInterestRate: float,
                 Channel: str,
                 PPM: str,
                 PropertyType: str,
                 LoanPurpose: str,
                 OrigLoanTerm: int,
                 NumBorrowers: int,
                 
                 LoanTermMonths: int,
                 LTV_Range: str,
                 Credit_Range: str,
                 Repay_Range: str):
        self.FirstTimeHomebuyer = FirstTimeHomebuyer
        self.MIP = MIP
        self.Occupancy = Occupancy
        self.OCLTV = OCLTV
        self.DTI = DTI
        self.OrigUPB = OrigUPB
        self.OrigInterestRate = OrigInterestRate
        self.Channel = Channel
        self.PPM = PPM
        self.PropertyType = PropertyType
        self.LoanPurpose = LoanPurpose
        self.OrigLoanTerm = OrigLoanTerm
        self.NumBorrowers = NumBorrowers
        
        self.LoanTermMonths = LoanTermMonths
        self.LTV_Range = LTV_Range
        self.Credit_Range = Credit_Range
        self.Repay_Range = Repay_Range

    def get_data_as_dict(self):
        try:
            custom_data_input_dict = {
            "FirstTimeHomebuyer": [self.FirstTimeHomebuyer],
            "MIP": [self.MIP],
            "Occupancy": [self.Occupancy],
            "OCLTV": [self.OCLTV],
            "DTI": [self.DTI],
            "OrigUPB": [self.OrigUPB],
            "OrigInterestRate": [self.OrigInterestRate],
            "Channel": [self.Channel],
            "PPM": [self.PPM],
            "PropertyType": [self.PropertyType],
            "LoanPurpose": [self.LoanPurpose],
            "OrigLoanTerm": [self.OrigLoanTerm],
            "NumBorrowers": [self.NumBorrowers],
            
            "LoanTermMonths": [self.LoanTermMonths],
            "LTV_Range": [self.LTV_Range],
            "Credit_Range": [self.Credit_Range],
            "Repay_Range": [self.Repay_Range],
        }

            return pd.DataFrame(custom_data_input_dict)
    
        except Exception as e:
            raise CustomException(e, sys)
        
 

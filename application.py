from flask import Flask, render_template, request
import joblib
import pandas as pd
from pathlib import Path
import os 
import sys


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('src/index.html')



@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
        if request.method=='GET':
            return render_template('src/Mortgage_Predict_Page.html')
        else:
            CustomData = {
            "FirstTimeHomebuyer": request.form.get('FirstTimeHomebuyer'),
            
            "MIP": float(request.form.get('MIP')) ,
            
            "Occupancy": request.form.get('Occupancy'),
            
            "OCLTV": float(request.form.get('OCLTV')) ,
            
            "DTI": float(request.form.get('DTI')) ,
            
            "OrigUPB":float(request.form.get('OrigUPB')),
            
            "OrigInterestRate":float(request.form.get('OrigInterestRate')),
            
            "Channel": request.form.get('Channel'),
            
            "PPM": request.form.get('PPM'),
            
            "PropertyType": request.form.get('PropertyType'),
            
            "LoanPurpose": request.form.get('LoanPurpose'),
            
            "OrigLoanTerm": float(request.form.get('OrigLoanTerm')),
            
            "NumBorrowers": float(request.form.get('NumBorrowers')),
            
            "LoanTermMonths": float(request.form.get('LoanTermMonths')),
            
            "LTV_Range": request.form.get('LTV_Range'),
            
            "Credit_Range": request.form.get('Credit_Range'),
            
            "Repay_Range": request.form.get('Repay_Range')
        }
        
        from src.pipeline.predict_pipeline_STAGE_FINAL import PredictPipeline 
        
        _ , _ , predictions_deliquent  , predictions_prepayment= PredictPipeline().predict(CustomData )
        
        
        if predictions_deliquent[0] == 1 : 
            
            return render_template('src/Mortgage_Predict_Page.html', results ='It appears that there is a delinquency issue associated with your loan.'  )
            
        else :
            return render_template('src/Mortgage_Predict_Page.html', results =f"Your loan is in excellent standing, with no history of delinquency. Your PPR of {round(predictions_prepayment[0],2) *100 } % " )
            



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
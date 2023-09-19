import os
import pickle
import sys

import numpy as np 
import pandas as pd
from joblib import dump, load

from src.exception import CustomException

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from collections import Counter

def save_object_joblib(file_path, obj):
  """Saves an object to a file using joblib.

  Args:
    file_path: The filepath to save the object to.
    obj: The object to save.
  """
  import joblib

  try:
    dir_path = os.path.dirname(file_path)

    os.makedirs(dir_path, exist_ok=True)

    joblib.dump(obj, file_path)

  except Exception as e:
    raise CustomException(e, sys)

def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object_joblib(file_path):
  """Loads an object from a file using joblib.

  Args:
    file_path: The filepath to load the object from.

  Returns:
    The object that was loaded.
  """
  import joblib

  try:
    return joblib.load(file_path)

  except Exception as e:
    raise CustomException(e, sys)
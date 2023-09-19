


from sklearn.preprocessing import RobustScaler, OneHotEncoder, OrdinalEncoder


numerical_transformer = RobustScaler() # RobustScaler is less prone to outliers

one_hote_categorical_features__transformer = OneHotEncoder(drop='first') # drop='first' to avoid dummy variable trap

ordinal_categories_features_transformer = OrdinalEncoder() # OrdinalEncoder to encode ordinal categories




import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class CleanAgeTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        def clean_age_value(val):
            if pd.isna(val):
                return np.nan
            try:
                # Convert to string and clean
                clean_val = str(val).replace('years', '').strip()
                # Convert to float first, then int to handle decimal values
                return int(float(clean_val))
            except (ValueError, TypeError):
                return np.nan
        
        if isinstance(X, pd.DataFrame):
            cleaned = X.iloc[:, 0].apply(clean_age_value)
            return cleaned.to_frame()
        elif isinstance(X, pd.Series):
            cleaned = X.apply(clean_age_value)
            return cleaned.to_frame()
        else:
            cleaned_val = clean_age_value(X)
            return np.array([[cleaned_val]])
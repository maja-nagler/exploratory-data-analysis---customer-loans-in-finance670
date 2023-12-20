
import pandas as pd


class DataFrameTransform:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def null_percentage(self):
        # Calculate percentage of NULL values in each column
        return (self.dataframe.isnull().sum() / len(self.dataframe)) * 100

    def drop_columns(self, columns):
        # Drop specified columns
        self.dataframe.drop(columns=columns, inplace=True)

    def impute_nulls(self, columns, method='median'):
        # Impute NULL values in specified columns using median or mean
        for col in columns:
            if method == 'median':
                self.dataframe[col].fillna(self.dataframe[col].median(), inplace=True)
            elif method == 'mean':
                self.dataframe[col].fillna(self.dataframe[col].mean(), inplace=True)
    
    def identify_skewed_columns(self, threshold=0.75):
        # Identify columns with skewness above the threshold
        skewed_cols = self.dataframe.skew().abs() > threshold
        return skewed_cols[skewed_cols].index.tolist()

    def transform_skewed_columns(self, columns):
        # Transform skewed columns using appropriate methods
        for col in columns:
            self.dataframe[col] = self.dataframe[col].apply(lambda x: x ** 0.5)  # Example transformation 
        
    def remove_outliers(self, columns):
        # Remove outliers from specified columns
        for col in columns:
            # Removing outliers using Z-score method
            z_scores = np.abs((self.dataframe[col] - self.dataframe[col].mean()) / self.dataframe[col].std())
            self.dataframe = self.dataframe[(z_scores < 3)]
            pass

    def identify_highly_correlated_columns(self, threshold=0.8):
        # Compute correlation matrix and identify highly correlated columns
        corr_matrix = self.dataframe.corr().abs()
        upper = corr_matrix.where(~pd.np.tril(pd.np.ones(corr_matrix.shape), k=-1).astype(pd.np.bool))
        to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
        return to_drop

    def remove_highly_correlated_columns(self, columns):
        # Remove highly correlated columns
        self.dataframe.drop(columns=columns, inplace=True)

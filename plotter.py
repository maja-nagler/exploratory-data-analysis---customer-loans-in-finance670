import matplotlib.pyplot as plt
import seaborn as sns


class Plotter:
    @staticmethod
    def visualize_data(dataframe):
        # Histograms for numerical columns
        numerical_cols = dataframe.select_dtypes(include=['int64', 'float64']).columns.tolist()
        for col in numerical_cols:
            plt.figure(figsize=(8, 6))
            sns.histplot(data=dataframe, x=col, kde=True)
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()

        # Boxplots for numerical columns
        for col in numerical_cols:
            plt.figure(figsize=(8, 6))
            sns.boxplot(data=dataframe, y=col)
            plt.title(f'Boxplot of {col}')
            plt.ylabel(col)
            plt.show()

        # Count plots for categorical columns
        categorical_cols = dataframe.select_dtypes(include=['object', 'category']).columns.tolist()
        for col in categorical_cols:
            plt.figure(figsize=(8, 6))
            sns.countplot(data=dataframe, x=col)
            plt.title(f'Countplot of {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.show()

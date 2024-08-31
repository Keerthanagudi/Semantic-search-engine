import kaggle
import pandas as pd
import zipfile
import os
from OpenSSL import SSL

def download_dataset(dataset, api_key):
    try:
        # Authenticate with Kaggle API
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(dataset)

        # Extract dataset files
        with zipfile.ZipFile(f"{dataset.split('/')[1]}.zip", "r") as zip_ref:
            zip_ref.extractall(".")

        print("Dataset downloaded and extracted successfully.")

        # Return the full file path of the main CSV file
        current_dir = os.getcwd()
        return f"{current_dir}/{dataset.split('/')[1]}.csv"

    except Exception as e:
        print(f"Failed to download the dataset: {e}")
        return None
    
if __name__ == "__main__":
    dataset_name = "harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows"
    api_key = "703c9e9ce7a3baf122d0b3203484b974"

    dataset_file = download_dataset(dataset_name, api_key)

    dataset='imdb_top_1000.csv'
    if dataset_file:

        # Load dataset into pandas DataFrame
        data_top10 = pd.read_csv(dataset)

        # Print columns and header of the dataset
        print("Columns:")
        print(data_top10.columns)

        print("\nFirst 10 rows of 'Series_Title' and 'Overview':")
        print(data_top10[["Series_Title", "Overview"]].head(10))
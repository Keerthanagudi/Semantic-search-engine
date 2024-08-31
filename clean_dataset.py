import pandas as pd

def clean_dataset(dataset_file):
    try:
        # Read dataset into DataFrame
        dataset = pd.read_csv(dataset_file)

        # Perform cleaning operations (removing duplicates)
        cleaned_dataset = dataset.drop_duplicates()

        # Select only the columns needed for embedding
        columns_selected = ['Series_Title', 'Overview', 'Director', 'Genre','Star1', 'Star2']
        cleaned_dataset = cleaned_dataset[columns_selected]

        # Clean the selected columns
        cleaned_dataset['Series_Title'] = cleaned_dataset['Series_Title'].str.lower()
        cleaned_dataset['Overview'] = cleaned_dataset['Overview'].str.lower()
        cleaned_dataset['Director'] = cleaned_dataset['Director'].str.lower()
        cleaned_dataset['Genre'] = cleaned_dataset['Genre'].str.lower()
        cleaned_dataset['Star1'] = cleaned_dataset['Star1'].str.lower()
        cleaned_dataset['Star2'] = cleaned_dataset['Star2'].str.lower()

        # Concatenate the cleaned columns into a new column
        cleaned_dataset['clean_text'] = cleaned_dataset['Series_Title'] + ' ' + cleaned_dataset['Overview'] + ' ' + cleaned_dataset['Director'] + ' ' + cleaned_dataset['Genre']+ ' ' + cleaned_dataset['Star1']+ ' ' + cleaned_dataset['Star2']

        # Save cleaned dataset
        cleaned_file = dataset_file.split(".")[0] + "_cleaned.csv"
        cleaned_dataset.to_csv(cleaned_file, index=False)

        print("Dataset cleaned and saved successfully as:", cleaned_file)
    except Exception as e:
        print(f"Failed to clean the dataset: {e}")

def main():
    dataset_file = "imdb_top_1000.csv"  
    clean_dataset(dataset_file)

if __name__ == "__main__":
    main()

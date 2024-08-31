# Semantic-Search-Engine

#IMPORTING DATASET USING KAGGLE API
 - create kaggle api token and save the json file to users (.kaggle)
 - give api key to py file
 - run create_dataset.py to download the dataset.

#CLEANING DATASET
 - chose required columns to be considered and clean the file.
 - clean.py will return dataset with cleaned columns and additional clean_text column with selected columns.

#EMBED AND STORE DATASET
 - download required python libraries.
 - sentence-transformers
 - streamlit
 - elasticsearch
   
#CONFIGURING ELASTIC SEARCH
 - download elasticsearch from official website, run elasticsearch on command prompt using elasticsearch.bat command.
 - after running easticsearch for first time, make sure to take note of password given and add it to embed_and_store.py & search.py file, wherever necessary.
 - ensure the ca certificate is among the trusted certificates list on pc, if not add it.
   
#SEARCH
 - run search.py file to get final output
 - you gat a streamlit command which shold be run in command prompt.
 - It automatically takes you to the web page for search.py code.

#QUERY
 - Search for any title or genre / any word relate dto the dataset considered.
 - You get an output of title and overview of most related searches along with similarity metric. 

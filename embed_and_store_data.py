import pandas as pd
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch


def embed_and_store(dataset_file, embedding_index='embedded_records'):

    # Load the dataset as a DataFrame
    dataset = pd.read_csv(dataset_file)

    # Choose a Sentence Embedding Model
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')

    # Embed the text
    embeddings = model.encode(dataset['clean_text'].tolist(), show_progress_bar=True)

    # Store the embeddings in Elasticsearch
    es = Elasticsearch(
        hosts=["https://localhost:9200"],
        basic_auth=("elastic", "hWGJXbDD2VCzK7GvxG0c"),
        ca_certs="C://Users//keert//elasticsearch-8.12.2//config//certs//http_ca.crt"
    )

    for idx, embedding in enumerate(embeddings):
        doc = {
            'text': dataset['clean_text'][idx],
            'embedding': embedding.tolist(),
            #  other fields from dataset
            'Series_Title': dataset['Series_Title'][idx],
            'Overview': dataset['Overview'][idx],
            'Director': dataset['Director'][idx],
            'Genre': dataset['Genre'][idx],
            'Star1': dataset['Star1'][idx],
            'Star2': dataset['Star2'][idx],
            'clean_text': dataset['clean_text'][idx]
        }

        # Index the document
        es.index(index=embedding_index, id=idx, body=doc)

    print("Data embedded and stored successfully in Elasticsearch.")

if __name__ == "__main__":
    dataset = 'imdb_top_1000_cleaned.csv'
    embed_and_store(dataset)


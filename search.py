
import streamlit as st
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch, exceptions

def main():
    st.title('Semantic Search Application')

    # Embed user input
    user_input = st.text_input('Enter your search query:')
    search_button = st.button('Search')

    if search_button:

        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        user_embedding = model.encode(user_input)

        # Search similar embeddings in Elasticsearch
        # Retrieve closest entries
        query = {
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                        "params": {"query_vector": user_embedding.tolist()}
                    }
                }
            }
        }
    
        try:
            # Connect to Elasticsearch
            es = Elasticsearch(
                hosts=["https://localhost:9200"],
                basic_auth=("elastic", "hWGJXbDD2VCzK7GvxG0c"),
                verify_certs=True,
                ca_certs="C://Users//keert//elasticsearch-8.12.2//config//certs//http_ca.crt"
            )

            res = es.search(index='embedded_records', body=query)
            hits = res['hits']['hits']

            # Extract the search results
            search_results = []
            for hit in hits:
                search_result = {}
                search_result['Series_Title'] = hit['_source']['Series_Title']
                search_result['Overview'] = hit['_source']['Overview']
                search_result['similarity_score'] = hit['_score']
                search_results.append(search_result)

            # Sort the search results by similarity score
            search_results = sorted(search_results, key=lambda x: x['similarity_score'], reverse=True)

            # Display the search results under the "Search Results" header
            if search_results:
                st.subheader('Search Results')
                for search_result in search_results:
                    st.write(f'{search_result["Series_Title"]} - Similarity score: {search_result["similarity_score"]}')
                    st.write(search_result['Overview'])
                    st.write('---')
            else:
                st.write('No matching results found.')

        except exceptions.ConnectionError:
            st.error("Failed to connect to Elasticsearch. Please make sure it's running.")
        except exceptions.RequestError as e:
            st.error(f"Elasticsearch request failed: {e}")

if __name__ == "__main__":
    main()


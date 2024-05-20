from settings import GOOGLE_API_KEY

from langchain_google_genai import GoogleGenerativeAIEmbeddings

CATEGORIES_PATH = 'data/categories.csv'
    
def embed_text(text: str):
    embeddings_model = GoogleGenerativeAIEmbeddings(model='models/text-embedding-004', google_api_key=GOOGLE_API_KEY, request_options={'timeout': 10000})
    query_embedding = embeddings_model.embed_query(text)
    return query_embedding

print(embed_text('iphone 14 pro'))

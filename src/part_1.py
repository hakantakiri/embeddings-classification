from settings import GOOGLE_API_KEY

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

CATEGORIES_PATH = 'data/categories.csv'

def generate_embeddings():
    loader = CSVLoader(CATEGORIES_PATH)
    documents = loader.load()
    embeddings_model = GoogleGenerativeAIEmbeddings(model='models/text-embedding-004', google_api_key=GOOGLE_API_KEY)
    local_db = FAISS.from_documents(documents=documents,embedding=embeddings_model)
    print(local_db)
    
def embed_text(text: str):
    embeddings_model = GoogleGenerativeAIEmbeddings(model='models/text-embedding-004', google_api_key=GOOGLE_API_KEY, request_options={'timeout': 10000})
    query_embedding = embeddings_model.embed_query(text)
    return query_embedding

# generate_embeddings()
print(embed_text('iphone 14 pro'))

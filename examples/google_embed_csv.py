import google.generativeai as genai
from settings import GOOGLE_API_KEY, GOOGLE_MODEL as MODEL
import json

CATEGORIES_PATH = './data/categories.csv'
genai.configure(api_key=GOOGLE_API_KEY)

def embed_csv(csv_path: str):
    f = open(csv_path)
    categories = f.read().split('\n')[1:]   
    return embed_list(categories)


def embed_list(list: list[str])->list[float]:
    result = genai.embed_content(model=MODEL, 
                                 content=list,
                                 task_type='classification')
    return result['embedding']

print(json.dumps({"embeddings": embed_csv(CATEGORIES_PATH)}))
    

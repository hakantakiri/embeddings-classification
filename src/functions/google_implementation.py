import google.generativeai as genai
from google.api_core import retry
from settings import GOOGLE_API_KEY, GOOGLE_MODEL as MODEL
from .f_operations import read_csv_into_list

genai.configure(api_key=GOOGLE_API_KEY)

def embed_csv(csv_path: str):
    categories = read_csv_into_list(csv_path)
    return embed_list(categories)

def embed_list(list: list[str])->list[list[float]]:
    result = genai.embed_content(model=MODEL, 
                                 content=list,
                                 task_type='classification')
    return result['embedding']

### Embed text
def make_embed_fn(model: str):
    @retry.Retry(timeout = 300.0) 
    def embed_fn(text: str) -> list[float]:
        embedding = genai.embed_content( model=model, 
                                        content=text, 
                                        task_type="classification")
        return embedding['embedding']
    return embed_fn

def embed_text(text: str)->list[float]:
    return make_embed_fn(MODEL)(text)

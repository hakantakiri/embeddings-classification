from google.api_core import retry
import google.generativeai as genai
import google.ai.generativelanguage as glm
from settings import GOOGLE_API_KEY, GOOGLE_MODEL as MODEL

text = 'iPhone 14 pro'
genai.configure(api_key=GOOGLE_API_KEY)

def make_embed_fn(model: str):
    @retry.Retry(timeout = 300.0) 
    def embed_fn(text: str) -> list[float]:
        embedding = genai.embed_content( model=model, 
                                        content=text, 
                                        task_type="classification")
        return embedding['embedding']
    return embed_fn

def create_text_embedding(text: str):
    return make_embed_fn(MODEL)(text)

print(create_text_embedding(text))
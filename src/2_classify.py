from functions.google_implementation import embed_text
from functions.cosine_similarity import get_CS
from functions.f_operations import load_json_file, save_json_to_local

LOCAL_EMBEDDINGS_JSON_PATH = './output/category_embeddings.json'
SCORES_JSON_PATH = './output/scores.json'
CLASSIFICATION_OUTPUT = './output/classification.json'
CATEGORIES_JSON_PATH = './output/readable_categories.json'
TEXT_TO_CLASSIFY = input('Enter the text to classify: ')

def load_local_embeddings(local_embeddings_json_path: str)-> list[list[float]] :
    return load_json_file(local_embeddings_json_path)

def get_CS_for_embedding_input(input_embedding: list[float], embeddings: list[list[float]]):
    similarities = []
    for emb in embeddings:
        similarities.append(get_CS(input_embedding, emb))
    return similarities

def get_CS_for_text_input(text: str, embeddings: list[list[float]]):
    return get_CS_for_embedding_input(embed_text(text), embeddings)

def save_scores(scores: list[float], scores_json_path: str):
    save_json_to_local(scores_json_path, scores)

def load_scores(scores_json_path: str)->list[float]:
    return load_json_file(scores_json_path)

def get_top(top: int, scores: list[float]) -> list[int]:
    tuples = [(i, score) for i, score in enumerate(scores)]
    ordered = sorted(tuples, key = lambda tuple: tuple[1], reverse=True)
    return ordered[0:top]

def translate_score_to_category(scores: tuple, categories: list[str]):
    picked = []
    for (i, score) in scores:
        picked.append((categories[i], score))
    return picked
        

save_scores(get_CS_for_text_input(TEXT_TO_CLASSIFY, 
                          load_local_embeddings(LOCAL_EMBEDDINGS_JSON_PATH)), 
                          SCORES_JSON_PATH)
# SAVE CLASSIFICATION LOCALLY
# save_json_to_local(CLASSIFICATION_OUTPUT, 
#                    translate_score_to_category(get_top(3, 
#                                                        load_scores(SCORES_JSON_PATH)), 
#                                                 load_json_file(CATEGORIES_JSON_PATH)))

# PRINT TO STD
print(translate_score_to_category(get_top(3, 
                                        load_scores(SCORES_JSON_PATH)), 
                                load_json_file(CATEGORIES_JSON_PATH)))
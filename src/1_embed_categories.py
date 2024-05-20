from functions.google_implementation import embed_csv
from functions.f_operations import save_json_to_local, read_csv_into_list

CATEGORIES_CSV_PATH = './data/categories.csv'
CATEGORIES_JSON_PATH = './output/readable_categories.json'
OUTPUT_JSON_PATH = './output/category_embeddings.json'

save_json_to_local(CATEGORIES_JSON_PATH, read_csv_into_list(CATEGORIES_CSV_PATH))
save_json_to_local(OUTPUT_JSON_PATH, 
                   embed_csv(CATEGORIES_CSV_PATH))
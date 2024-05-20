import json

def read_csv_into_list(csv_path):
    f = open(csv_path)
    return f.read().split('\n')[1:]   

def save_json_to_local(OUTPUT_JSON_PATH, data: any):
    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump({'data': data}, f, ensure_ascii=False)

def load_json_file(json_path):
    f = open(json_path)
    return json.load(f)['data']
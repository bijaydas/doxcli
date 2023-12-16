import json


def parse_json_file(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        return json.loads(f.read())


def parse_txt_file(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        return f.read().strip().split("\n")

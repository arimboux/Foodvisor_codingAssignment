from database import Database
import json
import os

path_to_files = '.'

db = Database()
with open(os.path.join(path_to_files, 'graph_build.json')) as build_json:
    build = json.load(build_json)
    db.add_nodes(build)

with open(os.path.join(path_to_files, 'img_extract.json')) as extract_json:
    extract = json.load(extract_json)
    db.add_extract(extract)

with open(os.path.join(path_to_files, 'graph_edits.json')) as edits_json:
    edits = json.load(edits_json)
    db.add_nodes(edits)

with open(os.path.join(path_to_files, 'expected_status.json')) as status_exp_json:
    status_exp = json.load(status_exp_json)

print('Expected status and results from get_extract_status are equals : ', db.get_extract_status() == status_exp)
import json
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
seed_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'seedData.js')

with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

json_str = json.dumps(db, indent=2, ensure_ascii=False)
js_content = f"export const seedData = {json_str};\n"

with open(seed_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Synchronized seedData.js with skillexa.json ({len(js_content)} bytes written).")

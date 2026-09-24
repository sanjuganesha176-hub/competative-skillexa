with open('server/seedData.js', 'r', encoding='utf-8') as f:
    text = f.read()

# usually `export const seedData = { ... };`
start = text.find('{')
end = text.rfind('}')
import json

try:
    data = json.loads(text[start:end+1])
    courses = data.get('courses', [])
    rc = [c for c in courses if 'reasoning' in c.get('slug', '').lower() or 'reasoning' in c.get('title', '').lower()]
    print("Reasoning courses in seedData:", rc)
    c_ids = [c['id'] for c in rc]
    rm = [m for m in data.get('modules', []) if m.get('course_id') in c_ids]
    print(f"Reasoning modules in seedData ({len(rm)}):")
    for m in rm:
        print(f"  {m['id']}: {m['title']}")
    rt = [t for t in data.get('topics', []) if t.get('course_id') in c_ids]
    print(f"Reasoning topics in seedData ({len(rt)}):")
    for t in rt:
        print(f"  ID {t['id']}: {t['title']} (module {t['module_id']}, order {t['order_index']})")
except Exception as e:
    print("Error parsing seedData.js as JSON:", e)

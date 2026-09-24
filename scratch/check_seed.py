with open('server/seedData.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find topics
print("Length of seedData.js:", len(text))
# Check how courses, modules, topics are defined
for match in re.finditer(r'\"id\":\s*(\d+),\s*\"title\":\s*\"([^\"]+)\",\s*\"course_id\":\s*3', text):
    print(f"Topic {match.group(1)}: {match.group(2)}")

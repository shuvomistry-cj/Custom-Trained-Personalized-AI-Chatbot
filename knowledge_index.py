import json

with open("knowledge_base.json", "r", encoding="utf-8") as f:
    knowledge_data = json.load(f)

print("Data Type:", type(knowledge_data))
print("First 5 Entries:", knowledge_data[:5] if isinstance(knowledge_data, list) else list(knowledge_data.items())[:5])

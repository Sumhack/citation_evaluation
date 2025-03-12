import pandas as pd
import re
import json

# Step 1: Load the CSV
data = pd.read_csv('C:\\Users\\suman.acharya\\OneDrive - Fractal Analytics Limited\\pythonProject\\inline-citations\\Rough data.csv',encoding="ISO-8859-1")

# Step 2: Preprocess Each Row
def split_statements(response):
    # Use regex or NLP-based tools for robust splitting
    statements = re.split(r'(?<!\d)\.(?!\d)', response)  # Avoid splitting on decimals
    return [stmt.strip() for stmt in statements if stmt.strip()]

enhanced_data = []
for idx, row in data.iterrows():
    question = row['Question']
    response = row['Response']
    citations = row['Citation Snippets']
    documents = row['Original Documents']

    # Step 3: Split Statements
    statements = split_statements(response)

    # Step 4: Map Citations and Snippets
    for i, statement in enumerate(statements, start=1):
        citations_found = re.findall(r'\?\d+\?', statement)
        snippets = [s for c in citations_found for s in citations.splitlines() if c in s]
        #docs = [d for c in citations_found for d in documents.splitlines() if c in d]

        enhanced_data.append({
            "question": question,
            "response": response,
            "context_id": f"Q{idx + 1:03}",
            "statement_index": i,
            "statement": statement,
            "citations": citations_found,
            "snippets": snippets,
            "documents": documents
        })

# Step 5: Save to JSON
with open('enhanced_data.json', 'w') as f:
    json.dump(enhanced_data, f, indent=4)

# Optional: Save to CSV
enhanced_df = pd.DataFrame(enhanced_data)
enhanced_df.to_csv('enhanced_data.csv', index=False)

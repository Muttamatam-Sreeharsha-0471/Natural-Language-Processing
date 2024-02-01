import spacy

def resolve_references(text):
    # Load spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Process the input text
    doc = nlp(text)

    # Extract entities and their positions
    entities = {ent.start: ent for ent in doc.ents}

    # Resolve pronoun references
    resolved_text = []
    for token in doc:
        if token.text.lower() in ['he', 'him', 'his', 'she', 'her', 'it']:
            # Check if the pronoun is part of an entity
            if token.i in entities:
                resolved_text.append(entities[token.i].text)
            else:
                # Use the pronoun as is if not part of an entity
                resolved_text.append(token.text)
        else:
            resolved_text.append(token.text)

    return ' '.join(resolved_text)

# Example usage
input_text = "John met Mary at the park. He gave her a book."
resolved_text = resolve_references(input_text)

# Display the results
print("Original Text:")
print(input_text)
print("\nResolved Text:")
print(resolved_text)

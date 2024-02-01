import spacy
def perform_ner(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
example_text = "Apple Inc. was founded by Steve Jobs in Cupertino. The iPhone was first released in 2007."
ner_results = perform_ner(example_text)
for entity, label in ner_results:
    print(f"{entity} - {label}")


    

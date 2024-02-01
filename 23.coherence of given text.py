import spacy
# Load the English language model
nlp = spacy.load('en_core_web_sm')
# Define the text
text = "The cat sat on the mat. The dog chased the cat. The cat ran away from the dog."
# Parse the text
doc = nlp(text)
# Extract the entities and relationships
entities = set([entity.text for entity in doc.ents])
relationships = set([chunk.text for chunk in doc.noun_chunks if chunk.root.dep_ == 'nsubj'])
# Compute the coherence score
coherence_score = len(relationships.intersection(entities)) / len(relationships.union(entities))
print('Coherence Score:', coherence_score)

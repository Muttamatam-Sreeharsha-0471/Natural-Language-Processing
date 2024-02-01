import spacy
def extract_noun_phrases(sentence):
    # Load the English language model for spaCy
    nlp = spacy.load("en_core_web_sm")
    # Process the input sentence
    doc = nlp(sentence)
    # Extract noun phrases and their meanings
    noun_phrases = []
    for chunk in doc.noun_chunks:
        noun_phrases.append((chunk.text, get_meaning(chunk.root)))
    return noun_phrases
def get_meaning(word):
    # In a real-world scenario, you might use WordNet or another resource for word meanings
    # For simplicity, this example returns a placeholder meaning
    return f"Meaning of '{word.text}' is not determined in this example."
# Example sentence
example_sentence = "The quick brown fox jumps over the lazy dog."
# Perform syntax-driven semantic analysis
semantic_results = extract_noun_phrases(example_sentence)
# Print the results
print("Noun Phrases and Their Meanings:")
for phrase, meaning in semantic_results:
    print(f"Noun Phrase: {phrase}")
    print(f"Meaning: {meaning}\n")

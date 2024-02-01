import nltk
from nltk.corpus import wordnet
def explore_word_meanings(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        print(f"No synsets found for the word '{word}'.")
        return
    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}")
        print()
example_word = "dog"
explore_word_meanings(example_word)

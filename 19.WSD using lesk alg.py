from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
example_sentence = "The bank was situated near the river bank."
tokenized_sentence = word_tokenize(example_sentence)
target_word = "bank"
sense = lesk(tokenized_sentence, target_word)
if sense:
    print(f"Target word: {target_word}")
    print(f"Best sense: {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print(f"No sense found for the target word '{target_word}'.")

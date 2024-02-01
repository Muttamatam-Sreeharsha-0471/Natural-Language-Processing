import nltk
def check_agreement(sentence):
    tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence))
    subjects = [word for word, tag in tagged_words if tag.startswith('N')]
    verbs = [word for word, tag in tagged_words if tag.startswith('V')]
    if subjects and verbs:
        subject_number = 'singular' if tagged_words[0][1].startswith('NNS') else 'singular'
        verb_number = 'singular' if tagged_words[-1][1].startswith('VB') else 'plural'
        if subject_number != verb_number:
            print("Subject-verb agreement error:")
            print(f"Subjects: {subjects} ({subject_number})")
            print(f"Verbs: {verbs} ({verb_number})")
        else:
            print("Subject-verb agreement is correct.")
    else:
        print("Unable to find subjects and verbs in the sentence.")
example_sentence = "The cat catches a dog"
check_agreement(example_sentence)

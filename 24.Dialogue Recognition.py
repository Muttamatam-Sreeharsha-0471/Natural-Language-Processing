import spacy
def recognize_dialog_acts(conversation):
    nlp = spacy.load("en_core_web_sm")
    # Process the conversation using spaCy
    doc = nlp(conversation)
    # Extract sentences and their dialog acts
    dialog_acts = []
    for sent in doc.sents:
        # You may customize this logic based on your requirements
        # Here, we assume simple categorization (question, statement, etc.)
        if "?" in sent.text:
            dialog_act = "Question"
        else:
            dialog_act = "Statement"
        dialog_acts.append((sent.text, dialog_act))
    return dialog_acts
if __name__ == "__main__":
    # Example conversation
    conversation = "User: How are you? Bot: I'm doing well. User: What's the weather like today?"
    # Recognize dialog acts
    dialog_acts = recognize_dialog_acts(conversation)
    # Print the recognized dialog acts
    for sentence, dialog_act in dialog_acts:
        print(f"{dialog_act}: {sentence}")

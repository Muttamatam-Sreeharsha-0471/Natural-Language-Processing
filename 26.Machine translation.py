import torch
from transformers import MarianMTModel, MarianTokenizer

def translate_to_french(english_sentence, model, tokenizer):
    input_text = f"translate English to French: {english_sentence}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)

    # Generate translation
    with torch.no_grad():
        output_ids = model.generate(input_ids)
    french_translation = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return french_translation

# Load the model and tokenizer outside the function
model_name = "Helsinki-NLP/opus-mt-en-fr"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Example usage
english_sentence = "The cat is on the mat."
french_translation = translate_to_french(english_sentence, model, tokenizer)
print(f"English: {english_sentence}")
print(f"French: {french_translation}")
     

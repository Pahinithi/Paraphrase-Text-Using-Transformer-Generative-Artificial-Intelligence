from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Load the model and tokenizer
model_name = 'tuner007/pegasus_paraphrase'
model = PegasusForConditionalGeneration.from_pretrained(model_name)
tokenizer = PegasusTokenizer.from_pretrained(model_name)

def generate_paraphrases(input_text, num_return_sequences=5):
    # Ensure that num_beams is at least as large as num_return_sequences
    num_beams = max(5, num_return_sequences)
    
    # Prepare the input
    batch = tokenizer([input_text], padding='longest', truncation=True, max_length=60, return_tensors="pt")
    
    # Generate paraphrases
    translated = model.generate(
        **batch, 
        max_length=60, 
        num_beams=num_beams, 
        num_return_sequences=num_return_sequences, 
        temperature=1.5, 
        do_sample=True
    )
    
    # Decode the paraphrased output
    paraphrases = tokenizer.batch_decode(translated, skip_special_tokens=True)
    
    return paraphrases

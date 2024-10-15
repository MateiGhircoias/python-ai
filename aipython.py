import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = 'gpt2'  # You can change this to 'gpt2-medium', 'gpt2-large', etc.
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Function to generate text
def generate_text(prompt, max_length=100, num_return_sequences=1):
    # Encode the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            no_repeat_ngram_size=2,
            early_stopping=True
        )

    # Decode the generated text
    generated_texts = []
    for i in range(num_return_sequences):
        generated_text = tokenizer.decode(output[i], skip_special_tokens=True)
        generated_texts.append(generated_text)

    return generated_texts

# Main loop for user input
if __name__ == "__main__":
    print("Welcome to the Text Generation AI! Type 'exit' to quit.")
    
    while True:
        prompt = input("Enter a prompt: ")
        
        if prompt.lower() == 'exit':
            break
        
        # Generate and display text
        generated_texts = generate_text(prompt, max_length=150, num_return_sequences=1)
        for idx, text in enumerate(generated_texts):
            print(f"\nGenerated Text {idx + 1}:\n{text}\n")

    print("Goodbye!")

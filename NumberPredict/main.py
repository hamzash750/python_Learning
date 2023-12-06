from transformers import pipeline

# Load the pre-trained language model for number prediction
model = pipeline("text2text-generation", model="EleutherAI/gpt-neo-1.3B")

# Generate numbers between 1 and 100
for i in range(1, 101):
    # Generate a prompt for the current number
    prompt = f"Please predict the next number in the sequence: {i},"
    # Generate the next number in the sequence using the language model
    output = model(prompt, max_length=2)[0]["generated_text"].strip()
    # Print the predicted number
    print(f"Predicted number for {i}: {output}")

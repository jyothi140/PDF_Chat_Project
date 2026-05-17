# We use a dictionary to simulate the 'Scoreboard' of the LLM
# This is called a Probability Distribution
prompt = "Artificial Intelligence will change the"

# The AI's internal 'Scoreboard' for the next word
word_scores = {
    "world": 0.01,    # Very likely
    "future": 0.04,   # Possible
    "internet": 0.05, # Less likely
    "weather": 0.90  # Unlikely
}

print(f"Prompt: {prompt}...")
print("-" * 30)

# We loop through the scoreboard to show how the AI 'sees' the options
for word, probability in word_scores.items():
    # Convert decimal to a percentage string
    percent = f"{probability * 100:.0f}%"
    # Create a visual bar using characters
    visual_bar = "#" * int(probability * 20)
    print(f"{word.ljust(10)} | {percent.ljust(5)} | {visual_bar}")

# Explain the choice
top_choice = max(word_scores, key=word_scores.get)
print("-" * 30)
print(f"AI Decision: The most likely next token is '{top_choice}'.")

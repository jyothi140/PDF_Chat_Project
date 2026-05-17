# We are creating a simple list of words to simulate a 'probability' choice
# This represents a tiny version of what an LLM does at a massive scale
import random # Import the random module to pick words

# The 'Prompt' or starting sentence
context = "The AI read the PDF and decided to"

# Possible 'Next Tokens' (words) based on what the AI learned
possible_next_words = ["summarize", "analyze", "explain", "rewrite"]

# The AI calculates which word is most likely (here we use random for the simulation)
chosen_word = random.choice(possible_next_words)

# Combine the context with the prediction
final_output = f"{context} {chosen_word} the content."

print("--- AI Prediction Simulation ---")
# Print the starting context
print(f"Input Context: {context}...")
# Print what the AI 'predicted' would come next
print(f"AI Prediction: {chosen_word}")
print(f"Final Sentence: {final_output}")

# A note on how this relates to our PDF project
print("\nNote: In our project, the LLM will use the PDF text to make these predictions!")

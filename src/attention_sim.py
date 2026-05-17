# We use a simple dictionary to represent 'Attention Weights'
# In a real LLM, these numbers are calculated using complex math (Dot Products)
sentence = "The bank of the river"

# Let's simulate how the AI focuses on the word 'bank'
# It gives high weight to 'river' to understand which 'bank' it is
attention_weights_for_bank = {
    "The": 0.05,
    "bank": 0.10,
    "of": 0.05,
    "the": 0.05,
    "river": 0.75  # The AI 'attends' most to 'river'
}

print(f"Analyzing sentence: '{sentence}'")
print(f"Focusing on the word: 'bank'\n")

print("--- Attention Weights (Importance) ---")
for word, weight in attention_weights_for_bank.items():
    # We create a simple visual bar to show the weight
    bar = "#" * int(weight * 20)
    print(f"{word.ljust(8)}: {bar} ({weight*100}%)")

# The result of high attention
print("\nConclusion: Because of high attention on 'river',")
print("the AI knows 'bank' means land, not a building.")

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load our secret vault
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 1. Define the 'Dials' for our AI
# Temperature: 0.0 (Strict/Factual) to 2.0 (Creative/Wild)
# Top-P: 0.0 to 1.0 (Percentage of vocabulary considered)
config = {
    "temperature": 0.2, # We keep it low for factual PDF chatting
    "top_p": 0.9,       # We allow a good variety of words
    "max_output_tokens": 100 # Limit the length of the response
}

# 2. Initialize the model with our custom config
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config=config
)

print(f"---  Running with Temp: {config['temperature']} ---")

# 3. Ask a question that requires a specific answer
prompt = "Give me a one-sentence definition of a PDF file."

try:
    response = model.generate_content(prompt)
    print(f"AI Response: {response.text}")
except Exception as e:
    print(f" ERROR: {e}")
# Import the OS and Dotenv for secure key loading
import os
from dotenv import load_dotenv
# Import the 'Symphony' components from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Start the 'Conductor' by loading environment variables
load_dotenv()

def run_milestone():
    print(" --- MODULE 4: ORCHESTRATION MILESTONE --- ")

    # 2. Initialize the AI Model (The Brain)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    # 3. Create a Multi-Variable Prompt Template
    # This ensures the output is always formatted as a professional summary
    template = """
    You are a professional research assistant.
    Provide a summary of the following topic: {topic}
    The target audience is: {audience}
    Format the output as a 3-bullet point list.
    """
    prompt = ChatPromptTemplate.from_template(template)

    # 4. Initialize the Output Parser (The Cleaner)
    parser = StrOutputParser()

    # 5. THE CHAIN: Snapping the Lego blocks together with Pipes (|)
    # User Input -> Prompt -> LLM -> Parser
    chain = prompt | llm | parser

    print(" Chain initialized. Sending orchestration request...")

    try:
        # 6. Execute the entire symphony with one 'Invoke' call
        # We pass the data as a dictionary matching our template variables
        response = chain.invoke({
            "topic": "The importance of Vector Databases in AI",
            "audience": "complete beginners"
        })

        # 7. Print the final, perfectly formatted result
        print("\n--- FINAL SUMMARY REPORT ---")
        print(response)
        print("\n MILESTONE REACHED: Your AI Orchestration is flawless!")

    except Exception as e:
        # 8. Handle any errors in the orchestration flow
        print(f" MILESTONE FAILED: {e}")

# Run the script
if __name__ == "__main__":
    run_milestone()

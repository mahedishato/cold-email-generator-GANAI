from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

class LLMClient:
    def __init__(self, model_name="llama-3.1-70b-versatile", temperature=0, max_tokens=None, timeout=None, max_retries=2):
        # Load environment variables from .env file
        load_dotenv()

        # Get the secret key from the environment variables
        self.secret_key = os.getenv('CODE_BASIC')

        # Initialize the ChatGroq model with the provided parameters
        self.llm = ChatGroq(
            groq_api_key=self.secret_key,
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            max_retries=max_retries,
        )

    def get_response(self, question):
        # Invoke the model with the provided question
        response = self.llm.invoke(question)
        return response.content

# Example usage
if __name__ == "__main__":
    client = LLMClient()
    text = "What is machine learning in short, two lines?"
    response = client.get_response(text)
    print(response)

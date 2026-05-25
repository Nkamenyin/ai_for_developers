import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

"""
    This projects sends a user prompt to OpenRouter API and returns the model's response.

    Args:
        prompt (str): The input text prompt from the user.

    Returns:
        str: The generated text response from the AI model.

    Raises:
        EnvironmentError: If required environment variables are missing.
        requests.exceptions.HTTPError: If the API request fails.
"""

def create_text(prompt: str) -> str:
    
    # Get API credentials from environment variables
    api_key = os.getenv("OPENROUTER_API_KEY")
    model_name = os.getenv("MODEL_NAME")

    # Validate environment variables
    if not api_key:
        raise EnvironmentError("OPENROUTER_API_KEY is missing.")
    if not model_name:
        raise EnvironmentError("MODEL_NAME is missing")

    # Send request to OpenRouter API
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model_name,
            "messages": [
                {"role": "user", "content": prompt}
            ],
        },
    )

    # Raise error if request failed (401, 402, 500, etc.)
    response.raise_for_status()

    # Parse JSON response
    data = response.json()

    # Extract and return generated message content
    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":

    # Ensure user provided input
    if len(sys.argv) < 2:
        sys.exit('Usage: python main.py "<your prompt>"')  

    # Combine CLI arguments into a single prompt string
    user_prompt = " ".join(sys.argv[1:])

    # Generate response from API and print to terminal
    print(create_text(user_prompt))
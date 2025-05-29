import openai
import os

# Set your API key here (or use environment variables for safety)
openai.api_key = os.getenv("OPENAI_API_KEY")

def test_openai_connection():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello using GPT-4o."}
            ]
        )
        print("✅ Successfully connected to OpenAI API using GPT-4o.")
        print("Response:")
        print(response['choices'][0]['message']['content'])
    except openai.error.AuthenticationError:
        print("❌ Authentication failed. Check your API key.")
    except openai.error.OpenAIError as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    test_openai_connection()
import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from openai._exceptions import OpenAIError, AuthenticationError

# Option 1: Set API key directly (not recommended for production)
import os
api_key = os.getenv("OPENAI_API_KEY")

# Option 2: Use environment variable (recommended)
# api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def test_openai_connection():
    try:
        messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello using GPT-4o."}
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        print("✅ Successfully connected to OpenAI API using GPT-4o.")
        print("Response:")
        print(response.choices[0].message.content)

    except AuthenticationError:
        print("❌ Authentication failed. Check your API key.")
    except OpenAIError as e:
        print(f"❌ An OpenAI error occurred: {e}")
    except Exception as e:
        print(f"❌ A general error occurred: {e}")


if __name__ == "__main__":
    test_openai_connection()

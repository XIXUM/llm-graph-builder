from openai import OpenAI

def test_openai():
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4.1",
        input="Write a one-sentence bedtime story about a unicorn."
    )

    print(response.output_text)

if __name__ == "__main__":
    test_openai()
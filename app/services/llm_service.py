from openai import OpenAI


def ask_llm(question: str) -> str:
    try:
        client = OpenAI()

        response = client.responses.create(
            model="gpt-5-nano",
            instructions="You are a helpful cloud assistant. Give short, beginner-friendly technical answers.",
            input=question,
        )

        return response.output_text.strip()

    except Exception as e:
        return f"OpenAI API error: {e}"
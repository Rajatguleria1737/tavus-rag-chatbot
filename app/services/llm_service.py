import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def create_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def stream_completion(prompt):

    return client.chat.completions.create(
        model="gpt-4.1",
        stream=True,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
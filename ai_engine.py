import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def process_data(data):
    prompt = f"You're an AI agent. Decide what to do with this input:\n{data}\n"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    decision = response['choices'][0]['message']['content']
    return decision.strip()

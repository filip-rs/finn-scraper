from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv('API_KEY')

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a horror story teller that scare the brave."},
        {
            "role": "user",
            "content": "Tell me about the horrors of javascript frameworks"
        }
    ]
)

print(completion.choices[0].message)
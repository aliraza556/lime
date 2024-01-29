from openai import OpenAI
from .models.state import (
    ConfigLoader,
)

class LocalParams(ConfigLoader):
    max_tokens = 50
    temperature = 0.0

LocalParams._initialize()

env_key = None
try:
    with open('/home/wsutt/.openai-key.txt', 'r') as f:
        env_key = f.read().strip()
except:
    from dotenv import load_dotenv
    import os
    load_dotenv()
    env_key = os.environ.get('OPENAI_API_KEY', None)
    assert env_key is not None, 'no env key found'


def submit_prompt(
    prompt: str,
    model_name: str,
    max_tokens: int = LocalParams.max_tokens,
    temperature: float = LocalParams.temperature,
) -> dict:

    client = OpenAI(
        api_key=env_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],    
        temperature=temperature,
        max_tokens=max_tokens,
        model=model_name,
    )

    return chat_completion


def get_completion(
    chat_completion: dict,
    role: str = "ai",
) -> str:

    return chat_completion.choices[0].message.content


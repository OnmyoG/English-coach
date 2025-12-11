import json
import os
from openai import OpenAI

with open(os.path.join(os.path.dirname(__file__), "config.json"), "r", encoding="utf-8") as f:
    config = json.load(f)

with open(os.path.join(os.path.dirname(__file__), "prompts.json"), "r", encoding="utf-8") as f:
    prompts = json.load(f)

prompt = prompts[config["prompt_mode"]]
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


conversation_history = [{"role": "system", "content": prompt}]

def generate_response(user_message: str) -> str:
    conversation_history.append({"role": "user", "content": user_message})
    limited_history = [conversation_history[0]] + conversation_history[-10:]
    response = client.chat.completions.create(
        model=config["model"],
        messages=limited_history,
        temperature=config.get("temperature", 0.7)
    )

    assistant_reply = response.choices[0].message.content.strip()
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

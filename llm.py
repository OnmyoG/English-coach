
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

conversation_history = [
    {"role": "system", "content": "You are a helpful English tutor. Keep your answers short and clear."}
]

def generate_response(user_message: str) -> str:
    conversation_history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-oss:20b",
        messages=conversation_history
    )
    assistant_reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply

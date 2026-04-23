from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_roast(chat_history):
    """Generate Naruto-style roast response"""

    prompt = f"""
You are Naruto, a funny savage anime character who roasts people in a hilarious way.
Keep it short, witty, and not too offensive.

Chat history:
{chat_history}

Reply with a funny roast:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Naruto, a funny roasting assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("[ERROR] OpenAI Error:", e)
        return "Bro even Naruto can't save this conversation 💀"
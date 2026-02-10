from openai import OpenAI

client = OpenAI()

def ask_order(user_message, model="gpt-4o-mini", temperature=0):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for a restaurant. You help customers place their orders."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

import chainlit as cl
from dotenv import load_dotenv
load_dotenv()

from src.llm import ask_order


@cl.on_message
async def main(message: cl.Message):
    response = ask_order(message.content)

    await cl.Message(
        content=response,
    ).send()

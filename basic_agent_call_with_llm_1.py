import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("open_ai_api_key")

async def check():
    print("I am called from check function")

    model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=str(api_key)
    )
    assistant = AssistantAgent(name="assistant",model_client=model_client)
    await Console(assistant.run_stream(task="What is 25 * 8"))
    await model_client.close()


asyncio.run(check())

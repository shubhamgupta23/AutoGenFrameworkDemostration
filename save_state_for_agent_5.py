import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("open_ai_api_key")

async def sav_state_agent():
    print("Going to save the state of first agent and pass it to another agent")

    model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=str(api_key)
    )

    agent_1 = AssistantAgent(name="QALead",model_client=model_client,
                             system_message="Act like a software QA lead and provide answers based on asked question to be in specific context. When anybody say 'thanks' or any related text you should say 'LESSON COMPLETE!'")

    agent_2 = AssistantAgent(name="QAEngineer", model_client=model_client,
                             system_message="Act like a QA engineer and you can ask answers to QALead for your QA related questions")

    await Console(agent_1.run_stream(task="'Steps' should be one of the key header of test case file"))

    current_state = await agent_1.save_state()

    with open("previous_chat.json","w") as f:
        json.dump(current_state,f)

    with open("previous_chat.json","r") as f:
        saved_state = json.load(f)

    await agent_2.load_state(saved_state)

    await Console(agent_2.run_stream(task="Which one is the header which should be in test case file?"))

    await model_client.close()



asyncio.run(sav_state_agent())
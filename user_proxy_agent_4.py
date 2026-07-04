import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("open_ai_api_key")


async def agent_to_agent_msg_limit():
    print("This function is useful to agent to agent chant")

    model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=str(api_key)
    )

    agent_1 = AssistantAgent(name="QALead", model_client=model_client,
                             system_message="Act like a software QA lead and provide answers based on asked question to be in specific context. When anybody say 'thanks' or any related text you should say 'LESSON COMPLETE!'")

    agent_2 = UserProxyAgent(name="Intern")

    team = RoundRobinGroupChat(participants=[agent_1, agent_2],
                               termination_condition=TextMentionTermination("LESSON COMPLETE!"))

    await Console(team.run_stream(task="What is test cases?"))

    await model_client.close()


asyncio.run(agent_to_agent_msg_limit())
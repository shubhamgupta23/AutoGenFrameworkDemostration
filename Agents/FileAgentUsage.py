import asyncio
import os

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

from Agents import McpConfig
from Agents.Agentfactory import Agentfactory

load_dotenv()
api_key = os.getenv("open_ai_api_key")

async def main():

    model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=str(api_key)
    )

    agents = Agentfactory(model_client)

    async with McpConfig.file_system_mcp_config() as workbench:

        file_agent = agents.file_system_agent(workbench,"Act like a file agent. Please do operations on file as requested. Always ask user if task done or not, if you receives 'thanks' or other related words say 'TASK COMPLETED!'.'")
        user_proxy = agents.user_proxy_agent(name="UserAgent")

        team = RoundRobinGroupChat(participants=[user_proxy,file_agent],
                            termination_condition=TextMentionTermination("TASK COMPLETED!")
                            )

        await Console(team.run_stream(task="Create a file and add current date in it"))

        await model_client.close()

asyncio.run(main())
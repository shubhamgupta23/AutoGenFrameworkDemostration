import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("open_ai_api_key")

async def file_tool_support():
    print("Providing file system tooling support to agent to write on file")

    model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=str(api_key)
    )

    server_param = StdioServerParams(command="/usr/bin/npx",
                                     args=[
                                         "-y",
                                         "@modelcontextprotocol/server-filesystem",
                                         str(os.getenv("directory_location"))
                                     ]
                                )

    workbenches = McpWorkbench(server_params=server_param)

    async with workbenches as workbench:
        agent = AssistantAgent(name="MathTeacher",model_client=model_client, workbench= workbench,
                       system_message="Act like a math teacher. Solve any algebra problem given and "
        "please write the solution on a text file. "
        "Use only the provided filesystem tool."
                       )
        await Console(agent.run_stream(task="What is the sum of 2*3 ?"))
        await model_client.close()


asyncio.run(file_tool_support())
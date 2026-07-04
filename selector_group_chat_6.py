import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("open_ai_api_key")


async def selector_group_chat():
    print("Here multiple agents can be interact with selector group class")

    model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=str(api_key)
    )

    qa_manager = AssistantAgent(name="QAManager",model_client=model_client,
                                system_message="Act like a software QA Manager. Let's discuss on how to implement AI in QA software. Can take multiple fllowups and sugeetsions within teams. And provide some context what you want. Review the things of QALead QATester suggestions and improvise it. Once all done if you see 'thanks' or something like that just end and say 'End Up Discussion!'"
                                )

    qa_lead = AssistantAgent(name="QALead", model_client=model_client,
                             system_message="Act like software QA Lead. Provide the valuable feedback taken by QA Manager and planning how we can implements AI on QA Testing. Provide technical aspect as per QA perspective"
                             )

    qa_tester = AssistantAgent(name="QATester", model_client=model_client,
                               system_message="Act like a software QA tester. You must be curious to know how we can implement the AI process in QA. Do some research and present to QALead and QAManager as per what manager wants. Show the blocker and critical aspect as well in front of team if any while implementing AI in process. You can share manul test generation to automation while reading the all docks and jira tickets.Once you clear say 'thanks'"
                               )

    max_message_termination = MaxMessageTermination(max_messages=6)
    text_mention_termination = TextMentionTermination("End Up Discussion!")

    termination_condition = max_message_termination | text_mention_termination

    team = SelectorGroupChat(participants=[qa_lead, qa_tester, qa_manager], model_client=model_client,
                      termination_condition=termination_condition
                      )

    await Console(team.run_stream(task="How to implement AI process in software QA?"))

    await model_client.close()


asyncio.run(selector_group_chat())
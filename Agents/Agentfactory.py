from autogen_agentchat.agents import AssistantAgent, UserProxyAgent


class Agentfactory:

    def __init__(self, model_client):
        print("init Agent factory")
        self.model_client = model_client



    def file_system_agent(self,workbench,system_message):
        file_system_agent = AssistantAgent(name="FileAgent"
                                            ,model_client=self.model_client,
                                                workbench=workbench,
                                                    system_message=system_message)
        return file_system_agent


    def user_proxy_agent(self,name):
        user_proxy_agent = UserProxyAgent(name=name)
        return user_proxy_agent







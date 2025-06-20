from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import requests

def call_custom_api(input_text):
    r = requests.post("http://api:8000/process", json={"prompt": input_text})
    return r.json()["response"]

tool = Tool(
    name="CustomAPI",
    func=call_custom_api,
    description="Calls a local FastAPI microservice"
)

llm = ChatOpenAI(temperature=0, openai_api_key="your-openai-key")

agent = initialize_agent(
    tools=[tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    print(agent.run("Process this input using the custom API."))
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from tools import search_tool
import re



load_dotenv()

# response = llm.invoke("What is the meaning of life?")
# print(response)

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
#setup LLM
#llm = ChatOpenAI(model = "gpt-4o-mini")
#llm = ChatAnthropic(model = "claude-3-5-sonnet-20241022")
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)#, temperature=0.7)
#setup output parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)
#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that helps generate reliable, factual research papers.
            If a question requires real-world knowledge, always use the available tools.
            Use the `search` tool whenever the question involves recent events or facts.
            Wrap your final output in this format only:\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
query = input("What can I help you research?")
raw_response = agent_executor.invoke({"query": query})
# print(raw_response)
try:
    # Extract the JSON string from inside the markdown block
    raw_output = raw_response.get("output", "")
    json_str = re.sub(r"```json|```", "", raw_output).strip()

    # Now parse into your Pydantic model
    structured_response = parser.parse(json_str)
    print(structured_response)
except Exception as e:
    print(" Error parsing response:", e)
    print(" Raw Response:", raw_response)
# print(structured_response.topic)
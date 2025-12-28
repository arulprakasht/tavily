import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tavily_resp = requests.post(
    "https://api.tavily.com/search",
    json={
        "api_key": os.getenv("TAVILY_API_KEY"),
        "query": "What is Tavily MCP?"
    }
).json()

resp = client.responses.create(
    model="gpt-4.1-mini",
    input=f"Answer using this data:\n{tavily_resp}"
)

print(resp.output_text)
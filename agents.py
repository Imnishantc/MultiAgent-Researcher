from langchain.agents import create_agent
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url
from dotenv import load_dotenv

load_dotenv()

#MODEL SETUP
llm = ChatMistralAI(model = "mistral-medium-latest", temperature = 0)

#Agent 1: Web Search Agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools=[web_search]
    )

#Agent 2: Web Scraping Agent
def build_scraping_agent():
    return create_agent(
        model = llm,
        tools=[scrape_url]
    )

#Writer Chain

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human","""Write a detailed research report on the topic below.
     Topic: {topic}

     Research gathered:
     {research}

     Structure the report as:  
     -Introduction
     -Key Findings{{minimum 3 well explained points}}
     -Conclusion
     -sources (list all sources used in the research)

     Be detailed, factual and professional.
    """)
])

writer_chain = writer_prompt | llm | StrOutputParser()

#Critic Chain

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research critic. Your task is to evaluate the quality of research reports based on accuracy, depth, clarity, and relevance."),
    ("human", """Evaluate the following research report based on the criteria below:
    
Research Report:
{report}
    
Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas for Improvement:
- ...
- ...

One line verdict:
...""")
])

critic_chain = critic_prompt | llm | StrOutputParser()

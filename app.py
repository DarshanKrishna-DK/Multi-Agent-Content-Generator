from crewai import Agent, Task, Crew, LLM 
from crewai_tools import SerperDevTool

from dotenv import load_dotenv

import os

load_dotenv()

# Initialize the CrewAI Agent

topic = "Harms of Social Media"

# Basic configuration - Tool 1
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)


# Tool 2
search_tool = SerperDevTool(n=10)

# Agent 1
senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal = "Research on the harms of social media",
    backstory = "You are Senior Research Analyst with 5 years of experience in the field of psychology. You have worked on multiple projects related to the the human brain and have a good understanding of the domain.",
    allow_delegation = False,
    verbose = True,
    tools = [search_tool],
    llm = llm
)

# Agent 2

content_writer = Agent(
    role="Content Writer",
    goal = "Write a detailed article on how social media harms the human brain",
    backstory = "You are a Content Writer with 3 years of experience in writing articles on various topics. You have written articles on the social media and the human brain in the past and have a good understanding of the domain.",
    allow_delegation = False,
    verbose = True,
    llm = llm
)

# Research Task

research_task = Task(
    description = "Research on the harms of social media",
    expected_output = "A detailed summary of the  of effects of social media in the human brain",
    agent = senior_research_analyst
)

# Content Generation Task

writing_task = Task(
    description = "Write a detailed article on the of social media",
    expected_output = "A well-researched article on the effects of social media in the human brain",
    agent = content_writer
)

# Crew

crew = Crew(
    agents = [senior_research_analyst, content_writer],
    tasks = [research_task, writing_task],
    verbose = True
)

result = crew.kickoff(inputs={"topic": topic})

print(result)

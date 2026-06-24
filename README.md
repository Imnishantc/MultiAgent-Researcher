# MultiAgent-Researcher
An end-to-end AI-powered Multi-Agent Research System that autonomously searches the web, extracts relevant information, generates structured research reports, and critiques the generated content using specialized AI agents powered by Mistral AI, LangChain, Tavily Search, and BeautifulSoup.

The application is built with a Streamlit-based user interface and fully containerized using Docker, enabling consistent deployment across different environments.

## Key Highlights

* Multi-Agent AI Architecture
* Tavily-Powered Web Search
* Intelligent Web Scraping with BeautifulSoup
* AI-Powered Research Report Generation
* Automated Research Critique & Evaluation
* Streamlit-Based Interactive Interface
* Dockerized Deployment
* LangChain Agent Framework
* Modular and Scalable Architecture

---

## Project Overview

Traditional research workflows require manually searching multiple sources, reading articles, organizing information, and preparing summaries.

MultiAgent-Researcher automates the complete research pipeline using specialized AI agents.

The system accepts a research topic, performs web search using Tavily Search, extracts detailed information from relevant sources using BeautifulSoup, generates a structured research report, and evaluates the quality of the report using a Critic Agent.

Example:

**User Query**

> Recent developments in Agentic AI

**AI Workflow**

Natural Language Query → Search Agent → Scraper Agent → Writer Agent → Critic Agent → Final Research Report

---

## Docker Support

Build Docker Image

```bash
docker build -t multiagent-researcher .
```

Run Docker Container

```bash
docker run -p 8501:8501 --env-file .env multiagent-researcher
```

The application will be available at:

[MultiAgent Researcher](https://multiagent-researcher.onrender.com/)


---

## Architecture

<img width="327" height="672" alt="image" src="https://github.com/user-attachments/assets/89edf92c-f232-4d30-9b13-80fb41eddc51" />

---

## Features

* Multi-Agent Research Workflow
* Tavily Search Integration
* Intelligent Web Scraping
* Research Report Generation
* Research Critique and Evaluation
* Streamlit User Interface
* Dockerized Deployment
* Modular Agent-Based Design
* Environment Variable Management using .env
* Mistral AI Integration
* LangChain Agent Framework
* Automated Information Gathering

---

## Tech Stack

### Programming Language

* Python

### AI / LLM

* Mistral AI
* LangChain
* Prompt Engineering
* LCEL (LangChain Expression Language)

### Research Tools

* Tavily Search API
* BeautifulSoup
* Requests

### Frontend

* Streamlit

### DevOps & Deployment

* Docker

### Development Tools

* VS Code
* Git
* GitHub

---

## Project Structure

```text
MultiAgent-Researcher/
│
├── agents.py
│   ├── Search Agent
│   ├── Scraper Agent
│   ├── Writer Chain
│   └── Critic Chain
│
├── tools.py
│   ├── Tavily Search Tool
│   └── BeautifulSoup Scraper Tool
│
├── pipeline.py
│   └── Main Research Pipeline
│
├── app.py
│   └── Streamlit Application
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .env
```

## Sample Research Topics

* Recent developments in Agentic AI
* Applications of Generative AI in Healthcare
* Future of Autonomous AI Agents
* Impact of Artificial Intelligence on Education
* Latest Trends in Machine Learning
* Advances in Computer Vision
* Quantum Computing Research Updates

---

## Screenshots

### Application Dashboard

<img width="1355" height="666" alt="image" src="https://github.com/user-attachments/assets/7b0d87e8-aabd-4b5d-bb38-fa07286d779f" />

### Agent Execution Workflow

<img width="1343" height="663" alt="image" src="https://github.com/user-attachments/assets/332e4555-caa8-4cf2-9ab5-1c1183bdd4da" />
<img width="1310" height="650" alt="image" src="https://github.com/user-attachments/assets/1e18f328-0bb1-416c-b48b-4bed0e984e49" />
<img width="1323" height="557" alt="image" src="https://github.com/user-attachments/assets/6545a486-8d77-49f2-b572-c8dc846bbc5a" />
<img width="1302" height="630" alt="image" src="https://github.com/user-attachments/assets/4eda3041-5bcb-4085-949d-032a9f0fe777" />
<img width="1285" height="383" alt="image" src="https://github.com/user-attachments/assets/d493ff8a-bce4-42dd-af08-cad33d241922" />


### Generated Research Report

<img width="1301" height="612" alt="image" src="https://github.com/user-attachments/assets/81c46753-e0e5-440f-8f15-1987d3d97ec5" />


### Critic Evaluation

<img width="1306" height="432" alt="image" src="https://github.com/user-attachments/assets/8349db14-65ef-436f-ae1d-d63a28b16caa" />


### Docker Deployment

<img width="1897" height="1046" alt="image" src="https://github.com/user-attachments/assets/43047190-cfba-4cac-8fcd-bdeec3deb370" />


---

## Agent Workflow

### Search Agent

Responsibilities:

* Search the web using Tavily Search
* Find recent and reliable sources
* Gather initial research information

### Scraper Agent

Responsibilities:

* Extract webpage content
* Parse relevant information
* Provide deeper context

### Writer Agent

Responsibilities:

* Analyze gathered information
* Generate structured research reports
* Organize findings clearly

### Critic Agent

Responsibilities:

* Review generated reports
* Evaluate report quality
* Identify strengths and weaknesses
* Provide final feedback

---

## Real-World Applications

This project can be used by:

* Researchers
* Students
* Business Analysts
* Content Writers
* Market Research Teams
* Product Managers
* AI Research Enthusiasts

The system reduces manual research effort by automating information gathering, report generation, and quality evaluation.

---

## Learning Outcomes

Through this project I gained hands-on experience in:

* Multi-Agent Systems
* LangChain Framework
* Mistral AI Integration
* Tavily Search API
* Web Scraping with BeautifulSoup
* Streamlit Application Development
* Docker Containerization
* AI Workflow Design
* End-to-End AI Application Development

---

## Future Enhancements

* React Frontend
* FastAPI Backend
* LangGraph Agent Orchestration
* PDF Export
* Research History Tracking
* Citation Management
* Multi-Source Research Validation
* Vector Database Integration
* Agent Memory
* Cloud Deployment

---

## Author

Nishant Chavan

LinkedIn: https://www.linkedin.com/in/nishant-chavan1705/

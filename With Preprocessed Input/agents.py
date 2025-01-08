from crewai import Agent

# Agent for vectorization and storage
data_vectorizer = Agent(
    role='Data Vectorizer',
    goal='Vectorize provided content and store it in a vector database using Ollama embeddings.',
    verbose=True,
    memory=True,
    tools=[],
    allow_delegation=False
)

# Agent for retriever design
retriever = Agent(
    role='Retriever Designer',
    goal='Design a retriever to search vectorized data and return relevant results.',
    verbose=True,
    memory=True,
    tools=[],
    allow_delegation=False
)

# Agent for chatbot
chatbot_agent = Agent(
    role='Chatbot Designer',
    goal='Implement a chatbot to answer questions based on retrieved content using Ollama LLM.',
    verbose=True,
    memory=True,
    tools=[],
    allow_delegation=False
)

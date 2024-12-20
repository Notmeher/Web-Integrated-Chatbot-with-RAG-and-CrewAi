import os
from dotenv import load_dotenv
from tasks import scrape_data, vectorize_data, design_retriever, implement_chatbot

# Load environment variables
load_dotenv()

URLS = [
    "https://genzmarketing.xyz/",
    "https://genzmarketing.xyz/about_us",
    "https://genzmarketing.xyz/services",
    "https://genzmarketing.xyz/books",
    "https://genzmarketing.xyz/packages",
    "https://genzmarketing.xyz/blogs",
    "https://genzmarketing.xyz/contact_us",
]

def crew_workflow(query):
    # Step 1: Scrape website data
    scraping_result = scrape_data({"urls": URLS})
    if "error" in scraping_result:
        return {"error": scraping_result["error"]}
    
    json_data = scraping_result["json_data"]

    # Step 2: Vectorize scraped data
    vectorization_result = vectorize_data({"json_data": json_data})
    if "error" in vectorization_result:
        return {"error": vectorization_result["error"]}

    # Step 3: Design retriever
    retriever_result = design_retriever({"vector_database": vectorization_result["database"]})
    if "error" in retriever_result:
        return {"error": retriever_result["error"]}

    # Step 4: Implement chatbot and answer the query
    chatbot = implement_chatbot({"retriever": retriever_result["retriever"]})
    if "error" in chatbot:
        return {"error": chatbot["error"]}

    # Query the chatbot
    response = chatbot({"query": query})
    return {"status": "success", "response": response}

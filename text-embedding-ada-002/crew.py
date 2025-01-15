import os
from dotenv import load_dotenv
from tasks import vectorize_data, design_retriever, implement_chatbot

# Load environment variables
load_dotenv()

JSON_FILE_PATH = r"D:\chat\GENZMarketing.json"

def crew_workflow(query):
    # Step 1: Vectorize provided data
    vectorization_result = vectorize_data({"json_file_path": JSON_FILE_PATH})
    if "error" in vectorization_result:
        return {"error": vectorization_result["error"]}

    # Step 2: Design retriever
    retriever_result = design_retriever({"vector_database": vectorization_result["database"]})
    if "error" in retriever_result:
        return {"error": retriever_result["error"]}

    # Step 3: Implement chatbot and answer the query
    chatbot_result = implement_chatbot({"retriever": retriever_result["retriever"]})
    if "error" in chatbot_result:
        return {"error": chatbot_result["error"]}

    # Get the chatbot function
    chatbot = chatbot_result["chatbot"]

    # Query the chatbot
    response = chatbot(query)
    result = response.get("result", "No answer provided.")
    sources = response.get("sources", [])

    return {
        "status": "success",
        "response": result,
        "sources": sources
    }

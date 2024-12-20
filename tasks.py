from tools import scrape_all_websites, save_to_json, create_vector_database, setup_retriever, build_chatbot

# Task: Scrape data
def scrape_data(inputs):
    urls = inputs.get("urls")
    if not urls:
        return {"error": "No URLs provided."}

    try:
        scraped_data = scrape_all_websites(urls)
        json_data = save_to_json(scraped_data)
        return {"json_data": json_data}
    except Exception as e:
        return {"error": f"Scraping error: {str(e)}"}

# Task: Vectorize data
def vectorize_data(inputs):
    json_data = inputs.get("json_data")
    if not json_data:
        return {"error": "No data for vectorization."}

    try:
        vector_db = create_vector_database(json_data)
        return {"database": vector_db}
    except Exception as e:
        return {"error": f"Vectorization error: {str(e)}"}

# Task: Design retriever
def design_retriever(inputs):
    vector_database = inputs.get("vector_database")
    if not vector_database:
        return {"error": "No vector database provided."}

    try:
        retriever = setup_retriever(vector_database)
        return {"retriever": retriever}
    except Exception as e:
        return {"error": f"Retriever design error: {str(e)}"}

# Task: Implement chatbot
def implement_chatbot(inputs):
    retriever = inputs.get("retriever")
    if not retriever:
        return {"error": "No retriever provided."}

    try:
        chatbot = build_chatbot(retriever)
        return chatbot
    except Exception as e:
        return {"error": f"Chatbot implementation error: {str(e)}"}

import streamlit as st
from crew import crew_workflow

st.title("GenZMarketing Chatbot with Local LLM and Crew AI")

# Input query
query = st.text_input("Enter your question:")

if st.button("Start Analysis and Ask"):
    if query:
        result = crew_workflow(query)

        if "error" in result:
            st.error(result["error"])
        else:
            response = result["response"]
            answer = response.get("result", "No answer provided.")
            st.success("Query answered successfully!")
            st.write(f"**Question:** {query}")
            st.write(f"**Answer:** {answer}")
    else:
        st.error("Please provide a question.")

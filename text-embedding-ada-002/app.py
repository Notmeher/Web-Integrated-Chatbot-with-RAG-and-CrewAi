import streamlit as st
from crew import crew_workflow

st.title("GenZMarketing Chatbot")

# Input query
query = st.text_input("Enter your question:")

if st.button("Start Analysis and Ask"):
    if query:
        result = crew_workflow(query)

        if "error" in result:
            st.error(result["error"])
        else:
            response = result["response"]
            sources = result.get("sources", [])
            
            st.success("Query answered successfully!")
            st.write(f"**Question:** {query}")
            st.write(f"**Answer:** {response}")
            
            if sources:
                st.write("**Sources:**")
                for source in sources:
                    st.write(f"- {source}")
            else:
                st.write("No sources found.")
    else:
        st.error("Please provide a question.")

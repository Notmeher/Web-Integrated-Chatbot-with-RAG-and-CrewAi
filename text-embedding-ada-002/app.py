import streamlit as st
from crew import crew_workflow

st.title("GenZMarketing Chatbot")

# Initialize session state to store past queries and responses
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input query
query = st.text_input("Enter your question:")

if st.button("Start Analysis and Ask"):
    if query:
        # Get the result from the workflow
        result = crew_workflow(query)

        if "error" in result:
            st.error(result["error"])
        else:
            response = result["response"]
            sources = result.get("sources", [])

            # Append the new query and response to the chat history
            st.session_state["chat_history"].append({
                "question": query,
                "response": response,
                "sources": sources,
            })

            st.success("Query answered successfully!")
    else:
        st.error("Please provide a question.")

# Display chat history
st.write("## Chat History")
for chat in st.session_state["chat_history"]:
    st.write(f"**Question:** {chat['question']}")
    st.write(f"**Answer:** {chat['response']}")
    if chat["sources"]:
        st.write("**Sources:**")
        for source in chat["sources"]:
            st.write(f"- {source}")
    else:
        st.write("No sources found.")
    st.write("---")  # Divider between chats

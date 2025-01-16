import asyncio
import streamlit as st
from crew import crew_workflow

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

def display_message(role, content):
    """Display a message in the chat interface based on its role."""
    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)
    elif role == "assistant":
        with st.chat_message("assistant"):
            st.markdown(content)
    elif role == "system":
        with st.chat_message("system"):
            st.markdown(f"**System**: {content}")

async def run_workflow_with_streaming(query):
    """Run the chatbot workflow with streaming text responses."""
    # Append the user's query to the chat history
    st.session_state["messages"].append({"role": "user", "content": query})

    # Display the user's query in the chat UI
    display_message("user", query)

    # Placeholder for the assistant's response
    message_placeholder = st.empty()
    partial_response = ""

    # Simulate streaming by breaking the response into chunks
    result = crew_workflow(query)

    if "error" in result:
        st.error(result["error"])
        return

    response = result.get("response", "")
    sources = result.get("sources", [])

    for chunk in response.split():
        await asyncio.sleep(0.1)  # Simulate streaming delay
        partial_response += f"{chunk} "
        message_placeholder.markdown(partial_response)

    # Finalize the response
    message_placeholder.markdown(partial_response)

    # Append the assistant's response to the chat history
    st.session_state["messages"].append({"role": "assistant", "content": partial_response})

    # Optionally display sources
    if sources:
        source_text = "\n".join([f"- {source}" for source in sources])
        st.session_state["messages"].append({"role": "system", "content": f"Sources:\n{source_text}"})

async def main():
    st.title("GenZMarketing Chatbot")
    st.write("Ask questions and receive responses about marketing with GenZ insights!")

    # Display chat history
    for message in st.session_state["messages"]:
        display_message(message["role"], message["content"])

    # User input
    user_query = st.chat_input("What is your question?")

    if user_query:
        await run_workflow_with_streaming(user_query)

if __name__ == "__main__":
    asyncio.run(main())

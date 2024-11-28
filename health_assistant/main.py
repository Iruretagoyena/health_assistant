import os
from health_assistant.data_processing import process_user_data, get_generated_sleep_data, convert_sleep_data_to_prompt
from health_assistant.rag_system import create_rag_system
from langchain.schema import SystemMessage
from health_assistant.config import set_openai_key
from langchain_openai import ChatOpenAI
from langgraph.graph import Graph, StateGraph
from typing import TypedDict, Annotated
from typing_extensions import TypedDict

# Get the API key
api_key = set_openai_key()
print(api_key)

llm = ChatOpenAI(
    model_name="gpt-4",
    api_key=api_key
)

rag_chain = create_rag_system(llm)

# Define the state structure
class State(TypedDict):
    user_data: dict
    query: str
    response: str

# Update the functions to work with state
def process_data(state: State) -> State:
    processed_data = process_user_data(state['user_data'])
    state['processed_data'] = processed_data
    # generated_sleep_data = get_generated_sleep_data()
    # state['processed_data'] = generated_sleep_data
    return state

def generate_health_schedule(state: State) -> State:
    system_message = SystemMessage(content="You are a knowledgeable assistant specializing in sleep science and health optimization. If the user provided his or her own sleep data, answer questions with some personalized health and sleep related recommendations and mention how to improve those data.")
    # Create a message list with the system message followed by the user query
    # Combine the system message content with the user query
    # generated_sleep_data = get_generated_sleep_data()
    sleep_data = convert_sleep_data_to_prompt('documents/sleep_data_minutes.csv')
    print("------sleep data------")
    print(sleep_data)
    print("------------")
    combined_query = f"{system_message.content}\n\n{sleep_data}\n\n{state['query']}"

    response = rag_chain.invoke(combined_query)
    state['response'] = response
    return state

# Create the graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("process_data", process_data)
workflow.add_node("generate_health_schedule", generate_health_schedule)

# Add edges
workflow.set_entry_point("process_data")
workflow.add_edge("process_data", "generate_health_schedule")
workflow.set_finish_point("generate_health_schedule")

# Compile the graph
app = workflow.compile()

# Example usage
user_profile = {
    'sleep_quality': [6.5, 7, 8, 6, 7.5],
    'steps': [10000, 12000, 9500, 11000, 12500],
    'heart_rate': [65, 70, 68, 72, 69]
}
# user_query = "Create a wellness plan for improving sleep quality and menstrual cycle health."
user_query = "How can I improve my sleep quality?"
# user_query = "Do I have enough deep sleep and REM? How can I improve it?"

# Run the graph with initial state
initial_state = State(
    user_data=user_profile,
    query=user_query,
    response=""
)

# Execute the workflow
final_state = app.invoke(initial_state)

print("Personalized Health Schedule with RAG:", final_state['response'])

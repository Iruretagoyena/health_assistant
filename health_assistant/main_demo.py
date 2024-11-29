# main_demo.py

import os
from typing import TypedDict, List
from datetime import datetime
from langchain.schema import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from health_assistant.config import set_openai_key
from health_assistant.rag_system import create_rag_system
from health_assistant.data_processing import process_user_data, convert_sleep_data_to_prompt

# Define state structures
class SleepMetrics(TypedDict):
   deep_sleep_percentage: float
   rem_percentage: float
   sleep_efficiency: float
   wake_episodes: List[str]
   total_sleep_time: float

class UserPreferences(TypedDict):
   bedtime: str
   wake_time: str
   work_schedule: str
   exercise_time: str
   sleep_issues: List[str]

class ConversationState(TypedDict):
   stage: str
   schedule_created: bool
   user_preferences: UserPreferences
   collecting_preferences: bool
   current_question: str

class State(TypedDict):
   user_data: dict
   query: str
   response: str
   conversation_state: ConversationState
   insights: List[str]

# Initialize system
api_key = set_openai_key()
llm = ChatOpenAI(model_name="gpt-4", api_key=api_key)
rag_chain = create_rag_system(llm)

def analyze_sleep_data(data: dict) -> List[str]:
   """
   TODO: Replace with actual sleep data analysis
   Currently using mock data for demonstration
   """
   deep_sleep = data.get('deep_sleep_percentage', 15.0)
   efficiency = data.get('sleep_efficiency', 85.0)
   wake_episodes = data.get('wake_episodes', ["2:00 AM"])[0]
   
   insights = []
   insights.append(f"Your deep sleep is {deep_sleep}% (optimal range: 20-23%)")
   insights.append(f"Your sleep efficiency is at {efficiency}%, which could be improved")
   insights.append(f"You have frequent wake episodes around {wake_episodes}")
   
   return insights

def process_data(state: State) -> State:
   """First agent: Process and analyze sleep data"""
   state['insights'] = analyze_sleep_data(state['user_data'])
   return state

def retrieve_knowledge(state: State) -> State:
   """Second agent: Get relevant sleep science knowledge"""
   sleep_data = convert_sleep_data_to_prompt('documents/sleep_data_minutes.csv')
   system_message = SystemMessage(content="You are a sleep expert. Using the sleep science knowledge base, provide evidence-based insights.")
   
   query = f"{system_message.content}\n\n{sleep_data}\n\n{state['query']}"
   knowledge = rag_chain.invoke(query)
   state['knowledge'] = knowledge
   return state

def generate_response(state: State) -> State:
   """Third agent: Generate personalized response"""
   stage = state['conversation_state']['stage']
   
   if stage == "initial":
       # Initial analysis response
       response = "Based on your sleep data:\n\n"
       for insight in state['insights']:
           response += f"• {insight}\n"
       response += "\nWould you like me to create a personalized sleep schedule?"
       state['conversation_state']['stage'] = "awaiting_schedule_confirmation"
       
   elif stage == "awaiting_schedule_confirmation":
       if "yes" in state['query'].lower():
           response = "Great! To create your personalized schedule, I need to know:\nWhat's your preferred bedtime?"
           state['conversation_state']['stage'] = "collecting_bedtime"
           
   elif stage == "collecting_bedtime":
       state['conversation_state']['user_preferences']['bedtime'] = state['query']
       response = "What time would you like to wake up?"
       state['conversation_state']['stage'] = "collecting_waketime"
       
   elif stage == "collecting_waketime":
       state['conversation_state']['user_preferences']['wake_time'] = state['query']
       response = "When do you usually exercise, or when would you prefer to exercise?"
       state['conversation_state']['stage'] = "collecting_exercise"
       
   elif stage == "collecting_exercise":
       state['conversation_state']['user_preferences']['exercise_time'] = state['query']
       response = generate_schedule(state['conversation_state']['user_preferences'], state['insights'])
       state['conversation_state']['stage'] = "schedule_created"
       
   else:
       response = state['knowledge']
   
   state['response'] = response
   return state

def generate_schedule(preferences: dict, insights: List[str]) -> str:
   """Generate schedule using RAG and user preferences"""
   system_message = SystemMessage(content="""Create a personalized sleep schedule that:
   1. Follows sleep science principles
   2. Addresses their sleep patterns
   3. Includes scientific reasoning for key recommendations
   Keep it concise but informative.""")
   
   query = f"""
   User sleep insights: {insights}
   Preferences:
   - Bedtime: {preferences.get('bedtime')}
   - Wake time: {preferences.get('wake_time')}
   - Exercise: {preferences.get('exercise_time')}
   
   Create a personalized sleep schedule with scientific reasoning.
   """
   
   response = rag_chain.invoke(f"{system_message.content}\n\n{query}")
   return f"{response}\n\nWould you like me to set up reminders for these times?"

# Create workflow
workflow = StateGraph(State)

# Add nodes
workflow.add_node("process_data", process_data)
workflow.add_node("retrieve_knowledge", retrieve_knowledge)
workflow.add_node("generate_response", generate_response)

# Add edges
workflow.set_entry_point("process_data")
workflow.add_edge("process_data", "retrieve_knowledge")
workflow.add_edge("retrieve_knowledge", "generate_response")
workflow.set_finish_point("generate_response")

# Compile graph
app = workflow.compile()

def run_demo():
   """Run interactive demo with the agent workflow"""
   print("\n=== Sleep Health Assistant Demo ===\n")
   
   initial_state = State(
       user_data={
           'deep_sleep_percentage': 15.0,
           'sleep_efficiency': 85.0,
           'wake_episodes': ["2:00 AM"]
       },
       query="How can I improve my sleep quality?",
       response="",
       conversation_state={
           "stage": "initial",
           "schedule_created": False,
           "user_preferences": {},
           "collecting_preferences": False,
           "current_question": ""
       },
       insights=[]
   )
   
   # Run the first interaction
   state = app.invoke(initial_state)
   print("Assistant:", state['response'])
   
   # Example interactions to demonstrate workflow
   sample_inputs = [
       "Yes, please create a schedule",
       "10:30 PM",
       "7:00 AM",
       "Morning"
   ]
   
   # Process each interaction
   for user_input in sample_inputs:
       print("\nUser:", user_input)
       state['query'] = user_input
       state = app.invoke(state)
       print("\nAssistant:", state['response'])
       
       # If schedule is created, show example notification
       if state['conversation_state']['stage'] == "schedule_created":
           print("\n=== Example Follow-up (Day 3) ===")
           print("Assistant: Great progress! I notice you've maintained your sleep schedule for 3 days.")
           print("Would you like to see your sleep metrics or adjust your schedule?")
           break

if __name__ == "__main__":
   run_demo()
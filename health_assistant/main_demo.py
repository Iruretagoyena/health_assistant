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
   user_metrics: dict
   query: str
   response: str
   conversation_state: ConversationState
   insights: List[str]

# Initialize system
api_key = set_openai_key()
llm = ChatOpenAI(model_name="gpt-4", api_key=api_key)
rag_chain = create_rag_system(llm)

def analyze_sleep_data(sleep_data, user_metrics):
    """Analyze sleep data and provide insights"""
    insights = []
    # print("Debug - Starting sleep data analysis")
    
    # Sleep duration analysis
    if sleep_data['total_sleep_time'] < 7:
        insights.append("You're getting less than the recommended 7-9 hours of sleep")
    elif sleep_data['total_sleep_time'] > 9:
        insights.append("You're sleeping longer than the recommended 7-9 hours")
    else:
        insights.append(f"Your sleep duration ({sleep_data['total_sleep_time']} hours) is within the recommended 7-9 hours range")
    
    # Age-specific insights
    age = user_metrics['age']
    if age > 65:
        if sleep_data['total_sleep_time'] < 7:
            insights.append("For your age group (65+), 7-8 hours of sleep is recommended")
        else:
            insights.append("Your sleep duration is appropriate for your age group (65+)")
    elif age < 18:
        if sleep_data['total_sleep_time'] < 8:
            insights.append("For your age group, 8-10 hours of sleep is recommended")
        else:
            insights.append("Your sleep duration is appropriate for your age group (under 18)")
    
    # Sleep quality insights
    if sleep_data['deep_sleep_percentage'] < 15:
        insights.append("Your deep sleep percentage is below optimal (15-25%)")
    else:
        insights.append(f"Your deep sleep percentage ({sleep_data['deep_sleep_percentage']}%) is within the optimal range of 15-25%")
    
    if sleep_data['rem_percentage'] < 20:
        insights.append("Your REM sleep percentage is below optimal (20-25%)")
    else:
        insights.append(f"Your REM sleep percentage ({sleep_data['rem_percentage']}%) is within the optimal range of 20-25%")
    
    if sleep_data['sleep_efficiency'] < 85:
        insights.append("Your sleep efficiency is below optimal (>85%)")
    else:
        insights.append(f"Your sleep efficiency ({sleep_data['sleep_efficiency']}%) is good (optimal is >85%)")
    
    # Wake episodes analysis
    if sleep_data['wake_episodes']:
        insights.append(f"You had wake episodes at: {', '.join(sleep_data['wake_episodes'])}")
    else:
        insights.append("You had no recorded wake episodes during your sleep")
    
    print("Debug - Generated insights:", insights)
    return insights

def process_data(state: State) -> State:
   """First agent: Process and analyze sleep data"""
#    print("Debug - Starting process_data")
#    print("Debug - User Data:", state['user_data'])
#    print("Debug - User Metrics:", state['user_metrics'])
   insights = analyze_sleep_data(state['user_data'], state['user_metrics'])
#    print("Debug - Insights after analysis:", insights)
   state['insights'] = insights
#    print("Debug - State insights after assignment:", state['insights'])
   return state

def retrieve_knowledge(state: State) -> State:
   """Second agent: Get relevant sleep science knowledge"""
   print(">>> Debug - Starting retrieve_knowledge")
#    print("Debug - State insights in retrieve:", state['insights'])
#    sleep_data = convert_sleep_data_to_prompt('documents/sleep_data_minutes.csv')
   sleep_data = "\n".join(state['insights'])
   system_message = SystemMessage(content="You are a sleep expert. Using the sleep science knowledge base, provide evidence-based insights.")
   question = "Based on the knowledge and user data, provide some analysis and recommendations."
   query = f"{system_message.content}\n\n{state['user_metrics']}\n\n{state['user_data']}\n\n{sleep_data}\n\n{question}"
   print(">>> Debug - Query in retrieve_knowledge:", query)
   knowledge = rag_chain.invoke(query)
#    print(">>>>> Debug - knowledge:", knowledge)
   state['knowledge'] = knowledge['result']
   print(">>>>> Debug - retrieve knowledge state: ", state)
#    print(">>> Debug - Knowledge:", knowledge)
   return state

def is_affirmative_response(user_input: str, llm: ChatOpenAI) -> bool:
    """
    Use OpenAI to determine if user's response is affirmative (yes) or negative (no).
    Returns True for yes, False for no.
    """
    prompt = f"""Determine if this response means 'yes' or 'no'. 
    Response: "{user_input}"
    Answer with only 'yes' or 'no'."""
    
    response = llm.invoke(prompt).content.strip().lower()
    return response == "yes"

def standardize_time_format(time_input: str, llm: ChatOpenAI) -> str:
    """
    Convert various time formats to standard 12-hour format (HH:MM AM/PM)
    Examples:
    - '7 in the morning' -> '7:00 AM'
    - 'half past 8 pm' -> '8:30 PM'
    - '23:00' -> '11:00 PM'
    """
    prompt = f"""Convert this time to standard 12-hour format (HH:MM AM/PM).
    Time: "{time_input}"
    Answer with only the time in HH:MM AM/PM format."""
    
    response = llm.invoke(prompt).content.strip()
    return response

def generate_response(state: State) -> State:
   """Third agent: Generate personalized response"""
   print(">>> Debug - Starting generate_response")
   print(">>> Debug - State in generate:", str(state))
   stage = state['conversation_state']['stage']

   if stage == "initial":
       is_affirmative = is_affirmative_response(state['query'], llm)
       if is_affirmative == False:
        #    print(">>> Inside False condition")
           print(">>> 2 Debug - state['knowledge'] in generate_response:", state['knowledge'])
           state['response'] = state['knowledge']
           state['conversation_state']['stage'] = "general_analysis"
           return state
       # Initial analysis response
       response = "Based on your sleep data:\n\n"
       for insight in state['insights']:
           response += f"• {insight}\n"
       response += "\nWould you like me to create a personalized sleep schedule?"
       state['conversation_state']['stage'] = "awaiting_schedule_confirmation"
       
   elif stage == "awaiting_schedule_confirmation":
       print(">>> debug - state = awaiting_schedule_confirmation")
       is_affirmative = is_affirmative_response(state['query'], llm)
       if is_affirmative:
           response = "Great! To create your personalized schedule, I need to know:\nWhat's your preferred bedtime?"
           state['conversation_state']['stage'] = "collecting_bedtime"
       else:
           state['response'] = state['knowledge']
           state['conversation_state']['stage'] = "general_analysis"
           return state

   elif stage == "collecting_bedtime":
       print(">>> debug - state = collecting_bedtime")
       if 'user_preferences' not in state['conversation_state']:
           state['conversation_state']['user_preferences'] = {}
           
       standardized_time = standardize_time_format(state['query'], llm)
       state['conversation_state']['user_preferences']['bedtime'] = standardized_time
       response = "What time would you like to wake up?"
       state['conversation_state']['stage'] = "collecting_waketime"
       
   elif stage == "collecting_waketime":
       print(">>> debug - state = collecting_waketime")
       standardized_time = standardize_time_format(state['query'], llm)
       state['conversation_state']['user_preferences']['wake_time'] = standardized_time
       response = "When do you usually exercise, or when would you prefer to exercise?"
       state['conversation_state']['stage'] = "collecting_exercise"
       
   elif stage == "collecting_exercise":
       state['conversation_state']['user_preferences']['exercise_time'] = state['query']
       response = generate_schedule(state['conversation_state']['user_preferences'], state['insights'])
       state['conversation_state']['stage'] = "schedule_created"
   elif stage == "schedule_created":
       is_affirmative = is_affirmative_response(state['query'], llm)
       if is_affirmative:
           state['response'] = "Great! I've set up reminders for your schedule."
       else:
           state['response'] = "Alright, I won't set up reminders."
       state['conversation_state']['stage'] = "general_analysis"
       return state
   elif stage == "general_analysis":
    #    print(">>> debug - state = general_analysis")
       response = general_analysis(state)
    #    print(">>> debug - state = general_analysis response", response)
   else:
       print(">>> debug - state = else")
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
   return f"{response['result']}\n\nWould you like me to set up reminders for these times?"

def general_analysis(state: State) -> str:
   system_message = SystemMessage(content="""Answer users questions regarding health, but if the user asks something completely not related to health, you don't have to provide health-related answers.\n
   If possible, provide evidence-based answers:
   1. Follows sleep science principles
   2. Addresses their sleep patterns
   3. Includes scientific reasoning for key recommendations
   4. Mention where the information is coming from or cited. 
   Keep it concise but informative.""")
   query = "Some user information you can use when necessary, but you don't have to use it if not necessary.\n" + "\n".join(state['insights']) + "\n" + state['query']
   response = rag_chain.invoke(f"{system_message.content}\n\n{query}")
   return response['result']

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

def run(state: State):
    print(">>> Debug - Running workflow" + str(state))
    return app.invoke(state)

def run_demo():
   """Run interactive demo with the agent workflow"""
   print("\n=== Sleep Health Assistant Demo ===\n")
   
   initial_state = State(
       user_data={
           'deep_sleep_percentage': 15.0,
           'rem_percentage': 20.0,
           'sleep_efficiency': 85.0,
           'wake_episodes': ["2:00 AM"],
           'total_sleep_time': 7.0
       },
       user_metrics={
           'age': 30,
           'weight': 70,
           'height': 170
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
   print(">>> Assistant:", state['response'])
   
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
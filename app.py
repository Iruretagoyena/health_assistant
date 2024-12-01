import gradio as gr
import openai
import os
from health_assistant.main_demo import State, run, generate_response, retrieve_knowledge, process_data
import time

# Retrieve the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Welcome image URL (replace with an appropriate URL)
WELCOME_IMAGE_URL = "assets/larger_image.jpg"
HEADER_IMAGE_URL = "assets/header3.jpg"

# Create a client instance
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Add state management
class SessionState:
    def __init__(self):
        self.sleep_data = None
        self.user_metrics = None
        self.insights = None

state = SessionState()
rag_state = None

# Add this near the top of your file with other constants
MOCK_HEALTH_DATA = {
    "user_profile": {
        "age": 32,
        "weight": 68.5,  # in kg
        "height": 172,   # in cm
    },
    "sleep_metrics": {
        "deep_sleep_percentage": 18,
        "rem_percentage": 23,
        "sleep_efficiency": 87,
        "total_sleep_time": 7.5,  # in hours
        "wake_episodes": ["02:30", "04:15"]  # Sample wake times
    }
}

# Add loading image constant
# LOADING_IMAGE_URL = "assets/loading.jpg"  # Remove this line

def ask_rag_system(user_input, chat_history):
    global rag_state
    if not state.sleep_data:
        return chat_history + [(user_input, "Please provide your sleep data first.")], ""

    try:
        if rag_state is None:
            rag_state = State(
                user_data=state.sleep_data,
                user_metrics=state.user_metrics,
                query=user_input,
                conversation_state={
                    'stage': 'initial'
                },
                response="",
                insights=state.insights
            )
            rag_state = process_data(rag_state)
            rag_state = retrieve_knowledge(rag_state)
            rag_state = generate_response(rag_state)
            # rag_state = run(rag_state)
            # print(">>>>> Debug - rag_state after retrieve_knowledge:", rag_state)
            chat_history.append((user_input, rag_state['response']))

        else:
            rag_state["query"] = user_input
            rag_state = generate_response(rag_state)
            print(">>>>> Debug - rag_state after generate_response:", rag_state)
            chat_history.append((user_input, rag_state['response']))
        # Call run() with the state object and user input
        # rag_state["query"] = user_input
        # rag_state = run(rag_state)
        # response_text = rag_state.get('result', {}).get('response', rag_state.get('response', ''))
        # chat_history.append((user_input, rag_state['response']['result']))
    except Exception as e:
        chat_history.append((user_input, f"Error: {str(e)}"))

    return chat_history, ""

# Chatbot function to get responses from OpenAI's API
def ask_openai(user_input, chat_history):
    if not state.sleep_data:
        return chat_history + [(user_input, "Please provide your sleep data first.")], ""

    try:
        # Format messages properly, filtering out None values
        messages = [
            {"role": "system", "content": "Please answer questions about health and medicine, especially for sleeping, eating, and exercise."}
        ]
        
        # Add chat history, only including valid messages
        for msg, response in chat_history:
            if msg:  # Add user message if it exists
                messages.append({"role": "user", "content": str(msg)})
            if response:  # Add assistant response if it exists
                messages.append({"role": "assistant", "content": str(response)})
        
        # Add current user input
        messages.append({"role": "user", "content": str(user_input)})

        # Make API call
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        answer = response.choices[0].message.content.strip()
        chat_history.append((user_input, answer))
    except Exception as e:
        chat_history.append((user_input, f"Error: {str(e)}"))

    return chat_history, ""

def create_chat_interface():
    with gr.Column():
        # Add header image
        gr.Image(
            value=HEADER_IMAGE_URL,
            elem_classes="header-image",
            show_label=False,
            container=False,
            type="filepath"
        )
        gr.Markdown("## Chat with Health Assistant")  # Added title
        
        chatbot = gr.Chatbot(
            label="Chatbot",
            height=400,
            container=False,
            scale=1,
            elem_classes="full-width-chatbot"
        )
        user_input = gr.Textbox(
            label="Type your question here",
            placeholder="Ask a question..."
        )
        with gr.Row():
            submit_button = gr.Button("Ask", elem_classes="primary-button")
            clear_button = gr.Button("Clear Chat", elem_classes="clear-button")
        with gr.Row():
            back_to_input = gr.Button("Back", elem_classes="back-button")
    
    return chatbot, user_input, submit_button, clear_button, back_to_input

def create_sleep_input_interface():
    with gr.Column():
        gr.Image(
            value=HEADER_IMAGE_URL,
            elem_classes="header-image",
            show_label=False,
            container=False,
            type="filepath"
        )
        gr.Markdown("## User Information")
        with gr.Row():
            age = gr.Number(
                minimum=1, maximum=120, value=30,
                label="Age (years)"
            )
            weight = gr.Number(
                minimum=20, maximum=300, value=70,
                label="Weight (kg)"
            )
            height = gr.Number(
                minimum=100, maximum=250, value=170,
                label="Height (cm)"
            )
        
        gr.Markdown("## Sleep Data Analysis")
        with gr.Row():
            deep_sleep = gr.Slider(
                minimum=0, maximum=100, value=15,
                label="Deep Sleep Percentage (%)"
            )
            rem_sleep = gr.Slider(
                minimum=0, maximum=100, value=25,
                label="REM Sleep Percentage (%)"
            )
        with gr.Row():
            sleep_efficiency = gr.Slider(
                minimum=0, maximum=100, value=85,
                label="Sleep Efficiency (%)"
            )
            total_sleep = gr.Slider(
                minimum=0, maximum=12, value=7,
                step=0.5,
                label="Total Sleep Time (hours)"
            )
        with gr.Column():
            gr.Markdown("### Wake Episodes")
            time_options = [f"{str(h).zfill(2)}:00" for h in range(0, 9)]
            wake_times = gr.Dropdown(
                choices=time_options,
                label="Wake Episode Time",
                multiselect=True,
                value=None
            )
            gr.Markdown("*Select times when you typically wake up during night (midnight to 8 AM)*")
        analyze_button = gr.Button("Submit Sleep Data", elem_classes="primary-button")
        back_button = gr.Button("Back", elem_classes="back-button")
    return age, weight, height, deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times, analyze_button, back_button

def add_custom_css():
    return gr.HTML("""
        <style>
        /* Header image adjustments */
        .header-image {
            width: 80% !important;
            height: 300px !important;
            object-fit: cover !important;
            object-position: center 100% !important;
            margin: 0 auto !important;
            display: block !important;
        }

        /* Welcome image adjustments */
        .welcome-image {
            width: 80% !important;
            height: 400px !important;
            object-fit: cover !important;
            margin: 0 auto !important;
            display: block !important;
        }

        /* Existing button colors (unchanged) */
        .primary-button {
            background-color: #0EA5E9 !important;
            color: white !important;
        }
        .primary-button:hover {
            background-color: #0284C7 !important;
        }
        
        .secondary-button {
            background-color: #22C55E !important;
            color: white !important;
        }
        .secondary-button:hover {
            background-color: #16A34A !important;
        }
        
        .action-button {
            background-color: #E67E22 !important;
            color: white !important;
        }
        .action-button:hover {
            background-color: #D35400 !important;
        }
        
        .clear-button {
            background-color: #F87171 !important;
            color: white !important;
        }
        .clear-button:hover {
            background-color: #EF4444 !important;
        }
        
        .back-button {
            background-color: #64748B !important;
            color: white !important;
        }
        .back-button:hover {
            background-color: #475569 !important;
        }
        </style>
    """)

def show_initial_screen():
    return (
        gr.update(visible=True),   # Show initial_page
        gr.update(visible=False),  # Hide sleep_input_container
        gr.update(visible=False),  # Hide device_msg
        gr.update(visible=False)   # Hide chat_container
    )

def show_manual_input():
    return (
        gr.update(visible=False),  # Hide initial_page (which contains welcome image)
        gr.update(visible=True),   # Show sleep_input_container
        gr.update(visible=False),  # Hide device_msg
        gr.update(visible=False)   # Hide chat_container
    )

def show_device_connection():
    return (
        gr.update(visible=False),  # Hide initial_page
        gr.update(visible=False),  # Hide sleep_input_container
        gr.update(visible=True),   # Show device_msg
        gr.update(visible=False)   # Hide chat_container
    )

def show_loading_screen():
    return (
        gr.update(visible=False),  # Hide initial_page
        gr.update(visible=False),  # Hide sleep_input_container
        gr.update(visible=True),   # Show loading_container
        gr.update(visible=False)   # Hide chat_container
    )

def process_device_data():
    # Simulate device data processing using the mock data
    data = MOCK_HEALTH_DATA
    return (
        gr.update(visible=False),  # Hide sleep_input_container
        gr.update(visible=True),   # Show chat_container
        [[None, process_sleep_data(
            age=data["user_profile"]["age"],
            weight=data["user_profile"]["weight"],
            height=data["user_profile"]["height"],
            deep_sleep_pct=data["sleep_metrics"]["deep_sleep_percentage"],
            rem_pct=data["sleep_metrics"]["rem_percentage"],
            efficiency_pct=data["sleep_metrics"]["sleep_efficiency"],
            total_sleep_hrs=data["sleep_metrics"]["total_sleep_time"],
            wake_times_list=data["sleep_metrics"]["wake_episodes"]
        )]],
        gr.update(visible=False)   # Hide loading_container
    )

def process_sleep_data(age, weight, height, deep_sleep_pct, rem_pct, efficiency_pct, total_sleep_hrs, wake_times_list):
    global rag_state
    rag_state = None
    
    # Store raw metrics
    user_metrics = {
        'age': age,
        'weight': weight,
        'height': height,
        'bmi': round(weight / ((height/100) ** 2), 1)  # Calculate BMI
    }
    state.user_metrics = user_metrics
    
    # Store raw sleep data
    data = {
        'deep_sleep_percentage': deep_sleep_pct,
        'rem_percentage': rem_pct,
        'sleep_efficiency': efficiency_pct,
        'total_sleep_time': total_sleep_hrs,
        'wake_episodes': wake_times_list if wake_times_list else []
    }
    state.sleep_data = data
    
    # Analyze sleep data against standard ranges
    insights = []
    
    # Sleep duration analysis (7-9 hours recommended for adults)
    if total_sleep_hrs < 7:
        insights.append("You're getting less than the recommended 7-9 hours of sleep")
    elif total_sleep_hrs > 9:
        insights.append("You're getting more than the recommended 7-9 hours of sleep")
    else:
        insights.append("Your sleep duration is within the recommended 7-9 hours range")
    
    # Deep sleep analysis (15-25% is optimal)
    if deep_sleep_pct < 15:
        insights.append(f"Your deep sleep percentage ({deep_sleep_pct}%) is below the optimal range of 15-25%")
    elif deep_sleep_pct > 25:
        insights.append(f"Your deep sleep percentage ({deep_sleep_pct}%) is above the optimal range of 15-25%")
    else:
        insights.append(f"Your deep sleep percentage ({deep_sleep_pct}%) is within the optimal range of 15-25%")
    
    # REM sleep analysis (20-25% is optimal)
    if rem_pct < 20:
        insights.append(f"Your REM sleep percentage ({rem_pct}%) is below the optimal range of 20-25%")
    elif rem_pct > 25:
        insights.append(f"Your REM sleep percentage ({rem_pct}%) is above the optimal range of 20-25%")
    else:
        insights.append(f"Your REM sleep percentage ({rem_pct}%) is within the optimal range of 20-25%")
    
    # Sleep efficiency analysis (>85% is considered good)
    if efficiency_pct < 85:
        insights.append(f"Your sleep efficiency ({efficiency_pct}%) is below optimal (>85%)")
    else:
        insights.append(f"Your sleep efficiency ({efficiency_pct}%) is good (optimal is >85%)")
    
    # Wake episodes analysis
    if wake_times_list:
        insights.append(f"You had {len(wake_times_list)} wake episodes during your sleep at: {', '.join(wake_times_list)}")
    else:
        insights.append("You had no recorded wake episodes during your sleep")
    
    # BMI analysis
    bmi = user_metrics['bmi']
    if bmi < 18.5:
        insights.append(f"Your BMI ({bmi}) indicates you are underweight")
    elif 18.5 <= bmi < 25:
        insights.append(f"Your BMI ({bmi}) is within the healthy range")
    elif 25 <= bmi < 30:
        insights.append(f"Your BMI ({bmi}) indicates you are overweight")
    else:
        insights.append(f"Your BMI ({bmi}) indicates obesity")

    state.insights = insights
    
    # Return just the message string
    return (
        f"Sleep analysis summary:\n\n"
        f"Personal profile:\n"
        f"- Age: {user_metrics['age']} years, height: {user_metrics['height']} cm, weight: {user_metrics['weight']} kg\n"
        f"- BMI: {user_metrics['bmi']} ({next(insight for insight in insights if 'BMI' in insight).split('BMI')[1].strip()})\n\n"
        
        f"Sleep duration:\n"
        f"- {data['total_sleep_time']} hours - {next(insight for insight in insights if 'recommended 7-9 hours' in insight)}\n\n"
        
        f"Sleep quality breakdown:\n"
        f"- Deep sleep: {data['deep_sleep_percentage']}% - {next(insight for insight in insights if 'deep sleep percentage' in insight).split('Your deep sleep percentage')[1].split('is')[1].strip()}\n"
        f"- REM sleep: {data['rem_percentage']}% - {next(insight for insight in insights if 'REM sleep percentage' in insight).split('Your REM sleep percentage')[1].split('is')[1].strip()}\n"
        f"- Sleep efficiency: {data['sleep_efficiency']}% - {next(insight for insight in insights if 'sleep efficiency' in insight).split('Your sleep efficiency')[1].split('is')[1].strip()}\n"
        f"- Wake episodes: {next(insight for insight in insights if 'wake episodes' in insight).split('You had')[1].strip()}\n\n"
        
        # f"More detailed analysis:\n"
        # f"{rag_state['knowledge']}\n\n"

        "Would you like me to provide more science and evidence-based analysis, or create a personalized sleep schedule?"
    )

def simulate_loading_and_process():
    time.sleep(2)  # Simulate loading delay
    data = MOCK_HEALTH_DATA
    
    # Process data and get message
    message = process_sleep_data(
        age=data["user_profile"]["age"],
        weight=data["user_profile"]["weight"],
        height=data["user_profile"]["height"],
        deep_sleep_pct=data["sleep_metrics"]["deep_sleep_percentage"],
        rem_pct=data["sleep_metrics"]["rem_percentage"],
        efficiency_pct=data["sleep_metrics"]["sleep_efficiency"],
        total_sleep_hrs=data["sleep_metrics"]["total_sleep_time"],
        wake_times_list=data["sleep_metrics"]["wake_episodes"]
    )
    
    # Return updates for all components
    return [
        gr.update(visible=False),  # Hide sleep_input_container
        gr.update(visible=True),   # Show chat_container
        [(None, message)],         # Update chatbot with tuple
        gr.update(visible=False)   # Hide loading_container
    ]

# Main welcome page with large image
with gr.Blocks() as demo:
    add_custom_css()
    
    # Initial page with welcome image
    with gr.Column(elem_classes="initial-page", visible=True) as initial_page:
        gr.Markdown("# Your Personal Health Assistant")
        
        # Large image for welcome page only
        gr.Image(
            value=WELCOME_IMAGE_URL,
            elem_classes="welcome-image",
            show_label=False,
            container=False,
            type="filepath"
        )
        
        # Initial choice buttons
        with gr.Row(elem_classes="button-container", visible=True) as choice_buttons:
            manual_input_btn = gr.Button("Provide Sleep Data Manually", elem_classes="primary-button")
            connect_device_btn = gr.Button("Connect with Health Device", elem_classes="secondary-button")
    
    # Device message page
    with gr.Column(visible=False) as device_msg:
        gr.Image(
            value=HEADER_IMAGE_URL,
            elem_classes="header-image",
            show_label=False,
            container=False,
            type="filepath"
        )
        gr.Markdown("## Device Connection")
        gr.Markdown("The device connection feature is not implemented yet. Please use manual input instead.")
        back_to_main = gr.Button("Back", elem_classes="back-button")
    
    # Sleep data input container (hidden by default)
    with gr.Column(visible=False) as sleep_input_container:
        age, weight, height, deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times, analyze_button, back_button = create_sleep_input_interface()
    
    # Chat interface (hidden by default)
    with gr.Column(visible=False) as chat_container:
        chatbot, user_input, submit_button, clear_button, back_to_input = create_chat_interface()
    
    # Update loading screen container
    with gr.Column(visible=False) as loading_container:
        gr.Image(
            value=HEADER_IMAGE_URL,
            elem_classes="header-image",
            show_label=False,
            container=False,
            type="filepath"
        )
        gr.Markdown("## Connecting to Apple Health")
        gr.Markdown("Retrieving your sleep metrics and personal data...")
    
    # Event handlers
    manual_input_btn.click(
        show_manual_input,
        outputs=[initial_page, sleep_input_container, device_msg, chat_container]
    )

    # Update the connect device button click handler
    connect_device_btn.click(
        show_loading_screen,
        outputs=[initial_page, sleep_input_container, loading_container, chat_container]
    ).then(
        simulate_loading_and_process,
        outputs=[sleep_input_container, chat_container, chatbot, loading_container]
    )

    analyze_button.click(
        process_sleep_data,
        inputs=[age, weight, height, deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times],
        outputs=[sleep_input_container, chat_container, chatbot]
    )
    
    # Chat functionality
    submit_button.click(ask_rag_system, [user_input, chatbot], [chatbot, user_input])
    user_input.submit(ask_rag_system, [user_input, chatbot], [chatbot, user_input])
    
    def clear_chat():
        return [], ""
    
    clear_button.click(clear_chat, None, [chatbot, user_input])
    
    # Add event handler for back button
    back_button.click(
        show_initial_screen,
        outputs=[initial_page, sleep_input_container, device_msg, chat_container]
    )

    def show_sleep_input():
        return (
            gr.update(visible=True),   # Show sleep_input_container
            gr.update(visible=False),  # Hide chat_container
            []  # Clear chatbot
        )
    
    # Connect the back button click event
    back_to_input.click(
        fn=show_sleep_input,
        outputs=[sleep_input_container, chat_container, chatbot]
    )

    back_to_main.click(
        show_initial_screen,
        outputs=[initial_page, sleep_input_container, device_msg, chat_container]
    )

# Launch the app
demo.launch()

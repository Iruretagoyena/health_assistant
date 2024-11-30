import gradio as gr
import openai
import os
from health_assistant.main_demo import analyze_sleep_data

# Retrieve the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a client instance
client = openai.OpenAI()

# Chatbot function to get responses from OpenAI's API
def ask_openai(user_input, chat_history):
    if not openai.api_key:
        return chat_history + [(user_input, "API key is missing. Please set the OPENAI_API_KEY environment variable.")], ""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Please answer questions about health and medicine, especially for sleeping, eating, and exercise."}] + 
                     [{"role": "user", "content": message} for message, _ in chat_history] + 
                     [{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message.content.strip()
        chat_history.append((user_input, answer))
    except Exception as e:
        chat_history.append((user_input, f"Error: {str(e)}"))

    return chat_history, ""

def create_chat_interface():
    with gr.Column():
        chatbot = gr.Chatbot(label="Chatbot")
        user_input = gr.Textbox(
            label="Type your question here", 
            placeholder="Ask a question..."
        )
        with gr.Row():
            submit_button = gr.Button("Ask", variant="primary")
            clear_button = gr.Button("Clear Chat")
        
        # Move back button to bottom and make it full width
        with gr.Row():
            back_to_input = gr.Button(
                "← Back to Sleep Data", 
                size="lg",  # Make it larger
                scale=1,    # Take full width
                min_width=100,
                variant="secondary"  # Different style to distinguish from primary actions
            )
    
    return chatbot, user_input, submit_button, clear_button, back_to_input

def create_sleep_input_interface():
    # Create a container for all elements
    with gr.Column():
        # Remove back button from top
        
        # Sleep Analysis header
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
        
        # Container for wake episodes
        with gr.Column():
            gr.Markdown("### Wake Episodes")
            time_options = [f"{str(h).zfill(2)}:00" for h in range(24)]
            
            wake_times = gr.Dropdown(
                choices=time_options,
                label="Wake Episode Time",
                multiselect=True,
                value=None
            )
            
            gr.Markdown("*Select times when you typically wake up (if any)*")
        
        analyze_button = gr.Button("Submit Sleep Data", variant="primary")
        back_button = gr.Button("Back to Sleep Data", variant="secondary")
    
    return deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times, analyze_button, back_button

# Add some custom CSS to style the back button
def add_custom_css():
    return gr.HTML("""
        <style>
        .button-row {
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
        }
        .button-row button {
            flex: 1;
        }
        </style>
    """)

# Add a function to handle going back
def show_initial_screen():
    return (
        gr.update(visible=True),   # choice_buttons
        gr.update(visible=False),  # sleep_input_container
        gr.update(visible=False),  # device_msg
        gr.update(visible=False)   # chat_container
    )

with gr.Blocks() as demo:
    add_custom_css()
    gr.Markdown("# Your Personal Health Assistant")
    
    # Initial choice buttons
    with gr.Row(visible=True) as choice_buttons:
        manual_input_btn = gr.Button("Provide Sleep Data Manually")
        connect_device_btn = gr.Button("Connect with Health Device")
    
    # Device connection message (hidden by default)
    device_msg = gr.Markdown(
        "Device connection feature is not implemented yet.", 
        visible=False
    )
    
    # Sleep data input container (hidden by default)
    with gr.Column(visible=False) as sleep_input_container:
        deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times, analyze_button, back_button = create_sleep_input_interface()
    
    # Chat interface (hidden by default)
    with gr.Column(visible=False) as chat_container:
        chatbot, user_input, submit_button, clear_button, back_to_input = create_chat_interface()
        
        # Add custom CSS
        gr.HTML("""
            <style>
            .ask-button {
                background-color: #28a745 !important;
                border-color: #28a745 !important;
            }
            button.ask-button:hover {
                background-color: #218838 !important;
                border-color: #1e7e34 !important;
            }
            </style>
        """)
    
    def show_manual_input():
        return (
            gr.update(visible=False),  # choice_buttons
            gr.update(visible=True),   # sleep_input_container
            gr.update(visible=False),  # device_msg
            gr.update(visible=False)   # chat_container
        )

    def show_device_connection():
        return (
            gr.update(visible=False),  # choice_buttons
            gr.update(visible=False),  # sleep_input_container
            gr.update(visible=True),   # device_msg
            gr.update(visible=False)   # chat_container
        )
    
    def process_sleep_data(deep_sleep_pct, rem_pct, efficiency_pct, total_sleep_hrs, wake_times_list):
        data = {
            'deep_sleep_percentage': deep_sleep_pct,
            'rem_percentage': rem_pct,
            'sleep_efficiency': efficiency_pct,
            'total_sleep_time': total_sleep_hrs,
            'wake_episodes': wake_times_list if wake_times_list else []
        }
        
        insights = analyze_sleep_data(data)
        initial_message = "Based on your sleep data:\n" + "\n".join([f"- {insight}" for insight in insights])
        return (
            gr.update(visible=False),  # Hide sleep_input_container
            gr.update(visible=True),   # Show chat_container
            [[None, initial_message]]  # chatbot
        )
    
    # Event handlers
    manual_input_btn.click(
            show_manual_input,
        outputs=[choice_buttons, sleep_input_container, device_msg, chat_container]
    )

    connect_device_btn.click(
        show_device_connection,
        outputs=[choice_buttons, sleep_input_container, device_msg, chat_container]
    )

    analyze_button.click(
        process_sleep_data,
        inputs=[deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times],
        outputs=[sleep_input_container, chat_container, chatbot]
    )
    
    # Chat functionality
    submit_button.click(ask_openai, [user_input, chatbot], [chatbot, user_input])
    user_input.submit(ask_openai, [user_input, chatbot], [chatbot, user_input])
    
    def clear_chat():
        return [], ""
    
    clear_button.click(clear_chat, None, [chatbot, user_input])
    
    # Add event handler for back button
    back_button.click(
        show_initial_screen,
        outputs=[choice_buttons, sleep_input_container, device_msg, chat_container]
    )

    # Event handlers
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

# Launch the app
demo.launch()
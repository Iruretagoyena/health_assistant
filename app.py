import gradio as gr
import openai
import os
from health_assistant.main_demo import analyze_sleep_data

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

state = SessionState()

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
    return deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times, analyze_button, back_button

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
        deep_sleep, rem_sleep, sleep_efficiency, total_sleep, wake_times, analyze_button, back_button = create_sleep_input_interface()
    
    # Chat interface (hidden by default)
    with gr.Column(visible=False) as chat_container:
        chatbot, user_input, submit_button, clear_button, back_to_input = create_chat_interface()
    
    def process_sleep_data(deep_sleep_pct, rem_pct, efficiency_pct, total_sleep_hrs, wake_times_list):
        data = {
            'deep_sleep_percentage': deep_sleep_pct,
            'rem_percentage': rem_pct,
            'sleep_efficiency': efficiency_pct,
            'total_sleep_time': total_sleep_hrs,
            'wake_episodes': wake_times_list if wake_times_list else []
        }
        state.sleep_data = data  # Store the data in state
        insights = analyze_sleep_data(data)
        initial_message = "Based on your sleep data:\n" + "\n".join([f"- {insight}" for insight in insights])
        return (
            gr.update(visible=False),  # Hide sleep_input_container
            gr.update(visible=True),   # Show chat_container
            [[None, initial_message]]  # Initial chatbot message
        )
    
    # Event handlers
    manual_input_btn.click(
        show_manual_input,
        outputs=[initial_page, sleep_input_container, device_msg, chat_container]
    )

    connect_device_btn.click(
        show_device_connection,
        outputs=[initial_page, sleep_input_container, device_msg, chat_container]
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

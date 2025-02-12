import os
import gradio as gr
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

#load the environment variables
load_dotenv()

# Check for API token
if not os.getenv("HUGGINGFACE_API_TOKEN"):
    raise ValueError("Please set HUGGINGFACE_API_TOKEN in your .env file")

client = InferenceClient(
    token=os.getenv("HUGGINGFACE_API_TOKEN"),
    timeout=10
)

MODELS = {
    "gpt2": "⚡ GPT-2 - Fastest general responses",
    "microsoft/CodeGPT-small-py": "🐍 CodeGPT Small - Fast Python specialist",
    "Salesforce/codegen-350M-mono": "🚀 CodeGen (350M) - Quick code generation",
}

def respond(message, history, model_choice):
    try:
        response = client.text_generation(
            message,
            model=model_choice,
            max_new_tokens=150,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.15,
            do_sample=True,
            return_full_text=False,
        )
        return response
    except Exception as e:
        return f"❌ Error: {str(e)}\nTry selecting a different model."

# Create chatbot interface
with gr.Blocks() as interface:
    # Model selector
    model_choice = gr.Dropdown(
        choices=list(MODELS.keys()),
        value="gpt2",
        label="🔧 Select Model",
        info="Choose the AI model (faster models listed first)"
    )
    
    # Chatbot component
    chatbot = gr.Chatbot(
        height=500,  # Fixed height for scrolling
        show_copy_button=True,  # Enable copy button
        bubble_full_width=False,  # Makes it look more like a chat
    )
    
    # Message input
    msg = gr.Textbox(
        label="Ask your coding question",
        placeholder="Enter your programming question here...",
        lines=3
    )

    # Clear button
    clear = gr.ClearButton([msg, chatbot])

    # Handle message submission
    msg.submit(
        respond,
        inputs=[msg, chatbot, model_choice],
        outputs=[chatbot],
        queue=False
    )

# Launch the interface
interface.launch(
    share=True,
    cache_examples=True,
    show_error=True,
)
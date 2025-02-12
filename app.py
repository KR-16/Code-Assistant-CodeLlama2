import requests
import json
import gradio as gr
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

#load the environment variables
load_dotenv()

# Check for API token
if not os.getenv("HUGGINGFACE_API_TOKEN"):
    raise ValueError("Please set HUGGINGFACE_API_TOKEN in your .env file")

client = InferenceClient(
    token=os.getenv("HUGGINGFACE_API_TOKEN")
)

MODELS = {
    "gpt2": "GPT-2 (124M) - General purpose model",
    "facebook/opt-125m": "OPT (125M) - Good for text generation",
    "EleutherAI/pythia-160m": "Pythia (160M) - Good for code",
    "bigscience/bloom-560m": "BLOOM (560M) - Multilingual model",
    "microsoft/phi-1": "Phi-1 (1.3B) - Good for coding tasks"
}


# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }

# history = []

def generate_response(prompt, model_choice):
    try:
        response = client.text_generation(
            prompt,
            model=model_choice,
            max_new_tokens=400,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.15,
            do_sample=True
        )
        return response
    except Exception as e:
        return f"Error: {str(e)}\n Try with another model"
    
interface = gr.Interface(
    fn = generate_response,
    inputs = [
                gr.Textbox(
                    lines=20,
                    label="Let me know your questions!",
                    placeholder="You can tell me the question here..."
                ),
                gr.Dropdown(
                    choices=list(MODELS.keys()),
                    value="microsoft/phi-1",
                    label="Select Model",
                    info="Choose the model to use"
                )
            ],
            outputs = gr.Textbox(
                label="Response",
                lines=20,
                max_lines=40,
                show_copy_button=True,
                interactive=False,
                container=True,
                autoscroll=True,
                scale=2
                ),
    title="Code Assistant",
    description="An AI assistant that helps you with coding questions using various Hugging Face models.",
    theme="soft"
)
if __name__ == "__main__":
    interface.launch(
        share=False,
        show_error=True,
        server_port=int(os.getenv("PORT", 7860)),
        show_api=False
        )
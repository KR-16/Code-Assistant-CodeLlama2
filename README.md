
---
title: Your Project Name
emoji: 🚀
colorFrom: blue
colorTo: red
sdk: gradio  # or streamlit, static, docker
sdk_version: 3.50.2
app_file: app.py
pinned: false
---
# Code Assistant

A Gradio web application that helps with coding questions using various Hugging Face models.

## Models Available
- GPT-2 (124M) - General purpose model
- OPT (125M) - Good for text generation
- Pythia (160M) - Good for code
- BLOOM (560M) - Multilingual model
- Phi-1 (1.3B) - Good for coding tasks

## Setup
The app requires a HUGGINGFACE_API_TOKEN environment variable to be set.

## Features

- **Interactive Interface**: Users can input prompts and receive code-related responses in real-time.
- **Model Integration**: Utilizes the CodeLlama2 model for generating code suggestions and explanations.
- **History Tracking**: Keeps track of user prompts to provide contextually relevant responses.

## Requirements

To run this project, you need to have the following Python packages installed:

- `langchain`
- `gradio`

You can install the required packages using pip:

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/KR-16/Code-Assistant-CodeLlama2.git
   cd Code-Assistant-CodeLlama2
   ```

2. Start the application:

   ```bash
   python app.py
   ```

3. Open your web browser and navigate to `http://localhost:7860` to access the interface.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Acknowledgments

- Thanks to the developers of CodeLlama2 for providing the model that powers this application.

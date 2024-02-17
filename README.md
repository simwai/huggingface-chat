# Hugging Face Model Demo

> A Streamlit web app for interacting with Hugging Face's text generation models.

This project is a simple web application that allows users to load pre-trained models from Hugging Face's model hub and generate text based on a user-provided prompt. It's built using Streamlit and the `transformers` library.

[![VS Code](https://img.shields.io/badge/IDE-VS%20Code-6A0DAD.svg)](https://code.visualstudio.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


## Features

- Load Hugging Face models dynamically by specifying the model name.
- Generate text using the loaded model with a custom prompt.
- Keep a history of loaded models for quick access.

## Installation

Make sure you have Python 3.6 or later installed. You can then install the dependencies with pip:

1. `python -m venv .venv`

2. Windows: `.venv\Scripts\activate`<br>
   Linux: `source .venv/bin/activate`

3. `pip install -r requirements`

## Usage

To run the app, navigate to the directory containing `index.py` and run:

`streamlit run index.py`

The Streamlit web interface should open in your default web browser, where you can interact with the model.

## API

The app is structured around a `MyPipeline` class that handles the loading and interaction with the Hugging Face models.

### `MyPipeline.load_model_and_tokenizer(model_name: str)`

Load the specified model and tokenizer from Hugging Face's model hub.

#### Parameters

- `model_name` - Type: `str`. The name of the model to load.

### `MyPipeline.analyze_text(text: str)`

Generate text using the loaded model based on the provided prompt.

#### Parameters

- `text` - Type: `str`. The prompt text to feed into the model.

## Contributing

Contributions are welcome! If you have a suggestion or an issue, please open an issue on the repository to discuss it.

## License

MIT © [simwai](https://simwai.taplink.ws)
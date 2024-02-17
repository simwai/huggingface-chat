from typing import Iterator
import streamlit as st
from transformers import pipeline


class TextAnalyzer:
    """A Streamlit application for text analysis using Hugging Face models."""

    def __init__(self, st) -> None:
        self.st = st

        self.st.title("Hugging Face Model Demo")
        self._initialize_model_history()

        self.load_gui()

    def _initialize_model_history(self) -> None:
        """Initialize the model history in the session state."""
        if "model_history" not in self.st.session_state:
            self.st.session_state["model_history"] = []

    def load_model(self, model_name: str) -> None:
        """Load a Hugging Face model."""
        try:
            self.st.session_state["pipeline"] = pipeline(
                "text-generation",
                model=model_name,
                torch_dtype="auto",
                device_map="auto",
            )
            self.st.session_state["max_length"] = self._get_max_length()
            self.st.success(f"Loaded model: {model_name}")
        except Exception as e:
            self.st.error(f"Failed to load model: {e}")

    def _get_max_length(self) -> int:
        """Get the maximum length from the model's configuration."""
        return self.st.session_state["pipeline"].model.config.max_position_embeddings

    def analyze_text(self, text: str) -> Iterator[str]:
        """Analyze the input text using the loaded model."""
        if not self._is_model_loaded() or not self._is_text_valid(text):
            return

        try:
            for i, output in enumerate(self._generate_text(text)):
                yield output["generated_text"]
        except Exception as e:
            self.st.error(f"An error occurred during text analysis: {e}")

    def _is_model_loaded(self) -> bool:
        """Check if the model pipeline is loaded."""
        if "pipeline" not in self.st.session_state:
            self.st.error("Model pipeline is not loaded. Please load the model first.")
            return False
        return True

    def _is_text_valid(self, text: str) -> bool:
        """Check if the input text is valid."""
        max_length = self.st.session_state["max_length"]
        if len(text) > max_length:
            self.st.error(
                f"The input text is too long. Maximum length allowed is {max_length} characters."
            )
            return False
        return True

    def _generate_text(self, text: str):
        """Generate text using the loaded model."""
        return self.st.session_state["pipeline"](
            text,
            max_length=self.st.session_state["max_length"],
            return_full_text=False,
        )

    def load_gui(self) -> None:
        """Load the graphical user interface."""
        model_name = self._get_model_name_from_user()
        if self.st.button("Load Model"):
            self._update_model_history(model_name)
            self.load_model(model_name)

        self._display_model_history()

        input_text = self._get_input_text_from_user()
        if self.st.button("Send"):
            if self._is_same_model_loaded(model_name):
                self.st.write("Analyzing...")
                self._display_generated_text(input_text)

    def _get_model_name_from_user(self) -> str:
        """Get the model name from the user."""
        return self.st.text_input(
            "Enter the name of the Hugging Face model",
            "teknium/OpenHermes-2.5-Mistral-7B",
        )

    def _update_model_history(self, model_name: str) -> None:
        """Update the model history."""
        if model_name not in self.st.session_state["model_history"]:
            self.st.session_state["model_history"].append(model_name)
            self.st.session_state["model"] = model_name

    def _display_model_history(self) -> None:
        """Display the model history."""
        if self.st.session_state["model_history"]:
            selected_model = self.st.selectbox(
                "Or select a model from history",
                options=self.st.session_state["model_history"],
            )
            if self.st.button("Load Model from History"):
                self.load_model(selected_model)

    def _get_input_text_from_user(self) -> str:
        """Get the input text from the user."""
        return self.st.text_area("Enter text to analyze", "Enter text here...")

    def _is_same_model_loaded(self, model_name: str) -> bool:
        """Check if the same model is loaded."""
        if self.st.session_state.get("model") != model_name:
            self.st.error("Please load a model first.")
            return False
        return True

    def _display_generated_text(self, input_text: str) -> None:
        """Display the generated text."""
        for output in self.analyze_text(input_text):
            self.st.write(output)


def main():
    """Main function to run the Streamlit application."""
    TextAnalyzer(st)


if __name__ == "__main__":
    main()


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os


class QwenModel:
    def __init__(self, model_name="Qwen/Qwen3-4B-Thinking-2507", cache_dir=None):
        if cache_dir is None:
            # Default to a local directory in the modeling folder
            cache_dir = os.path.join(os.path.dirname(__file__), "qwen3-4b-thinking-2507")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)

    def generate(self, prompt, max_length=50):
        if not prompt.strip():
            return ""
        inputs = self.tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


# Utility: Pre-download and cache the model for quick loading
if __name__ == "__main__":
    print("Downloading and caching Qwen3-4B-Thinking-2507 model and tokenizer...")
    QwenModel()
    print("Done. Model and tokenizer are cached locally.")
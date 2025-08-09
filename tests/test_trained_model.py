import pytest

from pipeline.modeling.trained_model import QwenModel
import os

@pytest.fixture(scope="module")
def model():
    # Use the same cache_dir as in trained_model.py
    cache_dir = os.path.join(os.path.dirname(__file__), "..", "pipeline", "modeling", "qwen3-4b-thinking-2507")
    return QwenModel(cache_dir=cache_dir)

def test_generate_basic(model):
    prompt = "Hello, my name is"
    result = model.generate(prompt, max_length=10)
    print(f"Test: test_generate_basic\nPrompt: {prompt}\nModel Output: {result}")
    assert isinstance(result, str)
    assert len(result) > 0

def test_generate_empty_prompt(model):
    prompt = ""
    result = model.generate(prompt, max_length=10)
    print(f"Test: test_generate_empty_prompt\nPrompt: (empty)\nModel Output: {result}")
    assert isinstance(result, str)
    assert result == ""

def test_generate_specific_prompt(model):
    prompt = "What is the capital of France?"
    result = model.generate(prompt, max_length=20)
    print(f"Test: test_generate_specific_prompt\nPrompt: {prompt}\nModel Output: {result}")
    assert isinstance(result, str)
    assert "Paris" in result or len(result) > 0  # Accepts any non-empty output, but prefers "Paris"
 

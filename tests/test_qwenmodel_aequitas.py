import pandas as pd
import pytest
from pipeline.modeling.trained_model import QwenModel
import os
from pipeline.evaluation.bias_audit import run_aequitas_audit

def classify_with_qwen(model, prompt):
    result = model.generate(prompt, max_length=20)
    print(f"Prompt: {prompt}\nModel Output: {result}")
    classification = 1 if "Paris" in result else 0
    print(f"Classified as: {classification} (1 if 'Paris' in output, else 0)")
    return classification

def test_qwenmodel_aequitas_audit():
    # Example data for audit
    data = {
        "prompt": [
            "What is the capital of France?",
            "What is the capital of Germany?"
        ],
        "label_value": [1, 0],  # 1 if Paris expected, 0 otherwise
        "sex": ["male", "female"]  # Example group attribute
    }
    df = pd.DataFrame(data)

    cache_dir = os.path.join(os.path.dirname(__file__), "..", "pipeline", "modeling", "qwen3-4b-thinking-2507")
    model = QwenModel(cache_dir=cache_dir)

    # Show prompt, output, and classification for each row
    df["score"] = df["prompt"].apply(lambda x: classify_with_qwen(model, x))


    fair_df = run_aequitas_audit(
        df=df,
        label_col="label_value",
        score_col="score",
        attr_cols=["sex"],
        output_path="tests/test_output/aequitas_qwen_report.csv"
    )
    print("\nAequitas Audit Results:")
    print(fair_df)

    assert "attribute_name" in fair_df.columns
    assert "attribute_value" in fair_df.columns
    assert "Statistical Parity" in fair_df.columns
    assert not fair_df.empty
    print("\nQwenModel Aequitas audit ran successfully:")

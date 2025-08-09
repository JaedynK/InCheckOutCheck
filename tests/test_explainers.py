import pytest
import os
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# === Fixtures ===

@pytest.fixture(scope="module")
def synthetic_data():
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    feature_names = [f"feature_{i}" for i in range(X.shape[1])]
    class_names = ["class_0", "class_1"]

    X_df = pd.DataFrame(X, columns=feature_names)
    y_series = pd.Series(y)

    model = RandomForestClassifier().fit(X_df, y_series)

    return model, X_df, y_series, feature_names, class_names

# === SHAP Test ===

def test_shap_explainer_runs(synthetic_data):
    model, X_df, _, _, _ = synthetic_data
    from pipeline.explainability.shap_explainer import explain_with_shap

    output_file = "shap_test_output.json"
    summary = explain_with_shap(model, X_df[:10], output_path=output_file)

    assert isinstance(summary, dict)
    assert os.path.exists(output_file)
    assert "feature_0" in summary  # Check at least one expected key

    os.remove(output_file)

# === LIME Test ===

def test_lime_explainer_runs(synthetic_data):
    model, X_df, _, feature_names, class_names = synthetic_data
    from pipeline.explainability.lime_explainer import explain_with_lime

    output_file = "lime_test_output.txt"
    explanation = explain_with_lime(
        model=model,
        X_train=X_df,
        X_instance=X_df.iloc[0],
        feature_names=feature_names,
        class_names=class_names,
        output_path=output_file
    )

    assert hasattr(explanation, "as_list")
    assert os.path.exists(output_file)

    with open(output_file, "r") as f:
        lines = f.readlines()
        assert any("feature" in line for line in lines)

    os.remove(output_file)
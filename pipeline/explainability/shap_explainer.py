import shap
import pandas as pd

def explain_with_shap(model, X_sample, output_path="shap_values.json"):
    explainer = shap.Explainer(model, X_sample)
    shap_values = explainer(X_sample)

    # Save global feature importance
    summary = shap_values.values.mean(axis=0)
    summary_dict = dict(zip(X_sample.columns, summary.tolist()))

    pd.Series(summary_dict).to_json(output_path, indent=2)

    return summary_dict
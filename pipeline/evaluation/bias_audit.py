# === Imports ===
from fairlearn.metrics import MetricFrame, selection_rate, equalized_odds_difference
from sklearn.metrics import accuracy_score
import pandas as pd
import json
from aequitas.group import Group
from aequitas.fairness import Fairness
from aequitas.bias import Bias

# === Core Audit Function ===
def run_bias_audit(model, X, y, sensitive_feature, output_path="audit_report.json"):
    """Main audit using Fairlearn's MetricFrame."""
    y_pred = model.predict(X)
    frame = MetricFrame(
        metrics={'accuracy': accuracy_score, 'selection_rate': selection_rate},
        y_true=y, y_pred=y_pred,
        sensitive_features=sensitive_feature
    )
    report = {
        "overall_accuracy": frame.overall["accuracy"],
        "selection_rate_by_group": frame.by_group["selection_rate"].to_dict(),
        "accuracy_by_group": frame.by_group["accuracy"].to_dict(),
        "equalized_odds_diff": equalized_odds_difference(y, y_pred, sensitive_feature)
    }
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
    return report

# Aequitas audit ===
def run_aequitas_audit(
    df: pd.DataFrame,
    label_col: str = "label_value",
    score_col: str = "score",
    attr_cols: list = ["sex"],
    output_path: str = "aequitas_fairness_report.csv"
):
    if label_col not in df.columns or score_col not in df.columns:
        raise ValueError(f"DataFrame must include '{label_col}' and '{score_col}' columns.")

    # Rename columns for Aequitas
    df = df.rename(columns={label_col: "label_value", score_col: "score"})

    # Step 1: Crosstabs
    g = Group()
    xtab, _ = g.get_crosstabs(df, attr_cols=attr_cols)

    # Step 2: Bias analysis
    b = Bias()
    bias = b.get_disparity_predefined_groups(
        xtab,
        original_df=df,
        ref_groups_dict = {col: df[col].mode()[0] for col in attr_cols},
        alpha=0.05,
        mask_significance=True
    )

    # Step 3: Fairness analysis
    f = Fairness()
    fair = f.get_group_value_fairness(bias)  # ✅ this now works because 'ppr_disparity' exists

    # Output
    fair.to_csv(output_path, index=False)
    return fair

# === Optional Add-on: Visual reports ===
def visualize_bias_metrics(frame: MetricFrame):
    """Visualize group-level metrics (optional)"""
    frame.by_group.plot(kind="bar", subplots=True)
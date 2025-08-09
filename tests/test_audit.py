import sys
import os
# Make sure the project root is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline.data_prep.load_data import load_data
from pipeline.evaluation.bias_audit import run_aequitas_audit
from sklearn.linear_model import LogisticRegression


def test_aequitas_bias_audit():
    # Load and clean the data
    df = load_data("tests/test_data/sample_data.csv")
    print("Loaded data sample:")
    print(df.head())

    # Create binary label column
    df["label_value"] = (df["income"].str.strip() == ">50K").astype(int)
    print("Label distribution:")
    print(df["label_value"].value_counts())

    # Train a simple model
    X = df.select_dtypes(include="number")
    y = df["label_value"]
    model = LogisticRegression(max_iter=1000).fit(X, y)

    # Add predicted column
    df["score"] = model.predict(X)
    print("Predictions (first 10):")
    print(df[["score", "label_value", "sex"]].head(10))

    # ✅ Aequitas expects lowercase 'label_value' and 'score'
    df = df.rename(columns={"label_value": "label_value", "score": "score"})

    # Run Aequitas bias audit
    fair_df = run_aequitas_audit(
        df=df,
        label_col="label_value",
        score_col="score",
        attr_cols=["sex"],
        output_path="tests/test_output/aequitas_test_report.csv"
    )

    print("\nAequitas Audit Results:")
    print(fair_df)

    # Basic assertions
    assert "attribute_name" in fair_df.columns
    assert "attribute_value" in fair_df.columns
    assert "Statistical Parity" in fair_df.columns
    assert not fair_df.empty

    print("\nAequitas audit ran successfully:")


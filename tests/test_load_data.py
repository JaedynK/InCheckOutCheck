
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd

from pipeline.data_prep.load_data import load_data
def test_sample_data_loads():
    path = "tests/test_data/sample_data.csv"  # Keep this relative to your repo root
    df = load_data(path)

    # Basic type and content check
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.shape[1] > 1
    assert df.shape[0] > 1

    # Optional: flag bad headers (e.g., if they look like data)
    suspicious = all(str(col).strip().isdigit() for col in df.columns[:3])
    assert not suspicious, "Header row missing or misread – columns look like data values."


def test_hf_parquet_load():
    path = "hf://datasets/MegaScience/MegaScience/data/train-00000-of-00001.parquet"
    df = load_data(path)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty   

    print("\nData loaded successfully:")
    print(df.head())
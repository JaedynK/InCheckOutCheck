import pandas as pd
import json

def load_data(path: str, file_type: str = None, **kwargs) -> pd.DataFrame:
    """
    Loads data from CSV, Excel, or SQL with optional kwargs passed to pandas.
    """
    if file_type is None:
        if path.endswith(".csv"):
            file_type = "csv"
        elif path.endswith(".xlsx") or path.endswith(".xls"):
            file_type = "excel"
        elif path.endswith(".json"):
            file_type = "json"
        else:
            raise ValueError("Unknown file type. Please specify 'file_type' manually.")

    if file_type == "csv":
        df = pd.read_csv(path, **kwargs)
    elif file_type == "excel":
        df = pd.read_excel(path, **kwargs)
    elif file_type == "json":
        df = pd.read_json(path, **kwargs)
    elif file_type == "sql":
        # Requires kwargs: sql_query and connection
        df = pd.read_sql_query(kwargs["sql_query"], kwargs["connection"])
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    return df
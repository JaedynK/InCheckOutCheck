# InCheckOutCheck Project: Structure, Tests, and Output

## Project Structure

```
InCheckOutCheck/
├── api/
│   ├── main.py
│   ├── routes_datasets.py
│   └── routes_models.py
├── config/
│   ├── default.yaml
│   ├── dvc.yaml
│   └── start_pipeline.py
├── pipeline/
│   ├── __init__.py
│   ├── data_prep/
│   │   └── load_data.py
│   ├── evaluation/
│   │   └── bias_audit.py
│   ├── explainability/
│   │   ├── lime_explainer.py
│   │   └── shap_explainer.py
│   ├── inference/
│   │   └── predict.py
│   ├── modeling/
│   │   ├── train_model.py
│   │   ├── trained_model.py
│   │   └── qwen3-4b-thinking-2507/
│   └── retraining/
│       └── trigger.py
├── tests/
│   ├── __init__.py
│   ├── test_audit.py
│   ├── test_explainers.py
│   ├── test_load_data.py
│   ├── test_qwenmodel_aequitas.py
│   ├── test_trained_model.py
│   ├── test_data/
│   │   └── sample_data.csv
│   └── test_output/
│       ├── aequitas_qwen_report.csv
│       └── aequitas_test_report.csv
├── all_test_output.txt
├── dockerfile
├── README.md
├── requirements.api.txt
└── requirements.txt
```

## What You Can Test

- Model loading and text generation (QwenModel)
- API endpoints (FastAPI)
- Data loading utilities
- Explainability (LIME, SHAP)
- Fairness & bias auditing (Aequitas, Fairlearn)
- Test data and outputs

## How to Run All Tests

From the `InCheckOutCheck` directory:
```powershell
$env:PYTHONPATH='.'; pytest -s -v > all_test_output.txt 2>&1
```

## Example Test Output

```
============================= test session starts =============================
platform win32 -- Python 3.10.4, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\Jaedyn\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Jaedyn\MLops_framework\InCheckOutCheck
plugins: anyio-4.9.0, hydra-core-1.3.2
collecting ... collected 9 items


================== 9 passed, 17 warnings in 94.26s (0:01:34) ==================
```

See `all_test_output.txt` for full details of each test, including print statements, model outputs, audit results, and warnings.

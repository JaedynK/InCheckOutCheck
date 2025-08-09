<<<<<<< HEAD
=======
<<<<<<< HEAD
# InCheckOutCheck
A lightweight, local-first MLOps framework focused on ethical and reproducible machine learning. Built for small teams that need explainable, bias-audited pipelines.

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

## Model Caching
The Qwen model is cached locally in `pipeline/modeling/qwen3-4b-thinking-2507/` and is ignored by git. To pre-download the model, run:
```bash
python pipeline/modeling/trained_model.py
```

## How to Run All Tests
From the `InCheckOutCheck` directory:
```powershell
$env:PYTHONPATH='.'; pytest -s -v > all_test_output.txt 2>&1
```
This will run all tests and save detailed output to `all_test_output.txt`.

## Example Test Output
See `all_test_output.txt` for full details of each test, including print statements, model outputs, audit results, and warnings.
=======
>>>>>>> 5977ff6 (added docker (not working yet) and Fast api and more tests)
# Ethics-First MLOps Framework
## Overview
A lightweight, local-first MLOps framework focused on ethical and reproducible machine learning. Built for small teams that lack enterprise resources but need explainable, bias-audited pipelines.

Category	    Library	    Purpose	                                        Use Case
Bias Auditing	fairlearn	Group   fairness metrics & visual diagnostics	Evaluation
Bias Auditing	aequitas	Audit report across protected attributes	    Evaluation
Explainability	shap	    Feature attribution and global explanation	    Explainability, Reporting
Explainability	lime	    Local explanation of individual predictions	    Explainability


ML + Utilities	scikit-learn, pandas, numpy	Model training, data prep	All stages


## Directory Structure.
📁 config/ # YAML/JSON config files
📁 pipeline/ # Core ML lifecycle components
📁 tests/ # Pytest-based testing suite
📄 README.md 


## Pipeline Components
Setup DONE
**Data Intake:** `load_data.py` handles ingestion and validation. - DONE
**Training:** `train_model.py` supports config-driven training runs.
**Evaluation:** Supports fairness audits using Aequitas or Fairlearn. - DONE
**Inference:** `predict.py` exposes FastAPI or CLI prediction service.
**Deployment:** `api.py` hosts REST endpoints via FastAPI.
**Retraining:** Simulates drift detection or audit-triggered retraining.

## TESTING
DATA LOAD - AUDIT - Explainers 

## Setup
```bash
pip install -r requirements.txt
<<<<<<< HEAD
python start_pipeline.py --config config/default.yaml
=======
python start_pipeline.py --config config/default.yaml
>>>>>>> 85f617b (Initial Framework with API, CLI, Tests)
>>>>>>> 5977ff6 (added docker (not working yet) and Fast api and more tests)

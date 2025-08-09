<<<<<<< HEAD
=======
<<<<<<< HEAD
# InCheckOutCheck
This will be the start of my ethics first mlOps Framework where I plan to grow over time.
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

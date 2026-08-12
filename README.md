# DLH — Modern AI

Data analysis and machine learning with scikit-learn — from data preparation through linear and tree-based models.

---

## Directory Structure

```
dlh-modern_ai/
├── data_analysis/               # Data wrangling
│   └── data_preparation_visualization/  # EDA, cleaning, visualization, statistics, features
│       ├── 0-describe_data.py through 17-split_data.py
│       ├── README.md
│       └── Telco-Customer-Churn.csv, Task_7.png, Task_8.png
├── machine_learning/            # Models
│   ├── linear_models/           # OLS → metrics → Ridge/Lasso → SHAP → logistic → SVM
│   │   ├── 0-linear_regression.py through 6-svm.py
│   │   └── README.md
│   ├── tree_models/             # Trees → pruning → random forest → boosting
│   │   ├── 0-build.py through 11-boosting.py
│   │   └── README.md
│   └── .gitignore
├── .venv/                       # Python virtual environment
├── requirements.txt
└── README.md
```

---

## Quick Reference

| Track | Module | Topics | Tasks |
|-------|--------|--------|-------|
| **Data Analysis** | [Data Preparation & Visualization](data_analysis/data_preparation_visualization/) | EDA, cleaning, encoding, scaling, train/test split, churn analysis (Telco) | 18 |
| **Machine Learning** | [Linear Models](machine_learning/linear_models/) | OLS, evaluation metrics, Ridge, Lasso, SHAP, logistic regression, SVM | 7 |
| **Machine Learning** | [Tree Models](machine_learning/tree_models/) | Decision trees, pre/post-pruning, random forest, feature importance, boosting (AdaBoost/GBM/XGBoost/LightGBM) | 12 |

---

## Learning Progression

### Learning Path
1. **Data Preparation & Visualization** (describe → clean → visualize → statistical tests → engineer → encode → scale → split) → 2. **Linear Models** (OLS → evaluation metrics → Ridge/Lasso → SHAP → logistic → SVM) → 3. **Tree Models** (single tree → pre/post-pruning → random forest → feature importance → boosting)

---

## Setup

```bash
cd dlh-modern_ai
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` installs numpy, pandas, scipy, matplotlib, and seaborn.

# Linear Models

Linear models with scikit-learn — ordinary least squares through regularized regression (Ridge, Lasso), logistic regression and SVM classifiers, with SHAP for explaining predictions.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | Create an OLS model with sklearn |
| 2 | Compute MSE, RMSE, MAE, and R² regression metrics |
| 3 | What Ridge adds over OLS (L2 regularization, coefficient shrinkage) |
| 4 | What Lasso adds over OLS (L1 regularization, automatic feature selection) |
| 5 | Explain model predictions with SHAP |
| 6 | Classify with logistic regression |
| 7 | Pick an SVM kernel |

---

## Task-by-Task Reference

---

### Task 0 — Linear Regression (`0-linear_regression.py`)

**Challenge:** Create a regression model — what is the minimal sklearn estimator?

**Approach:** `linear_model.LinearRegression()` instantiates an untrained ordinary least squares model; the function returns it.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `linear_model.LinearRegression()` | Untrained OLS estimator — coefficients are learned later by `.fit()` |

> **Key takeaway:** OLS minimizes the residual sum of squares. sklearn hands you an untrained estimator whose `.fit()` / `.predict()` API is shared by every model in this project.

---

### Task 1 — Regression Evaluation Metrics (`1-regression_evaluation_metrics.py`)

**Challenge:** One number cannot judge a regression — different metrics expose different error types.

**Approach:** Compute four metrics on the same `(y_true, y_pred)` pair — MSE, RMSE, MAE, R² — and return them as the tuple `(mse, rmse, mae, r2)`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `metrics.mean_squared_error(y_true, y_pred)` | Average squared error — penalizes large errors quadratically |
| `metrics.root_mean_squared_error(y_true, y_pred)` | Square root of MSE — error in the original units |
| `metrics.mean_absolute_error(y_true, y_pred)` | Average absolute error — robust to outliers |
| `metrics.r2_score(y_true, y_pred)` | Fraction of variance explained (1 = perfect prediction) |

> **Key takeaway:** MSE punishes big errors, RMSE restores the original unit, MAE ignores error magnitude, and R² is scale-free — the four together tell the full story.

---

### Task 2 — Ridge Regression (`2-ridge_regression.py`)

**Challenge:** OLS coefficients blow up when features are correlated — how do you stabilize them?

**Approach:** `linear_model.Ridge(random_state=random_state)` adds an L2 penalty that shrinks large coefficients; `random_state` seeds the estimator for reproducible results.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `linear_model.Ridge(random_state=random_state)` | L2-regularized OLS — shrinks coefficients without zeroing them |
| `random_state` | Integer seed making stochastic estimator behavior reproducible |

> **Key takeaway:** Ridge trades a little bias for much lower variance: the L2 penalty pulls all coefficients toward zero, so correlated features no longer produce extreme weights.

---

### Task 3 — Lasso Regression (`3-Lasso_regression.py`)

**Challenge:** Ridge shrinks coefficients but keeps every feature — how do you get a sparse model?

**Approach:** `linear_model.Lasso(random_state=random_state)` adds an L1 penalty that forces some coefficients to exactly zero, doing automatic feature selection.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `linear_model.Lasso(random_state=random_state)` | L1-regularized OLS — zeroes coefficients, selecting features |

> **Key takeaway:** L1 vs L2: Lasso drives coefficients to zero (feature selection), Ridge only shrinks them — a sparse model is simpler to interpret and cheaper to deploy.

---

### Task 4 — SHAP (`4-shap.py`)

**Challenge:** Coefficients give a feature's average effect — how do you explain one single prediction?

**Approach:** `shap.LinearExplainer(model, X_train)` builds an explainer with `X_train` as background data; calling `explainer(X_test)` produces per-sample SHAP values.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `shap.LinearExplainer(model, X_train)` | SHAP explainer for linear models, initialized on the training set |
| `explainer(X_test)` | Compute SHAP values decomposing each prediction into per-feature contributions |

> **Key takeaway:** SHAP turns a prediction into a fair per-feature allocation of blame — for linear models the decomposition is exact and requires no retraining.

---

### Task 5 — Logistic Regression (`5-logisitc_regression.py`)

**Challenge:** Regression outputs a continuous number — how do you output a class probability instead?

**Approach:** `linear_model.LogisticRegression(random_state=random_state)` fits the logistic (sigmoid) function to separate two classes — binary classification through the same estimator API.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `linear_model.LogisticRegression(random_state=random_state)` | Binary classifier — the logistic function maps the linear combination into a (0, 1) probability |

> **Key takeaway:** Logistic regression is a linear model with a sigmoid on top — same API as OLS, but optimized for classification.

---

### Task 6 — SVM (`6-svm.py`)

**Challenge:** Which decision boundary shape? And how do you fail loudly on bad input?

**Approach:** `svm.SVC(kernel=name, random_state=random_state)` creates a support vector classifier with the requested kernel — `'linear'`, `'poly'`, or `'rbf'`. Any other name triggers a bare `raise TypeError` with no message.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `svm.SVC(kernel=name, random_state=random_state)` | SVM classifier — the kernel choice determines the boundary shape |
| `raise TypeError` | Input validation — bare raise, no message, the project's only explicit error |

> **Key takeaway:** This is the only task with explicit validation — a bare `raise TypeError` (no message) guards the kernel whitelist; validate input before constructing the model.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `LinearRegression()` — untrained OLS estimator | Model Creation |
| 1 | MSE, RMSE, MAE, R² via sklearn.metrics | Evaluation |
| 2 | `Ridge(random_state=)` — L2 regularization, coefficient shrinkage | Regularization |
| 3 | `Lasso(random_state=)` — L1 regularization, feature selection | Regularization |
| 4 | `shap.LinearExplainer` + `explainer(X_test)` — per-prediction explanations | Explainability |
| 5 | `LogisticRegression(random_state=)` — logistic function for binary classification | Classification |
| 6 | `svm.SVC(kernel=)` + bare `raise TypeError` validation | Classification |

---

## Resources

**scikit-learn API reference:**
- [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
- [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
- [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- [mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)
- [root_mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html)
- [mean_absolute_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)
- [r2_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)

**Explainability:**
- [SHAP LinearExplainer](https://shap.readthedocs.io/en/latest/generated/shap.LinearExplainer.html)

---

## Group Project

[Audi A1 Price Prediction](https://github.com/kaankartalk/Audi_A1_Price) — built with the group. Scrapes ~471 used Audi A1 listings from AutoTrader (UK) into `Audi_A1_listings.csv` and predicts resale price with the exact models this project covers: linear regression, Ridge, Lasso, and SHAP explanations. Live demo: https://kaankartalk.github.io/Audi_A1_Price/. Will be merged at the end for those interested.

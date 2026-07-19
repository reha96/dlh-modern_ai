# Tree-Based Models

Build, train, tune, and compare tree-based classifiers — from a single decision tree through ensemble methods (random forest and boosting) — using scikit-learn, XGBoost, and LightGBM on the Wine dataset.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | What is a decision tree classifier? |
| 2 | How do decision trees make splits? |
| 3 | What is pre-pruning vs. post-pruning? |
| 4 | What is ccp_alpha in pruning? |
| 5 | How does a random forest improve over a single tree? |
| 6 | What is feature importance in random forests? |
| 7 | What is boosting? |
| 8 | How does AdaBoost differ from Gradient Boosting? |
| 9 | What are XGBoost and LightGBM? |
| 10 | How do you evaluate classifier performance? |
| 11 | What is the difference between bagging and boosting in ensemble learning? |

---

## Task-by-Task Reference

---

### Task 0 — Decision Tree Classifier (`0-build.py`)

**Challenge:** Create a configurable decision tree — what parameters does sklearn expose, and what do they control?

**Approach:** Instantiate `DecisionTreeClassifier` with `criterion='gini'` (split quality measure), `max_depth=None` (unrestricted growth), and the three user-supplied arguments (`min_samples_leaf`, `min_samples_split`, `random_state`).

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `tree.DecisionTreeClassifier(criterion='gini', max_depth=None, min_samples_leaf, min_samples_split, random_state)` | Create a tree: Gini impurity measures split quality; unrestricted depth lets it grow until leaves are pure or stopping criteria kick in |

> **Key takeaway:** A decision tree recursively partitions data using impurity-based splits. `min_samples_leaf` and `min_samples_split` set the floor for how small a split or leaf can be — they are the tree's first line of defense against overfitting.

---

### Task 1 — Train a Tree-Based Classifier (`1-train.py`)

**Challenge:** Learn — and remember — the single most important sklearn API call.

**Approach:** `clf.fit(X, y)` fits the classifier to the feature matrix `X` and target labels `y`. The function returns `None`; the classifier is mutated in place.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `clf.fit(X, y)` | Universal sklearn training method — builds the tree by finding optimal splits on training data |

> **Key takeaway:** Every sklearn classifier (tree, forest, boosted model) exposes `.fit()`. Once you learn it for one model, you know it for all.

---

### Task 2 — View the Decision Rules of a Trained Tree (`2-draw.py`)

**Challenge:** How do you inspect what a trained tree actually learned — which features it splits on and at what thresholds?

**Approach:** `tree.export_text(clf, feature_names, class_names)` converts the fitted tree into a human-readable text representation with indentation for depth and class predictions at each leaf.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `tree.export_text(clf, feature_names, class_names)` | Render the full decision tree as indented if-then rules showing feature, threshold, gini, samples, and predicted class at every node |

> **Key takeaway:** Decision trees are inherently interpretable — unlike neural networks, you can trace exactly why any prediction was made by following the path from root to leaf.

---

### Task 3 — Generate Predictions (`3-generate_predictions.py`)

**Challenge:** Use a trained model to make predictions on new data — the entire point of ML.

**Approach:** `clf.predict(X)` returns a NumPy array of class labels. Each sample in `X` falls through the tree's splits until it lands at a leaf node whose majority class becomes the prediction.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `clf.predict(X)` | Apply trained rules to new data and output predicted class labels |

> **Key takeaway:** `.fit()` trains, `.predict()` infers. These two methods are the universal contract for every sklearn supervised estimator.

---

### Task 4 — Evaluate Classifier Performance (`4-evaluate.py`)

**Challenge:** Accuracy says "80% correct" but hides which classes the model confuses. How do you get per-class metrics?

**Approach:** `metrics.classification_report(true_labels, predicted_labels, target_names)` generates precision (when it predicts class X, how often is it right?), recall (of actual class X, how many did it catch?), and F1-score (harmonic mean of the two) for each class.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `metrics.classification_report(true, pred, target_names=class_names)` | Per-class precision, recall, F1-score, and support in a formatted string |

> **Key takeaway:** Accuracy alone is insufficient — especially with imbalanced classes. A classification report reveals whether the model is biased toward the majority class or weak at detecting a specific minority class.

---

### Task 5 — Pre-Pruning (`5-pre_pruning.py`)

**Challenge:** A fully grown tree easily overfits. How do you systematically find the best constraints to apply *during* tree construction?

**Approach:** `model_selection.GridSearchCV` exhaustively tries every combination of `criterion` (gini/entropy), `max_depth`, `min_samples_leaf`, and `min_samples_split` (each in range [2,5)), evaluates each with 5-fold cross-validation using accuracy, and returns `.best_params_`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `model_selection.GridSearchCV(estimator, param_grid, cv=5, scoring='accuracy')` | Exhaustive hyperparameter search with cross-validation — trains and scores every combination automatically |
| `grid_search.fit(X, y)` | Run the grid search: splits data 5 ways, trains on 4 folds, tests on 1, rotates, averages |
| `.best_params_` | Dictionary of the best hyperparameter combination found |

> **Key takeaway:** Pre-pruning controls tree complexity *before* and *during* growth by capping depth and leaf size. GridSearchCV automates the trial-and-error of finding which caps work best.

---

### Task 6 — (Post-Pruning) Retrieve the Pruning Path (`6-pruning_path.py`)

**Challenge:** How do you get a range of pruning strengths to test for post-pruning?

**Approach:** `clf.cost_complexity_pruning_path(X, y)` computes the entire pruning sequence of a fitted tree. For each possible subtree size, it returns the corresponding `ccp_alpha` value (the penalty that prunes to that subtree) and the total leaf impurity at that alpha.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `clf.cost_complexity_pruning_path(X, y)` | Compute the full sequence of effective alpha values and their corresponding total leaf impurities |

> **Key takeaway:** `ccp_alpha` (cost-complexity pruning parameter) is the post-pruning analogue of pre-pruning's max_depth — larger alpha = more aggressive pruning = simpler tree. The pruning path gives you all possible alphas to test.

---

### Task 7 — (Post-Pruning) Train and Evaluate Decision Trees with Pruning (`7-prune_decision_tree.py`)

**Challenge:** For each candidate `ccp_alpha`, train a tree and measure its performance on both training and test data to compare generalization.

**Approach:** Loop over `ccp_alphas`. For each, construct a fresh `DecisionTreeClassifier(ccp_alpha=alpha)` with the same base parameters, train it via `train_tree()`, then record `clf.score(X_train, y_train)` and `clf.score(X_test, y_test)`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `clf.score(X, y)` | Mean accuracy on a dataset — shorthand for `.predict(X)` then comparing to `y` |
| Training trees at varying `ccp_alpha` | Compare how pruning strength affects train vs. test accuracy to detect overfitting |

> **Key takeaway:** Post-pruning grows the tree fully first, then prunes branches back using ccp_alpha. Plotting train vs. test accuracy across alphas reveals the bias-variance tradeoff: low alpha = low bias, high variance (overfit); high alpha = high bias, low variance (underfit).

---

### Task 8 — (Post-Pruning) Best ccp_alpha for Pruning (`8-best_ccp_alpha.py`)

**Challenge:** From the array of trained trees at different alphas, how do you programmatically select the best one using a principled multi-tier tiebreaker?

**Approach:** Three-tier selection:
1. **Highest test accuracy** — primary goal is predictive performance.
2. If tie: **Smallest train–test accuracy gap** — penalizes overfitting; prefers generalization.
3. If still tied: **Largest ccp_alpha** — promotes the simplest, most regularized tree.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Multi-tier model selection algorithm | A decision rule chain that picks the best model from candidates, balancing accuracy, generalization, and simplicity |

> **Key takeaway:** Selecting the best model is rarely just "pick the highest score." You need a tiebreaker cascade that encodes your priorities — in this case: accuracy first, generalization second, simplicity third.

---

### Task 9 — Random Forest Classifier (`9-random_forest.py`)

**Challenge:** A single tree has high variance — small changes in training data produce very different trees. How do you stabilize predictions?

**Approach:** `ensemble.RandomForestClassifier(n_estimators, random_state)` builds many trees, each on a different bootstrap sample of the data with a random subset of features considered at each split. The final prediction is the majority vote across all trees.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `ensemble.RandomForestClassifier(n_estimators, random_state)` | Bootstrap-aggregated (bagged) ensemble: many trees vote, canceling out individual errors |

> **Key takeaway:** Random forest reduces variance through bagging — **B**ootstrap **agg**regat**ing**. Trees are built independently in parallel on random data subsets. Each tree overfits, but their errors are uncorrelated, so averaging (voting) cancels them out. This is the defining difference from boosting (Task 11).

---

### Task 10 — Feature Importance with Random Forest (`10-feature_importance.py`)

**Challenge:** A random forest is a black-box ensemble of many trees. How do you know which input features actually matter for predictions?

**Approach:** `rf.feature_importances_` returns the Gini importance (mean decrease in impurity) for each feature, aggregated across all trees. `np.argsort()` ranks them from least to most important.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `rf.feature_importances_` | Per-feature Gini importance scores — how much each feature reduces impurity across the forest (sum = 1) |
| `np.argsort(importances)` | Return indices sorted in ascending order by importance |

> **Key takeaway:** Feature importance exposes which variables actually drive the model's decisions — valuable for both model interpretation and feature selection (drop low-importance columns to simplify without losing accuracy).

---

### Task 11 — Boosting (`11-boosting.py`)

**Challenge:** A single classifier has irreducible bias. How do you build an ensemble where each new model corrects the mistakes of the previous ones?

**Approach:** Map four boosting algorithm names to their scikit-learn/XGBoost/LightGBM constructors: `AdaBoostClassifier` (reweights misclassified samples), `GradientBoostingClassifier` (fits residuals), `XGBClassifier` (regularized gradient boosting), and `LGBMClassifier` (leaf-wise growth for speed). Raise `ValueError` for unknown names.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `ensemble.AdaBoostClassifier(n_estimators, random_state)` | Adaptive boosting: reweights misclassified samples so later trees focus on hard cases |
| `ensemble.GradientBoostingClassifier(n_estimators, random_state)` | Gradient boosting: each tree fits the residual errors of the previous ensemble |
| `xgb.XGBClassifier(n_estimators, random_state)` | Extreme Gradient Boosting: adds L1/L2 regularization to gradient boosting for better generalization |
| `lgb.LGBMClassifier(n_estimators, random_state, verbose=-1)` | LightGBM: gradient boosting with leaf-wise growth and histogram-based splitting for speed |

> **Key takeaway:** Boosting builds trees **sequentially** — each new tree corrects the previous ensemble's errors — reducing **bias** at the risk of overfitting. Bagging (Task 9) builds trees in **parallel** on random subsets — reducing **variance**. AdaBoost reweights samples; Gradient Boosting fits residuals; XGBoost and LightGBM add optimizations for speed and regularization.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `DecisionTreeClassifier` with Gini, max_depth, min_samples_leaf/split, random_state | Model Creation |
| 1 | `clf.fit(X, y)` — universal training method | Training |
| 2 | `tree.export_text(clf, feature_names, class_names)` — tree as human-readable rules | Inspection |
| 3 | `clf.predict(X)` — generate class labels for new data | Inference |
| 4 | `metrics.classification_report(true, pred, target_names)` — per-class precision, recall, F1 | Evaluation |
| 5 | `GridSearchCV` with 5-fold CV, `best_params_` — exhaustive hyperparameter search | Hyperparameter Tuning |
| 6 | `clf.cost_complexity_pruning_path(X, y)` → ccp_alphas, impurities | Post-Pruning |
| 7 | `clf.score(X, y)` + training trees across ccp_alphas | Post-Pruning |
| 8 | Multi-tier selection: max test accuracy → min train–test gap → largest alpha | Model Selection |
| 9 | `RandomForestClassifier(n_estimators, random_state)` — bagged ensemble | Ensemble |
| 10 | `rf.feature_importances_` + `np.argsort()` — Gini importance ranking | Inspection |
| 11 | AdaBoost, Gradient Boosting, XGBoost, LightGBM — sequential ensemble methods | Ensemble |

---

## Resources

**scikit-learn API reference:**
- [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [tree.export_text](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html)
- [cost_complexity_pruning_path](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.cost_complexity_pruning_path)
- [classification_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)
- [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
- [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
- [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)

**XGBoost & LightGBM:**
- [xgboost.XGBClassifier](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier)
- [lightgbm.LGBMClassifier](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html)

**Articles:**
- [Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html)
- [Feature Importance with Random Forests](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)

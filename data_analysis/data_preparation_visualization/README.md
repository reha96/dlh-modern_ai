# Data Preparation & Visualization

End-to-end preprocessing of the Telco Customer Churn dataset — from raw CSV inspection through cleaning, exploratory visualization, statistical testing, feature engineering, encoding, scaling, and train/test split.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | Load CSV data and inspect DataFrame structure (shape, dtypes, missing, duplicates) |
| 2 | Visualize missingness patterns with scatter plots |
| 3 | Convert column data types with `pd.to_numeric` and `.replace` |
| 4 | Handle missing values with `dropna`, `fillna` (median, formula imputation) |
| 5 | Remove duplicate rows |
| 6 | Drop non-predictive identifier columns |
| 7 | Plot target variable class distribution with bar plots |
| 8 | Plot categorical feature distributions in a subplot grid |
| 9 | Visualize continuous feature distributions with histogram + KDE + boxplot |
| 10 | Create annotated correlation heatmaps with seaborn |
| 11 | Plot churn rate per categorical feature using `groupby` + bar |
| 12 | Compare numeric distributions by churn with side-by-side grouped-bar histograms |
| 13 | Test categorical feature independence from target using chi-square |
| 14 | Test numeric feature mean differences between churn groups using Welch's t-test |
| 15 | Engineer new features: count-based composites and binned categoricals |
| 16 | Encode categorical features for ML: `LabelEncoder`, `OrdinalEncoder`, one-hot encoding |
| 17 | Standardize numeric features with `StandardScaler` |
| 18 | Split data into train/test sets with stratified sampling |

---

## Task-by-Task Reference

---

### Task 0 — Describe Data (`0-describe_data.py`)

**Challenge:** Get a quick structural overview of a new dataset without visual inspection.

**Approach:** Load CSV with `pd.read_csv()`, then chain `.shape`, `.dtypes`, `.head()`, `.isna().sum()`, and `.duplicated().sum()` to inspect structure, types, preview, missing counts, and duplicates.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `pd.read_csv(filename)` | Load tabular data from a CSV file |
| `df.shape` | Tuple of (rows, columns) |
| `df.dtypes` | Series of column data types |
| `df.head()` | Preview first 5 rows |
| `df.isna().sum()` | Count NaN values per column |
| `df.duplicated().sum()` | Count duplicate rows |

> **Key takeaway:** The first step of any data project is a high-level structural scan — shape, types, missingness, duplicates — before any cleaning or modeling.

---

### Task 1 — Plot Missingness (`1-plot_missingness.py`)

**Challenge:** Visually identify which columns and rows contain missing values, at a glance.

**Approach:** Use `np.where(df.isnull().values)` to get (row, col) coordinates of missing values, then `plt.scatter()` them on a grid with y-tick labels as column names.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `np.where(condition)` | Get (row, col) indices where condition is True |
| `df.isnull().values` | Boolean array marking NaN positions |
| `plt.scatter(x, y, marker="|")` | Scatter plot with vertical line markers |
| `plt.yticks(positions, labels)` | Custom y-axis tick labels |
| `plt.tight_layout()` | Adjust subplot spacing to avoid overlap |

> **Key takeaway:** A missingness scatter plot reveals the shape of incompleteness — vertical streaks indicate whole-column issues, horizontal streaks indicate problematic rows.

---

### Task 2 — Convert Columns (`2-convert_columns.py`)

**Challenge:** Fix improperly typed columns — a numeric column stored as string, and a 0/1 column that should be categorical 'Yes'/'No'.

**Approach:** `pd.to_numeric(…, errors='coerce')` converts strings to floats (invalid → NaN). `.replace({0: 'No', 1: 'Yes'})` remaps numeric codes to readable labels.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `pd.to_numeric(series, errors='coerce')` | Convert to numeric, coercing failures to NaN |
| `df['col'].replace({old: new, …})` | Map specific values to replacements; unmatched values stay unchanged |

> **Key takeaway:** Data read from CSV often arrives with wrong dtypes; `to_numeric` and `replace` are the primary tools for type correction.

---

### Task 3 — Clean Total Charges (`3-clean_total_charges.py`)

**Challenge:** Handle missing values in a critical column with three different strategies, selectable by parameter.

**Approach:** `dropna(subset=[…])` removes rows where TotalCharges is NaN. `fillna(median())` replaces NaN with the column median. Formula imputation fills NaN as `MonthlyCharges * tenure`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `df.dropna(subset=['col'])` | Remove rows where a specific column is NaN |
| `Series.fillna(value)` | Replace NaN with a scalar or computed value |
| `Series.median()` | Compute median, ignoring NaN |
| `df.copy()` | Explicit shallow copy to avoid mutating the original |

> **Key takeaway:** Missing value handling is not one-size-fits-all; different imputation strategies (drop, median, formula) have different trade-offs and should be parameterized.

---

### Task 4 — Remove Duplicates (`4-remove_duplicates.py`)

**Challenge:** Eliminate redundant identical rows from a DataFrame.

**Approach:** `df.drop_duplicates()` removes all rows that are exact duplicates of preceding rows.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `df.drop_duplicates()` | Remove duplicate rows (keeps first occurrence) |

> **Key takeaway:** Duplicate rows inflate counts and bias statistical tests. One line of pandas fixes it.

---

### Task 5 — Drop customerID (`5-drop_customerID.py`)

**Challenge:** Remove a column that uniquely identifies each row but has no predictive value.

**Approach:** `df.drop("customerID", axis=1)` removes the column by name.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `df.drop("col", axis=1)` | Drop a column by name (`axis=1` targets columns, not rows) |

> **Key takeaway:** Unique identifiers (customerID, row index) must be dropped before modeling — they carry zero signal and can cause data leakage.

---

### Task 6 — Plot Churn Distribution (`6-plot_churn_distribution.py`)

**Challenge:** Check whether the target variable is imbalanced (far more No than Yes).

**Approach:** `value_counts().reindex(['No', 'Yes'])` ensures consistent bar order, then `plt.bar()` with per-bar colors.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `Series.value_counts()` | Count occurrences of each unique value |
| `Series.reindex([order])` | Reorder index to enforce a display order |
| `plt.bar(x, y, color=[…])` | Bar plot with per-bar color assignment |

> **Key takeaway:** Always check target class balance first — severe imbalance determines whether you need stratified sampling, class weights, or resampling.

---

### Task 7 — Plot Categorical Distributions (`7-plot_categorical_distributions.py`)

**Challenge:** Visualize the frequency of every categorical feature in a single figure.

**Approach:** Use `plt.subplots(n_rows, n_cols)` for a grid layout, enumerate over axes and columns, plot each with `ax.bar()`, rotate labels 45°, and hide unused subplots with `.axis('off')`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `plt.subplots(n_rows, n_cols, figsize=…)` | Create a grid of subplots |
| `axes.flatten()` | Convert 2D axes array to 1D for easy iteration |
| `ax.tick_params(axis='x', labelrotation=45)` | Rotate x-tick labels |
| `ax.axis('off')` | Hide unused subplot frames |

> **Key takeaway:** A subplot grid is the standard pattern for batch-visualizing multiple features; `flatten()` + zip makes the loop trivial.

---

### Task 8 — Plot Continuous Distributions (`8-plot_continuous_distributions.py`)

**Challenge:** Show both the shape (histogram + KDE) and outliers (boxplot) of each numeric column in one figure.

**Approach:** `plt.subplots(n, 2)` — left column = `ax.hist(density=True)` + `stats.gaussian_kde()` overlay as a dashed red line; right column = `ax.boxplot()`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `stats.gaussian_kde(data)` | Fit a kernel density estimator to data |
| `kde(x_vals)` | Evaluate KDE over a dense range for a smooth curve |
| `np.linspace(min, max, N)` | Generate evenly spaced values for KDE evaluation |
| `ax.plot(x, y, color='red', ls='--')` | Overlay a dashed KDE line on the histogram |
| `ax.boxplot(data, orientation='horizontal')` | Horizontal box-and-whisker plot |

> **Key takeaway:** Histogram + KDE shows distribution shape; boxplot exposes outliers, skew, and quartiles. Together they give a complete picture of a continuous variable.

---

### Task 9 — Plot Correlation Heatmap (`9-plot_correlation_heatmap.py`)

**Challenge:** Identify which numeric features move together, using a single visual.

**Approach:** `df.select_dtypes(include='number').corr()` computes the pairwise Pearson correlation matrix. `sns.heatmap()` with `annot=True`, `cmap='coolwarm'`, and `vmin=-1, vmax=1` creates an annotated diverging heatmap.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `df.corr()` | Compute pairwise Pearson correlation matrix |
| `sns.heatmap(matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)` | Annotated heatmap with full-range diverging colormap |

> **Key takeaway:** Correlation heatmaps quickly reveal multicollinearity — features that carry redundant information — critical for linear models.

---

### Task 10 — Plot Categorical vs Churn (`10-plot_categorical_vs_churn.py`)

**Challenge:** Quantify how churn rate varies across categories of a categorical feature.

**Approach:** `df.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean())` computes churn rate per category as the proportion of 'Yes', then `plt.bar()` plots the result.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `df.groupby(col)['target'].apply(func)` | Split-apply-combine: group by category, compute per-group statistic |
| `lambda x: (x == 'Yes').mean()` | Compute proportion of 'Yes' — mean of boolean is fraction of True |

> **Key takeaway:** Groupby + apply is the pandas idiom for per-group statistics; `(x == 'Yes').mean()` directly gives the proportion without explicit counting.

---

### Task 11 — Plot Numeric vs Churn (`11-plot_numeric_vs_churn.py`)

**Challenge:** Compare the distribution of a continuous feature between churners and non-churners in a single plot — without overlapping.

**Approach:** Bin the numeric column with `pd.cut(bins=30)`, create a cross-tabulation with `groupby().value_counts().unstack()`, then `ct.plot.bar()` for side-by-side grouped bars per bin.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `pd.cut(series, bins=N)` | Bin continuous data into N equal-width intervals |
| `groupby(bins)[col].value_counts().unstack(fill_value=0)` | Cross-tabulate binned numeric variable against categorical |
| `DataFrame.plot.bar(width=0.8)` | Grouped bar plot — one group per bin, bars side by side |

> **Key takeaway:** `pd.cut + unstack + plot.bar` turns a continuous-vs-categorical comparison into an intuitive side-by-side grouped bar chart — no manual bin shifting needed.

---

### Task 12 — Chi-Square Tests (`12-chi_square_tests.py`)

**Challenge:** Quantify, with p-values, whether each categorical feature is statistically associated with Churn.

**Approach:** For each categorical column, build a contingency table with `pd.crosstab(col, Churn)`, then feed it to `stats.chi2_contingency()` and extract the p-value.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `pd.crosstab(row_var, col_var)` | Build a contingency (frequency) table |
| `stats.chi2_contingency(table)` | Chi-square test of independence; returns `(chi2, p, dof, expected)` |

> **Key takeaway:** `crosstab` + `chi2_contingency` is the direct Python equivalent of Stata's `tabulate x y, chi2` — test independence between two categorical variables.

---

### Task 13 — Welch's t-test (`13-ttest_numeric.py`)

**Challenge:** Test whether the mean of each numeric feature differs significantly between churners and non-churners.

**Approach:** For each numeric column, split into Yes/No groups, then `stats.ttest_ind(yes, no, equal_var=False)` computes Welch's t-test p-value.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `stats.ttest_ind(a, b, equal_var=False)` | Welch's t-test (does not assume equal variances) |
| `df.select_dtypes(include='number')` | Select only numeric columns |

> **Key takeaway:** Welch's t-test is preferred over Student's t-test when group variances are likely unequal; `equal_var=False` switches to Welch-Satterthwaite degrees of freedom.

---

### Task 14 — Create Features (`14-create_features.py`)

**Challenge:** Engineer two new features — a count-based composite (NumServices) and a binned categorical (TenureGroup) — then drop the source columns used to create them.

**Approach:** `(df[svc_cols] == 'Yes').sum(axis=1)` counts subscribed services row-wise, plus 1 if InternetService is DSL or Fiber optic. `pd.cut(tenure, bins, labels, right=True, include_lowest=False)` creates tenure interval groups.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `(df[cols] == val).sum(axis=1)` | Row-wise count of boolean matches across multiple columns |
| `Series.isin([val1, val2])` | Check membership in a list; returns boolean Series |
| `pd.cut(series, bins, labels, right=True, include_lowest=False)` | Full-parameter binning: custom labels, upper-bound-inclusive, exclude lowest edge |

> **Key takeaway:** Feature engineering transforms raw columns into more predictive representations — counting services reduces dimensionality; binning tenure captures non-linear relationships.

---

### Task 15 — Encode Features (`15-encode_features.py`)

**Challenge:** Convert all categorical columns to numeric representations suitable for ML models.

**Approach:** `LabelEncoder` for target Churn (single column, 1D). `OrdinalEncoder(categories=[['No', 'Yes']])` for binary Yes/No columns, each encoded individually to control the repr. `pd.get_dummies(drop_first=True, dtype=int)` for multi-category columns (Contract, PaymentMethod) with k−1 columns. Separate `OrdinalEncoder` for TenureGroup (alphabetical order).

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `preprocessing.LabelEncoder().fit_transform(series)` | Encode single 1D categorical column to 0/1/2/… |
| `preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])` | Encode with explicit category ordering; shapes repr |
| `pd.get_dummies(df[[cols]], drop_first=True, dtype=int)` | One-hot encode with k−1 columns to avoid multicollinearity |
| `df.drop(columns=[…])` + `pd.concat([df, dummies], axis=1)` | Replace original columns with encoded versions |

> **Key takeaway:** Three encoding strategies map to three column types: LabelEncoder for target (1D), OrdinalEncoder for ordered/binary features, One-hot (get_dummies) for nominal multi-category features.

---

### Task 16 — Scale Numeric (`16-scale_numeric.py`)

**Challenge:** Standardize numeric features to mean=0, std=1 so they're on a common scale for distance-based models.

**Approach:** `StandardScaler().fit_transform(df[['MonthlyCharges', 'TotalCharges']])` computes z-scores and replaces the columns in-place.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `preprocessing.StandardScaler()` | Standardize features: remove mean, scale to unit variance |
| `scaler.fit_transform(X)` | Fit to data and transform in one call |

> **Key takeaway:** Standardization (z-score normalization) is essential for models sensitive to feature magnitude — linear/logistic regression, SVM, KNN, neural networks. Without it, large-magnitude features dominate.

---

### Task 17 — Split Data (`17-split_data.py`)

**Challenge:** Split data into train/test sets while preserving the class distribution of the target variable.

**Approach:** `df.drop(columns=['Churn'])` separates X (features) from y (target). `model_selection.train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)` splits with stratification.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `df.drop(columns=[target])` | Separate feature matrix from target vector |
| `model_selection.train_test_split(X, y, test_size, random_state, stratify=y)` | Stratified train/test split preserving class proportions |

> **Key takeaway:** `stratify=y` ensures the train and test sets have the same target distribution — critical for imbalanced datasets where random splitting could skew evaluation metrics.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `pd.read_csv`, `shape`, `dtypes`, `head()`, `isna()`, `duplicated()` | EDA & Inspection |
| 1 | `np.where`, `plt.scatter(marker="|")`, `ytick` customization | EDA & Inspection |
| 2 | `pd.to_numeric(errors='coerce')`, `replace()` | Data Cleaning |
| 3 | `dropna(subset=)`, `fillna(median)`, formula imputation, `copy()` | Data Cleaning |
| 4 | `drop_duplicates()` | Data Cleaning |
| 5 | `drop(col, axis=1)` — removing IDs | Data Cleaning |
| 6 | `value_counts().reindex()`, `plt.bar(colors)` | Visualization |
| 7 | `subplots(n,m)`, `flatten()`, `tick_params(rotation=45)`, `axis('off')` | Visualization |
| 8 | `gaussian_kde`, KDE overlay, `np.linspace`, `boxplot` | Visualization |
| 9 | `df.corr()`, `sns.heatmap(annot=True, cmap='coolwarm')` | Visualization |
| 10 | `groupby().apply(lambda)`, churn rate as boolean mean | Visualization |
| 11 | `pd.cut` + `unstack` → side-by-side grouped bar histogram | Visualization |
| 12 | `pd.crosstab`, `chi2_contingency` — independence testing | Statistical Testing |
| 13 | `ttest_ind(equal_var=False)`, `select_dtypes(include='number')` | Statistical Testing |
| 14 | `(df == val).sum(axis=1)`, `isin()`, `pd.cut` full params | Feature Engineering |
| 15 | `LabelEncoder`, `OrdinalEncoder`, `get_dummies(drop_first=True, dtype=int)` | Encoding & Scaling |
| 16 | `StandardScaler().fit_transform()` | Encoding & Scaling |
| 17 | `train_test_split(stratify=y)` | Model Preparation |

---

## Resources

- [pandas Documentation](https://pandas.pydata.org/docs/)
- [matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [seaborn Documentation](https://seaborn.pydata.org/)
- [SciPy stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [scikit-learn preprocessing Documentation](https://scikit-learn.org/stable/modules/preprocessing.html)
- [scikit-learn model selection Documentation](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection)
- [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

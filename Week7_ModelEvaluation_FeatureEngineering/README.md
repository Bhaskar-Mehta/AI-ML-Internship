# Week 7 – Model Evaluation & Feature Engineering

Part of my [AI-ML-Internship](https://github.com/Bhaskar-Mehta/AI-ML-Internship) under mentor **Anurag Sharma**.

## Overview

This week focused on evaluating models properly instead of trusting a single train/test split, plus feature engineering and hyperparameter tuning. The Week 6 diabetes classification project was re-run with cross-validation, cleaned data, and tuned hyperparameters.

## Dataset

**Pima Indians Diabetes Dataset** — same dataset as Week 6, loaded directly from a public URL (no CSV file stored in this repo):

```python
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
```

## What I Did

- **Day 1:** Applied 5-fold cross-validation to the Week 6 Decision Tree and compared it against the original single train/test split score
- **Day 2:** Feature engineering — replaced invalid zero values (Glucose, BMI, etc.) with medians, checked for outliers
- **Day 3:** Hyperparameter tuning on Decision Tree using GridSearchCV
- **Day 4:** Hyperparameter tuning on Random Forest and SVM using RandomizedSearchCV / GridSearchCV
- **Day 5:** Built a before-vs-after comparison of all tuned models against their Week 6 baselines
- **Day 6:** Finalized results and wrote up the summary

## Cross-Validation vs Single Split

| Model | Single Split F1 (Week 6) | 5-fold CV Mean F1 |
|---|---|---|
| Decision Tree | TBD | TBD |

*(Table to be filled in with actual results after running the notebook.)*

## Before vs After Tuning

| Model | Week 6 F1 (before) | Week 7 F1 (after tuning) | Improvement |
|---|---|---|---|
| Decision Tree | TBD | TBD | TBD |
| Random Forest | TBD | TBD | TBD |
| SVM | TBD | TBD | TBD |

*(Table to be filled in with actual results after running the notebook.)*

## Best Tuned Model

**TBD** — will be updated with the best-performing tuned model, its parameters, and F1-score.

## Tools Used

- Python, Jupyter Notebook
- pandas, NumPy
- scikit-learn (GridSearchCV, RandomizedSearchCV, KFold, cross_val_score)
- matplotlib, seaborn

## Files

- `diabetes_tuned.ipynb` — full notebook with cross-validation, feature engineering, hyperparameter tuning, and before/after comparison

## Next Up

Week 8: Unsupervised Learning & NLP basics.
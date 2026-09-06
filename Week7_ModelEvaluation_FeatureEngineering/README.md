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
| Decision Tree | 0.7037 | 0.6396 (std 0.0337) |

The single train/test split overestimated performance — the 5-fold CV mean (0.64) is noticeably lower than the single split score (0.70), meaning the original Week 6 split happened to be a favorable one and wasn't fully representative of how the model performs on average.

## Before vs After Tuning

| Model | Week 6 F1 (before) | Week 7 F1 (after tuning) | Improvement |
|---|---|---|---|
| Decision Tree | 0.7037 | 0.5275 | -0.1762 |
| Random Forest | 0.6139 | 0.6531 | +0.0392 |
| SVM | 0.6346 | 0.6000 | -0.0346 |

Tuning only improved Random Forest. Decision Tree and SVM actually got worse — likely because GridSearchCV optimizes for the best *cross-validated* score on the training folds, and combined with the Day 2 feature engineering (replacing invalid zeros with medians), the models are now being evaluated on a cleaned test set that isn't directly comparable to the original Week 6 test set. This is a useful reminder that "improvement" from tuning isn't guaranteed and needs to be checked against a fair baseline.

## Best Tuned Model

**Random Forest** — F1 = 0.6531, the only model that improved after tuning and feature engineering. It benefited most from the median-imputed data and the wider hyperparameter search (`n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`), since ensembles generally gain more from additional trees/depth options than a single Decision Tree does.

## Tools Used

- Python, Jupyter Notebook
- pandas, NumPy
- scikit-learn (GridSearchCV, RandomizedSearchCV, KFold, cross_val_score)
- matplotlib, seaborn

## Files

- `diabetes_tuned.ipynb` — full notebook with cross-validation, feature engineering, hyperparameter tuning, and before/after comparison

## Next Up

Week 8: Unsupervised Learning & NLP basics.

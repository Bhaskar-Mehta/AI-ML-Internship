# Week 6 – Classification Algorithms

Part of my [AI-ML-Internship](https://github.com/Bhaskar-Mehta/AI-ML-Internship) under mentor **Anurag Sharma**.

## Overview

This week focused on supervised classification algorithms — Decision Trees, Random Forests, KNN, and SVM — benchmarked against each other on a real diabetes dataset.

## Dataset

**Pima Indians Diabetes Dataset** — binary classification (diabetic / not diabetic), loaded directly from a public URL (no CSV file stored in this repo):

```python
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
```

Features: Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age.

## What I Did

- **Day 1:** Built the ML workflow (split → train → predict → evaluate) with a Decision Tree classifier
- **Day 2:** Implemented Random Forest and compared feature importance to the single tree
- **Day 3:** Implemented KNN with feature scaling and tuned the value of k
- **Day 4:** Implemented SVM and compared linear, RBF, and polynomial kernels
- **Day 5:** Benchmarked all four models side by side using accuracy, precision, recall, and F1-score
- **Day 6:** Compared confusion matrices across models and wrote a final recommendation

## Models Compared

| Model | Accuracy | Precision | Recall | F1-score |
|---|---|---|---|---|
| Decision Tree | 0.7922 | 0.7037 | 0.7037 | 0.7037 |
| SVM | 0.7532 | 0.6600 | 0.6111 | 0.6346 |
| Random Forest | 0.7468 | 0.6596 | 0.5741 | 0.6139 |
| KNN | 0.7468 | 0.6596 | 0.5741 | 0.6139 |

## Best Model

**Decision Tree** — it came out on top across every metric, including the highest F1-score (0.70). This was a bit of a surprise since ensembles like Random Forest usually outperform a single tree, but with `max_depth=5` the tree stayed shallow enough to avoid overfitting while still capturing the key splits (Glucose, BMI, Age were the top features). SVM was the closest runner-up, while Random Forest and KNN tied and lagged behind on recall — meaning they missed more actual diabetic cases than the Decision Tree did.

## Tools Used

- Python, Jupyter Notebook
- pandas, NumPy
- scikit-learn (DecisionTreeClassifier, RandomForestClassifier, KNeighborsClassifier, SVC)
- matplotlib, seaborn

## Files

- `diabetes_classification.ipynb` — full notebook with all four models, evaluation metrics, and comparison charts

## Next Up

Week 7: cross-validation and hyperparameter tuning to validate and improve on these results.
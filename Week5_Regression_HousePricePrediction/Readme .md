# Week 5 — Supervised Learning: Regression
 
**AI/ML Internship Program — Month 2: Core ML**

## What this covers
- Linear Regression from first principles: cost function + gradient descent, demoed from scratch on tiny fake data.
- **Main project:** House Price Prediction using scikit-learn — full workflow: split → train → predict → evaluate.
- Logistic Regression on a binary classification problem (Breast Cancer dataset).

## Files
- `Week5_Regression_HousePricePrediction.ipynb` — the main notebook (run top to bottom).
- `data/USA_Housing.csv` — dataset used for the house price regression.
  (The Breast Cancer dataset used for Logistic Regression is built into scikit-learn — no download needed.)

## How to run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook Week5_Regression_HousePricePrediction.ipynb
```

## Results
- **Linear Regression (House Price):** R² ≈ 0.918, MAE ≈ $80,879, RMSE ≈ $100,444
- **Logistic Regression (Breast Cancer):** strong accuracy on held-out test data; full confusion matrix and classification report in the notebook.

## Key takeaways
1. Linear Regression explains ~92% of house price variance using just 5 numeric features.
2. MAE/RMSE give interpretable dollar-error figures; R² gives an overall fit score — useful together.
3. Logistic Regression needs feature scaling to train well; Linear Regression here did not.
4. Confusion matrix reveals which mistakes a classifier makes, which matters more than raw accuracy in sensitive domains like medical diagnosis.
 
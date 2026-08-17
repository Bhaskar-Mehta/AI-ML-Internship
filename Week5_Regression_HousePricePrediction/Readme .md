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
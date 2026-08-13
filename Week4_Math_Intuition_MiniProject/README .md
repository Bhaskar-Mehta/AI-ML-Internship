# Week 4 — Math Intuition for ML + Mini Project

**AI/ML Internship Program — Month 1: Foundations**

## What this covers
- Intuitive (not just formula-based) understanding of vectors, matrices, dot products, probability, and gradients/derivatives.
- A small hands-on gradient descent demo showing how models "learn" by minimizing a function step by step.
- **Mini Project:** an independent, full EDA (cleaning → exploration → visualization → written insights) on the Palmer Penguins dataset — a dataset not used in Weeks 2 or 3.

## Files
- `Week4_Math_Intuition_MiniProject.ipynb` — the main notebook (run top to bottom).
- `data/penguins.csv` — the dataset used for the mini project.
- `*.png` — chart images saved automatically when the notebook runs (also embedded in the notebook itself).

## How to run
```bash
pip install pandas numpy matplotlib seaborn jupyter
jupyter notebook Week4_Math_Intuition_MiniProject.ipynb
```

## Key findings from the mini project
1. Gentoo penguins are the largest species by body mass and flipper length.
2. Flipper length and body mass are strongly positively correlated.
3. Bill depth vs. bill length separates the three species more clearly than either measurement alone.
4. Species and island are closely linked (e.g., Gentoo only appears on Biscoe Island in this data).
5. Within each species, males tend to be slightly larger than females.
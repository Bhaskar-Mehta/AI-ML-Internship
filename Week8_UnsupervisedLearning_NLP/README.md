# Week 8 – Unsupervised Learning & NLP Basics

Part of my [AI-ML-Internship](https://github.com/Bhaskar-Mehta/AI-ML-Internship) under mentor **Anurag Sharma**.

## Overview

This week covered two areas of machine learning not touched before: unsupervised learning (clustering + dimensionality reduction) and an introduction to NLP through a sentiment analysis pipeline. Two separate notebooks, since these are two distinct topics.

## Notebook 1: `clustering_pca.ipynb`

**Dataset:** Wine dataset (13 chemical features, 3 wine cultivars), loaded via `sklearn.datasets.load_wine()` — no external file needed.

- **Day 1:** K-Means clustering — used the elbow method to confirm k=3, fit K-Means, checked cluster quality with silhouette score and adjusted rand index against the true wine classes
- **Day 2:** PCA — reduced the 13 features to 2 principal components and visualized the K-Means clusters in PCA space alongside the true wine classes

### Clustering Results

| Metric | Score |
|---|---|
| Silhouette score | 0.2848 |
| Adjusted Rand Index (vs true labels) | 0.8974 |
| PCA total variance captured (2 components) | 55.4% (PC1: 36.2%, PC2: 19.2%) |

The silhouette score is on the lower side, meaning the clusters aren't extremely tight or well-separated in the full 13-dimensional space. But the adjusted rand index of 0.90 shows the K-Means clusters almost perfectly matched the true wine cultivars — a strong result, and visually confirmed by the PCA scatter plot where the three clusters were clearly grouped.

## Notebook 2: `sentiment_analysis.ipynb`

**Dataset:** NLTK's `movie_reviews` corpus — 2000 labeled movie reviews (positive/negative).

- **Day 3:** Text preprocessing — tokenization, stopword removal, and TF-IDF vectorization
- **Day 4:** Built and evaluated two classifiers — Logistic Regression and Naive Bayes
- **Day 5:** Tested the pipeline on custom sentences and finalized the write-up

### Sentiment Classifier Results

| Model | Accuracy |
|---|---|
| Logistic Regression | 0.8125 |
| Naive Bayes | 0.7825 |

## Best Model

**Logistic Regression** — accuracy of 81.25% vs 78.25% for Naive Bayes, with slightly more balanced precision and recall across both classes. That said, testing the pipeline on short custom sentences (Day 5) revealed a limitation: it misclassified a clearly positive review as negative. This is likely because the model was trained on full-length professional movie reviews, and TF-IDF weighting on short, simple sentences doesn't carry the same signal — a good reminder that test-set accuracy doesn't always guarantee real-world reliability on inputs that look different from the training data.

## Tools Used

- Python, Jupyter Notebook
- pandas, NumPy
- scikit-learn (KMeans, PCA, TfidfVectorizer, LogisticRegression)
- nltk (movie_reviews corpus, tokenization, stopwords)
- NaiveBayes (MultinomialNB)
- matplotlib, seaborn

## Files

- `clustering_pca.ipynb` — K-Means clustering and PCA visualization on the wine dataset
- `sentiment_analysis.ipynb` — text preprocessing and sentiment classification pipeline

## Next Up

Week 9: Neural Networks basics.

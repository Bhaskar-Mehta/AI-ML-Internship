# Reflection: 12 Weeks of AI/ML

**Bhaskar Mehta — AI-ML-Internship, mentored by Anurag Sharma**

Over 12 weeks I went from Python basics to training models, a neural network, and a deployed app. These are the three things that changed how I work, and what I still want to improve.

## The 3 biggest things I learned

### 1. One number can fool you
In Week 6 my Decision Tree scored an F1 of 0.70 on a single train/test split. In Week 7 I checked it with 5-fold cross-validation and the average dropped to 0.64. The first split had simply been lucky. In Week 8 my sentiment model reached 81% test accuracy, yet it called an obviously positive review "negative" when I tried my own sentences. On the capstone, only about a quarter of customers churn, so a model can get good accuracy while missing many churners. Now I check more than one split, look at recall and F1 and not just accuracy, and test the model on inputs I wrote myself.

### 2. The model has to fit the data
In Week 9 my neural network scored an F1 of 0.55 on the diabetes data, worse than the simple Decision Tree from Week 6, because there were only about 770 rows. In Week 10 a small CNN reached 98.94% on MNIST, which has 60,000 images and is a much better match for a neural network. Tuning in Week 7 also made some models worse, not better. A bigger or more complex model is not automatically a better one, and every change needs to be checked against a fair baseline.

### 3. A model is only useful when someone can use it, and debugging is part of the job
In Week 11 I saved a trained model, moved the model code into its own file, and built a Streamlit app around it. That showed me that a trained model is just a file of weights, and that the app has to prepare inputs exactly the way training did. Before that, PyTorch kept crashing my notebook kernel. I tried reinstalling and repairing things, and the fix was a separate conda environment with Python 3.11. Reading error messages carefully and fixing the environment turned out to be as important as writing the model code.

## Areas I want to keep improving

### 1. Understanding the maths behind the models
I can build and train models, and I can explain ideas like backpropagation and gradient descent in simple words. I want to understand the maths underneath more deeply, so I can explain why a model behaves the way it does and not only what it did.

### 2. Stronger models and bigger projects
So far I used mostly basic models on small datasets. I want to try gradient boosting (XGBoost or LightGBM), work with larger and messier real datasets, and practise on Kaggle competitions. I also want to write cleaner, more reusable code with scripts and fixed environments from the start.

## What I'm proud of
Training the MNIST digit classifier in Week 10 and then turning it into a working web app in Week 11. It was the first time something I trained was usable by another person, not just a number in a notebook.
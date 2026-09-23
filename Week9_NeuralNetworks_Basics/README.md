# Week 9 – Neural Networks: The Basics

Part of my [AI-ML-Internship](https://github.com/Bhaskar-Mehta/AI-ML-Internship) under mentor **Anurag Sharma**.

## Overview

This week was about getting a simple, conceptual understanding of neural networks — no heavy math — and getting comfortable running basic code in PyTorch. The deliverable is one small neural network trained on a dataset already used before (the diabetes dataset from Week 6/7), so the focus stays on understanding the network itself rather than new data.

## Dataset

**Pima Indians Diabetes Dataset** — same dataset as Week 6/7, loaded directly from a public URL (no CSV file stored in this repo):

```python
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
```

## What I Did

- **Day 1:** Learned the core concepts — neurons, layers, weights, forward pass, loss, backpropagation, and gradient descent (no code, just understanding)
- **Day 2:** Set up PyTorch, ran basic tensor operations, and used a small autograd example to see how gradients are calculated automatically
- **Day 3:** Built a simple feedforward neural network (2 hidden layers) using the diabetes dataset
- **Day 4:** Trained the network using binary cross-entropy loss and the Adam optimizer, plotted the training loss over 100 epochs
- **Day 5:** Evaluated the trained network on the test set and compared it against earlier Week 6/7 models
- **Day 6:** Wrote a summary explaining how the network works in my own words

## Network Architecture

A simple feedforward neural network:
- Input layer → 16 neurons (ReLU)
- Hidden layer → 8 neurons (ReLU)
- Output layer → 1 neuron (Sigmoid, for binary classification)

Trained with Binary Cross-Entropy loss and the Adam optimizer over 100 epochs.

## Results

| Model | F1-score |
|---|---|
| Decision Tree (Week 6) | 0.7037 |
| Random Forest, tuned (Week 7) | 0.6531 |
| Neural Network (Week 9) | 0.5490 |

Accuracy for the neural network was 0.7013, but F1-score lagged behind both classical models — driven by weak recall (0.52) on the diabetic class. The network is much better at identifying non-diabetic cases (recall 0.80) than diabetic ones.

## How It Works (In My Own Words)

I built a simple feedforward neural network with 2 hidden layers (16 neurons, then 8 neurons) using ReLU activation, and a final output neuron with Sigmoid activation to produce a probability between 0 and 1.

During training, the network makes a prediction, compares it to the real answer using binary cross-entropy loss, then uses backpropagation to figure out how much each weight contributed to the error. The Adam optimizer then nudges every weight slightly to reduce that error, repeating this over 100 epochs.

The neural network underperformed both classical models from Week 6/7 on F1-score. This is a common result on small tabular datasets like this one (~770 rows): neural networks typically need more data to learn patterns that simpler models like decision trees can already capture efficiently from a small sample. It's a useful, realistic finding — bigger or more complex models don't automatically mean better results, especially on small data.

## Tools Used

- Python, Jupyter Notebook
- PyTorch (torch, torch.nn, torch.optim)
- pandas, NumPy, scikit-learn (StandardScaler, train_test_split, metrics)
- matplotlib

## Files

- `diabetes_nn.ipynb` — neural network concepts, PyTorch basics, and a trained model on the diabetes dataset

## Next Up

Week 10: A guided deep learning mini-project — a basic image or text classifier.

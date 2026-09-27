# Week 10 – Simple Deep Learning Mini Project

Part of my [AI-ML-Internship](https://github.com/Bhaskar-Mehta/AI-ML-Internship) under mentor **Anurag Sharma**.

## Overview

This week applied what I learned in Week 9 to one guided beginner deep learning project — a handwritten digit classifier using the MNIST dataset. The focus was on understanding what each part of the code does, not on optimizing or tuning the model.

## Dataset

**MNIST** — 70,000 grayscale images of handwritten digits (0–9), each 28x28 pixels. Loaded directly through `torchvision.datasets.MNIST`, which downloads it automatically — no manual file handling needed.

## What I Did

- **Day 1:** Loaded and explored the MNIST dataset, visualized sample digits, and set up data loaders for batching
- **Day 2:** Built a simple Convolutional Neural Network (CNN) with 2 convolutional layers and 2 fully connected layers
- **Day 3:** Trained the CNN over 5 epochs using Cross-Entropy loss and the Adam optimizer — loss dropped steadily from 0.2226 to 0.0257
- **Day 4:** Evaluated the trained model on the test set and visualized predictions
- **Day 5:** Wrote a summary of what I learned

## Model Architecture

A simple CNN:
- Conv layer (1 → 16 channels) → ReLU → Max Pooling
- Conv layer (16 → 32 channels) → ReLU → Max Pooling
- Fully connected layer (→ 128 neurons) → ReLU
- Output layer (→ 10 classes, one per digit)

Trained with Cross-Entropy loss and the Adam optimizer over 5 epochs.

## Result

| Metric | Score |
|---|---|
| Test Accuracy | 0.9894 (98.94%) |

Training loss dropped from 0.2226 (epoch 1) to 0.0257 (epoch 5), showing clean, steady learning with no signs of instability. Sample predictions on test images matched their true labels correctly.

## What I Learned

I built a simple Convolutional Neural Network (CNN) that classifies handwritten digits with 98.94% test accuracy after just 5 epochs of training.

The biggest thing I learned is why CNNs work so well for images: the convolutional layers scan the image with small filters to automatically detect visual patterns like edges and curves, instead of treating every pixel as an independent, unrelated input the way a plain feedforward network would. The pooling layers then shrink the data while keeping the important features, which both speeds up training and helps the model generalize instead of overfitting to exact pixel positions.

Compared to the feedforward network I built in Week 9 on the diabetes dataset (which struggled with only ~770 rows), this result really shows how much a well-matched architecture and a large, clean dataset (60,000 training images) can improve results — MNIST is a much easier problem for a neural network than the tabular diabetes data was.

## Tools Used

- Python, Jupyter Notebook
- PyTorch (torch, torch.nn, torch.optim)
- torchvision (datasets, transforms)
- matplotlib

## Files

- `mnist_classifier.ipynb` — a simple CNN trained to classify handwritten digits from the MNIST dataset

## Next Up

Week 11: Model deployment basics — saving this trained model and building a simple Streamlit app around it.
# Week 11 – Model Deployment Basics

Part of my [AI-ML-Internship](https://github.com/Bhaskar-Mehta/AI-ML-Internship) under mentor **Anurag Sharma**.

## Overview

This week was about taking a trained model out of a notebook and turning it into something other people can use. I saved the MNIST digit classifier from Week 10 and built a small Streamlit web app around it. You give it a digit image and it predicts which digit it is.

## What I Did

- **Day 1:** Moved the CNN into its own file (`model.py`), retrained it, and saved the weights to `mnist_cnn.pt`
- **Day 2:** Reloaded the saved weights into a fresh model and checked it still works (test accuracy 0.9855)
- **Day 3:** Built the Streamlit app (`app.py`) with two ways to try the model
- **Day 4:** Ran the app locally and tested it with sample inputs
- **Day 5:** Wrote this README

## How the App Works

The app has two tabs:

- **Upload an image:** upload a PNG or JPG of a single digit. The app converts it to grayscale, flips it if it is dark-on-light, resizes it to 28x28, and shows what the model sees.
- **Try a test image:** pick an image from the MNIST test set (by index or with a random button) and compare the prediction to the true label.

For each image the app shows the predicted digit, the confidence, and a bar chart of the probability for every digit 0–9.

## How to Run It

1. Install the requirements:
```
pip install -r requirements.txt
```
2. From this folder, start the app:
```
streamlit run app.py
```
3. Open `http://localhost:8501` in your browser (it usually opens by itself).

`mnist_cnn.pt` must be in the same folder as `app.py`. The MNIST test set downloads automatically on first run.

## Files

- `model.py` — the CNN definition, shared by the notebook and the app
- `save_model.ipynb` — trains the model, saves it to `mnist_cnn.pt`, and reloads it to verify
- `mnist_cnn.pt` — the saved model weights
- `app.py` — the Streamlit app
- `requirements.txt` — Python packages needed to run the app

## Results

The reloaded model scored **0.9855** test accuracy, in line with the 0.9894 from Week 10 (the model was retrained here, so the numbers differ slightly).

## Limitations

- The model is trained only on MNIST, so it expects a single, centred digit. When I uploaded an image that was not a digit (a screenshot), it gave a low-confidence answer (about 20%) with probability spread across all digits, which is the model effectively saying it is unsure.
- Hand-drawn or photographed digits may be less accurate than MNIST test images, because MNIST digits are cleanly centred and scaled.

## What I Learned

A trained model is just a file of weights. To deploy it, I needed to keep the model definition in a separate file, save and reload the weights, and wrap the prediction in a simple interface. Reloading the model and re-checking its accuracy before building the app was a useful sanity check. Testing with an input the model was never trained for also showed why showing the confidence matters.

## Tools Used

- Python, PyTorch, torchvision
- Streamlit
- Pillow, NumPy

## Next Up

Week 12: Capstone project and wrap-up.
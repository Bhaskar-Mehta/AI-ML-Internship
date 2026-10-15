import random
import torch
import numpy as np
import streamlit as st
from PIL import Image, ImageOps
from torchvision import datasets, transforms
from model import SimpleCNN

st.set_page_config(page_title="Digit Classifier", page_icon="🔢")


@st.cache_resource
def load_model():
    model = SimpleCNN()
    model.load_state_dict(torch.load("mnist_cnn.pt", map_location="cpu"))
    model.eval()
    return model


@st.cache_data
def load_test_data():
    return datasets.MNIST(root="./data", train=False, download=True,
                          transform=transforms.ToTensor())


def predict(img_tensor):
    with torch.no_grad():
        logits = model(img_tensor.unsqueeze(0))
        probs = torch.softmax(logits, dim=1)[0]
    return int(probs.argmax()), probs.numpy()


def show_result(digit, probs):
    st.success(f"Predicted digit: **{digit}**  (confidence {probs[digit]*100:.1f}%)")
    st.bar_chart(probs)


model = load_model()

st.title("Handwritten Digit Classifier")
st.write("A small CNN trained on MNIST (98.9% test accuracy). "
         "Upload an image of one digit, or try an image from the MNIST test set.")

tab1, tab2 = st.tabs(["Upload an image", "Try a test image"])

with tab1:
    file = st.file_uploader("Upload a PNG or JPG of a single digit", type=["png", "jpg", "jpeg"])
    if file is not None:
        img = Image.open(file).convert("L")
        if np.array(img).mean() > 127:      # dark digit on light background -> flip it
            img = ImageOps.invert(img)
        img = img.resize((28, 28))
        st.image(img, caption="What the model sees (28x28)", width=150)
        digit, probs = predict(transforms.ToTensor()(img))
        show_result(digit, probs)

with tab2:
    test_data = load_test_data()
    if "idx" not in st.session_state:
        st.session_state.idx = 0
    if st.button("Random test image"):
        st.session_state.idx = random.randint(0, len(test_data) - 1)
    idx = st.number_input("Test image index", 0, len(test_data) - 1, key="idx")
    image, true_label = test_data[idx]
    st.image(image.squeeze().numpy(), caption=f"True label: {true_label}", width=150)
    digit, probs = predict(image)
    show_result(digit, probs)
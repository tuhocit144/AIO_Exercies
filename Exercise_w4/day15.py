import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image
import streamlit as st
import torch.nn as nn
import os
CLASS_NAMES = ['Dyskeratotic',
               'Koilocytotic',
               'Metaplastic',
               'Parabasal',
               'Superficial - Intermediate']
MODEL_NAME = 'model_weights.pth'


def predict(model_name, img_path):
    # load the model
    model = models.resnet152(pretrained=True)
    model.fc = nn.Linear(in_features=2048, out_features=5, bias=True)
    weights = torch.load(model_name, map_location='cpu')
    model.load_state_dict(weights)

    # preprocess the image
    prep_img_mean = [0.485, 0.456, 0.406]
    prep_img_std = [0.229, 0.224, 0.225]
    transform = transforms.Compose(
        [
            transforms.Resize(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=prep_img_mean, std=prep_img_std
                                 ),
        ]
    )
    image = Image.open(img_path)
    preprocessed_image = transform(image).unsqueeze(0)

    # predict the class
    model.eval()
    output = model(preprocessed_image)
    pred_idx = torch.argmax(output, dim=1)
    predicted_class = CLASS_NAMES[pred_idx]
    return predicted_class


def getpath_of_image(filename):
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    path_file = current_directory + filename
    return path_file


def mainprocess():
    myfile = 'datatest.png'
    myfile = getpath_of_image(myfile)
    st.title('Cervical Cancer Classification App')
    file = st.file_uploader('Choose an image to classification', type=[
                            'jpg', 'png', 'jpeg'])
    if st.button("Predict"):
        if file is not None:

            try:
                model_name = getpath_of_image("/models/"+MODEL_NAME)
                predict_result = predict(model_name, file)
                col1, col2 = st.columns(2)
                col1.title(predict_result)
                col2.image(file)
            except:
                st.write('Not detected object')


mainprocess()

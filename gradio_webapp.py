import gradio as gr
import requests
import torch
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from torchvision import transforms
import numpy as np
import torchvision.models as models
mobilenet = models.mobilenet_v3_large(pretrained=True)
model = torch.nn.Sequential(mobilenet.features, mobilenet.avgpool, torch.nn.Flatten())
# Load the CSV file into a DataFrame
paths_df = pd.read_csv('paths_list_960_full.csv')

# Extract the 'path' column as a list
df = paths_df['path'].tolist()

# Load the model using its relative path
mobilenet = models.mobilenet_v3_large(pretrained=True)
model = torch.nn.Sequential(mobilenet.features, mobilenet.avgpool, torch.nn.Flatten())
model.eval()
# Define the normalization transform
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
normalize = transforms.Normalize(mean=mean, std=std)

# Define the transformation pipeline
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def process_image(image):
    image = Image.fromarray((image * 255).astype(np.uint8))
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0) 
    with torch.no_grad():
        features = model(input_batch)
    vector= features.squeeze()
    #print("Feature vector extracted from the input image:", vector[:20])
    response = requests.post('http://annoy-db:5000/reco', json={'vector': vector.tolist()})
    if response.status_code == 200:
        indices = response.json()
        paths = [df[idx] for idx in indices]
        fig, axs = plt.subplots(1, len(paths), figsize=(5 * len(paths), 5))
        for i, path in enumerate(paths):
            img = Image.open(path)
            axs[i].imshow(img)
            axs[i].axis('off')
        return fig
    else:
        return "Error in API request"
iface = gr.Interface(fn=process_image, inputs="image", outputs="plot")
iface.launch(server_name="0.0.0.0")
from flask import Flask, request, jsonify
import torch
import torchvision.transforms as transforms
from PIL import Image
import os
from utils import load_model, preprocess_image

app = Flask(__name__)

from constants import CLASS_NAMES

MODEL = load_model('model.pth', CLASS_NAMES)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    try:
        image = Image.open(file).convert('RGB') 
        img_tensor = preprocess_image(image)

        with torch.no_grad():
            output = MODEL(img_tensor)
            _, pred = torch.max(output, 1) #rn its highest probability class but I could return the percent
            prediction = CLASS_NAMES[pred.item()]

        return jsonify({'flower_type': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
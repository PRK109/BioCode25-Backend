# BioCode25-Backend



# server.py:
```
from flask import Flask, request, jsonify
from utils import load_model, process_image
from constants import CLASS_NAMES

app = Flask(__name__)

MODEL = load_model('model.pth', CLASS_NAMES)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    try:
        p_class, probs = process_image(file, MODEL, CLASS_NAMES)

        return jsonify({
            'predicted_disease': p_class,
           #'probabilities': probs
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

testing.py:
```
import requests
import os

image_path = os.path.join(os.getcwd(), 'sk.jpg')

# Check if the image exists
if os.path.exists(image_path):
    with open(image_path, 'rb') as img:
        files = {'file': img}
        try:
            response = requests.post("http://127.0.0.1:5000/predict", files=files)
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Error: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
else:
    print("That image doesn't exist")
```


constants.py:
```
CLASS_NAMES = ['abscess', 'ards', 'atelectasis', 'atherosclerosis of the aorta',
               'cardiomegaly', 'emphysema', 'fracture', 'hydropneumothorax',
               'hydrothorax', 'pneumonia', 'pneumosclerosis',
               'post-inflammatory changes', 'post-traumatic ribs deformation', 'sarcoidosis',
               'scoliosis', 'tuberculosis', 'venous congestion']
```

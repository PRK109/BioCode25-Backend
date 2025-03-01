import requests
import os
image_path = os.path.join(os.getcwd(), 'sf.jpg')

if os.path.exists(image_path):
    with open(image_path, 'rb') as img:
        files = {'file': img}
        response = requests.post("http://127.0.0.1:5000/predict", files=files)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
else:
    print("that image dont exist")

from flask import Flask, request, jsonify
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import json
import requests
import cv2

app = Flask(__name__)

api_key = "AIzaSyDlp19ogXeUuugzO3UZYRUqL9RVSzo2nQk"

@app.route('/booktitle', methods=["POST"])

def getbooktitle():
    file = request.files['image']
    img = Image.open(file.stream)
    booktitle = pytesseract.image_to_string(img)

    url = f"https://www.googleapis.com/books/v1/volumes?q={booktitle}&key={api_key}"
    response = requests.get(url)
    json_response = response.json()
    volume_info = json_response['items'][0]['volumeInfo']
    title = volume_info.get('title')
    author = volume_info.get('authors')
    images_link = volume_info['imageLinks']
    #small_image = images_link['smallThumbnail']
    data = {
        'title': title,
        'author': author,
        'images_links': images_link
    }
    data_in_json = json.dumps(data)

    return data_in_json

if __name__ == "__main__":
    app.run()

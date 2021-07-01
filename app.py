from flask import Flask, request, jsonify
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import json
import requests
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getbooktitle():
    if request.method == "POST":
        file = request.files['file']
        if file:
            image = Image.open(file)
            booktitle = pytesseract.image_to_string(image)
            return booktitle


api_key = "AIzaSyDlp19ogXeUuugzO3UZYRUqL9RVSzo2nQk"

url = f"https://www.googleapis.com/books/v1/volumes?q={booktitle}&key={api_key}"
response = requests.get(url)
json_response = response.json()
volume_info = json_response['items'][0]['volumeInfo']
api_title = volume_info.get('title')
api_author = volume_info.get('authors')
images_link = volume_info['imageLinks']
small_image= images_link['smallThumbnail']
data = {
'title': title,
'author': author,
'images_links': images_link
}
data_in_json = json.dumps(data)


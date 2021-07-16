from flask import Flask, request, jsonify
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
from PIL import Image
import requests


app = Flask(__name__)

@app.route("/getbook", methods=["POST"])
def getbooktitle():
    if request.method == "POST":
        file = request.files['image']
        img = Image.open(file.stream)
        booktitle = pytesseract.image_to_string(img)

        api_key = "AIzaSyDNBwiEqYoB0M54qgxi1OOAUBCG1-5lmHA"
        url = f"https://www.googleapis.com/books/v1/volumes?q={booktitle}&key={api_key}"
        response = requests.get(url)
        json_response = response.json()
        volume_info = json_response['items'][0]['volumeInfo']
        title = volume_info.get('title')
        author = volume_info.get('authors')
        imageslink = volume_info['imageLinks']
        smallimage = imageslink['smallThumbnail']
        return jsonify({"books": [{'title': title, 'author': author[0], 'imageLink': smallimage}]})

if __name__ == "__main__":
    app.run()

# This code is for webhook that extracts text from an uploaded PDF document using the Google Cloud Vision API
from flask import Flask, request, jsonify
from google.cloud import vision_v1
from google.protobuf import json_format

app = Flask(__name__)

# Initialize the Google Cloud Vision client
client = vision_v1.ImageAnnotatorClient()

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON request from Dialogflow
    request_data = request.get_json()

    # Extract the URL of the uploaded contract document from the request
    document_url = request_data['queryResult']['parameters']['document_url']

    # Perform OCR on the document
    text = extract_text_from_document(document_url)

    # Prepare a response for Dialogflow
    response = {
        'fulfillmentText': text,
    }

    return jsonify(response)

def extract_text_from_document(document_url):
    # Use the Google Cloud Vision API to extract text from the document
    image = vision_v1.Image()
    image.source.image_uri = document_url

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return "No text found in the document."

if __name__ == '__main__':
    app.run(port=8080)

# This code is for webhook that extracts text from an uploaded PDF document using the Google Cloud Vision API  


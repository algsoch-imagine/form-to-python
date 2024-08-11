from flask import Flask, request, send_from_directory
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_uri = "mongodb://localhost:27017/"
client = MongoClient(mongo_uri)
db = client['vicky']
collection = db['contact_forms']

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    gmail = request.form['gmail']
    subject = request.form['subject']
    details = request.form['details']

    # Insert into MongoDB
    document = {
        'name': name,
        'gmail': gmail,
        'subject': subject,
        'details': details
    }
    collection.insert_one(document)

    # Show thank you message
    return '''
        <html>
        <head>
            <title>Thank You</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f4f4f4;
                }
                .message-container {
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    width: 300px;
                    text-align: center;
                }
                h1 {
                    color: #333;
                }
            </style>
        </head>
        <body>
            <div class="message-container">
                <h1>Thank You!</h1>
                <p>Thank you for your interest. We will contact you soon.</p>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

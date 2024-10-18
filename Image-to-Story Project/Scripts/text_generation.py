import os
import base64
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

#Load environment variables from .env
load_dotenv()

app = Flask(__name__)

#Grabbing API Key from .env
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

#Setting folder for storage of uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Checking if upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_image_description(image_path):

    '''Function to get image description using DALL-E'''

    try:
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this image in detail."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ],
                }
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error getting image description: {e}")
        return "An image of unknown contents."

def generate_story(prompt):

    ''' This function is prompting the GPT to create a short story with the generated image description. 
        Incorporates exception handling incase of any issues '''
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative story writer."},
                {"role": "user", "content": f"Write a short story based on this image description: {prompt}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating story: {e}")
        return "Sorry, we couldn't generate a story at this time."

@app.route('/', methods=['GET'])
def main_page():
    return render_template('landing_page.html')

@app.route('/generate-story', methods=['POST'])
def generate_story_route():

    ''' Handling User Requests and Validating Files/File type, and returns the story with an image url '''

    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        image_description = get_image_description(filename)
        story = generate_story(image_description)

        return jsonify({'story': story, 'image_url': filename})

    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
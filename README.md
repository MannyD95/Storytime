# Storytime: A GenAI Narrative App
<br>

## Background <br>
The Intention with this application is to act as a proof of concept that we can randomly generate unique stories based on an uploaded .jpeg file. <br>
The idea came about after family members remarked how hard it was to get children's books at the library for my nephew. <br>
Ideally, after future iterations it could seamlessly generate short stories that are appropriate for someone his age. <br>
Also, I wanted to try out web dev, thus the choice of using Flask and boilerplate HTML with some JS for async and backend communication <br>

## Running the App <br>
As of writing, it is not hosted publically, so to run the app you would need to clone the repo locally. Also, be sure to have the necessary libraries installed: <br>

pip install Flask <br>
pip install openai <br>

To protect your OpenAI API key, set up the necessary environment variables by creating a .env file in the root directory <br>
> i.e OPENAI_API_KEY=your-openai-api-key
<br>
Make sure the static/uploads directory exists to store uploaded images. You can manually create it with: mkdir -p static/uploads <br>
<br>
Run the Application with flask by inputting flask run at the command line, and the local server will be launched <br>

## Future Considerations/Roadmap <br>
I want to make this program more feature-complete, this will involve: <br>
> ability to fine tune narrative text based on reading level
> 
> incorporating AI image generation in combintion with text generation to remove the need for uploading and become one-button operational
> 
> A toggle for genres and/or flavour text
> 
> Troubleshooting .png image previewing and optimizing file storage

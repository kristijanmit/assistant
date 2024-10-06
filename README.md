# assistant

This project is an AI-powered assistant built using Python, FastAPI, and Langchain's integration with Ollama for natural language processing. It also includes text-to-speech and speech recognition functionality, allowing the assistant to both listen to and speak to the user.

Features

- Textual Input/Output API: Interact with the assistant via a RESTful API.
- Natural Language Processing: The assistant uses the Ollama model for conversational AI.
- Weather Search: The assistant can fetch current weather data for any city.
- Web Search: The assistant can search the web for answers.
- Text-to-Speech: The assistant can read out responses using the pyttsx3 library.
- Speech Recognition: The assistant can listen to and transcribe voice input using speech_recognition.

Run the Setup Script

- ./start_api.sh

Manual Setup (Optional)

- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- uvicorn ai_assistant.api:app --reload

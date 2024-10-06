from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jarvis.conversation import handle_textual_input  # Import the new function

app = FastAPI()

# Define a Pydantic model for the expected JSON input
class ChatInput(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Assistant API"}

@app.post("/chat")
def chat(input: ChatInput):
    """
    Send a textual input to the assistant and receive a response.
    """
    try:
        response = handle_textual_input(input.user_input)  # Use the new function here
        return {"user_input": input.user_input, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

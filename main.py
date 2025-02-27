import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],  
    allow_headers=["*"],
)

@app.get("/")
def get_integration_json():
    with open('integration.json', 'r') as file:
        integration_json = json.load(file)
    return integration_json

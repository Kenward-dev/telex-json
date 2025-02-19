import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_integration_json():
    with open('integration.json', 'r') as file:
        integration_json = json.load(file)
    return integration_json
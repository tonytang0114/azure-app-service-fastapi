from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def index():
    return [
        {
            "name": "roshi",
            "id": 1
        }
    ]

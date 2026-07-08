from fastapi import FastAPI

app = FastAPI(
    title="Repair Workshop Analytics",
    version="0.0.1"
)

@app.get("/")
def home():
    return {
        "project": "Repair Workshop Analytics",
        "version": "0.0.1",
        "status": "Backend running correctly"
    }

from fastapi import FastAPI

app = FastAPI(
    title="TaskFlow API",
    description="Smart task manager with analytics",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"Hello": "TaskFlow API"}
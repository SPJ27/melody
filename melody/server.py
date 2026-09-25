import uvicorn

def run():
    uvicorn.run(
        "melody.application:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
import uvicorn

def run(port=8000, reload=True):
    uvicorn.run(
        "melody.application:app",
        host="127.0.0.1",
        port=port,
        reload=reload
    )
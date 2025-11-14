from fastapi import FastAPI

app = FastAPI(title="BIOSGuardML", version="0.1.0")


@app.get("/health")
def health_check():
    """
    Simple endpoint to verify that the service is running.
    """
    return {"status": "ok", "service": "BIOSGuardML"}

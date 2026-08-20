from fastapi import FastAPI

app = FastAPI(title="FastApi_Project", version="0.1.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

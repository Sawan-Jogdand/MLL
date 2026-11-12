from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

from backend.services import snippet_service

app = FastAPI(title="ML Snippet Backend")


@app.get("/")
def home():
    return {"message": "Use /api/snippets/<name> to fetch a snippet."}


@app.get("/api/snippets")
def list_snippets():
    return {"snippets": snippet_service.list_snippets()}


@app.get("/api/snippets/{name}")
def get_snippet(name: str):
    content = snippet_service.get_snippet(name)
    if content is None:
        raise HTTPException(status_code=404, detail="Snippet not found.")
    return PlainTextResponse(content=content, media_type="text/plain; charset=utf-8")

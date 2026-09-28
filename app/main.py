from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.agent import agent

app = FastAPI(title="AI Ops Assistant")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


class Mesaj(BaseModel):
    metin: str
    thread_id: str = "default"


@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse("app/static/index.html")


@app.post("/chat")
def chat(mesaj: Mesaj) -> dict[str, str]:
    config = {"configurable": {"thread_id": mesaj.thread_id}}
    sonuc = agent.invoke({"messages": [{"role": "user", "content": mesaj.metin}]}, config)
    return {"cevap": sonuc["messages"][-1].content}
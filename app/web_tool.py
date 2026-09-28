from langchain_core.tools import tool
from ddgs import DDGS

@tool
def web_ara(sorgu:str) -> str:
    """Internette guncel bilgi almak icin kullanilir."""
    sonuclar = DDGS().text(sorgu, max_results=3)
    return "\n\n".join(f"{s['title']}: {s['body']}" for s in sonuclar)

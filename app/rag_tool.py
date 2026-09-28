from langchain_core.tools import tool
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

DOKUMANLAR = [
    "CitePilot, PDF dokumanlarda kaynak gosteren bir RAG uygulamasidir. Python ve FastAPI ile yazilmistir.",
    "Support Triage Agent, destek taleplerini kategori ve aciliyete gore siniflandiran bir LangGraph agent'idir.",
    "Predictive Maintenance API, sicaklik ve titresim verisinden makine ariza riskini tahmin eden bir scikit-learn modelidir.",
]


def embed_text(text: str) -> list[float]:
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding

DOKUMAN_VEKTORLERI = [embed_text(d) for d in DOKUMANLAR]

@tool
def dokuman_ara(soru: str) -> str:
    """Bu sistemin kendi dahili proje dokumanlarinda (CitePilot, Support Triage Agent,
    Predictive Maintenance API gibi bu ekibin gelistirdigi projeler) arama yapar.
    Kullanicinin sorusu bu projelerden biriyle ilgiliyse, internette arama yapmadan
    ONCE bu araci kullan."""
    sorgu_vektoru = embed_text(soru)
    skorlar = cosine_similarity([sorgu_vektoru], DOKUMAN_VEKTORLERI).flatten()
    en_iyi_index = skorlar.argmax()
    return DOKUMANLAR[en_iyi_index]
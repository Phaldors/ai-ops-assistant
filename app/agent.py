import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

conn = sqlite3.connect("memory.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from app.rag_tool import dokuman_ara
from app.web_tool import web_ara
from app.maintenance_tool import ariza_tahmini


SISTEM_TALIMATI = (
    "Sen bu ekibin AI projeleri hakkinda soru cevaplayan bir asistansin. "
    "CitePilot, Support Triage Agent ve Predictive Maintenance API bu ekibin "
    "kendi gelistirdigi projelerdir; internette baska sirketlerin ayni veya "
    "benzer isimli urunleriyle karistirma. Bu projeler hakkindaki sorularda "
    "once dokuman_ara aracini kullan, sadece guncel/genel bilgi gerektiginde web_ara'yi kullan."
)

llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(llm,checkpointer=checkpointer, tools=[dokuman_ara, web_ara, ariza_tahmini], system_prompt=SISTEM_TALIMATI)

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "test-1"}}

    sonuc1 = agent.invoke({"messages": [{"role": "user", "content": "Benim adim Arda"}]}, config)
    print(sonuc1["messages"][-1].content)

    sonuc2 = agent.invoke({"messages": [{"role": "user", "content": "Benim adim neydi?"}]}, config)
    print(sonuc2["messages"][-1].content)
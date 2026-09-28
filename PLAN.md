---
title: AI Ops Assistant — Proje Planı
created: 2026-09-28
type: project
status: active
tags: [ai-engineer, portfolio, langgraph, flagship]
---

# AI Ops Assistant

Çok agent'lı, araç kullanan, hafızalı bir yapay zekâ asistanı. CitePilot (RAG),
Support Triage Agent (LangGraph) ve Predictive Maintenance API'de (klasik ML)
öğrenilen her şeyi tek, tutarlı bir sistemde birleştirir. Çok oturuma yayılacak
flagship proje.

## Mimari

- **Router agent (LangGraph):** kullanıcı mesajını okuyup hangi aracın
  gerektiğine karar verir.
- **RAG aracı:** CitePilot'un embedding + cosine similarity mantığı, artık
  agent'ın çağırabileceği bir tool olarak.
- **Web arama aracı:** DuckDuckGo (API key gerektirmiyor, ekstra hesap
  açma sürtünmesi yok).
- **Bakım aracı:** Predictive Maintenance API'nin modelini çağırıp makine
  durumu sorgular.
- **Kalıcı hafıza:** konuşma geçmişi SQLite'ta saklanır, oturumlar arası
  devam eder (şu ana kadarki projelerde hiç veritabanı yoktu — yeni).
- **Arayüz:** tarayıcıda gerçek bir chat ekranı (düz HTML/CSS/JS,
  framework yok — Arda'nın frontend bilgisi kalibre edilecek).
- **Deploy:** Docker + Render, aynı akış CitePilot'taki gibi.

## İlerleme

- [x] Proje iskeleti kuruldu
- [x] Router agent (tek tool ile başla: RAG) — `langchain.agents.create_agent` + `dokuman_ara` tool'u çalışıyor
- [x] Web arama aracı eklendi — `ddgs` ile, tool selection sorunu (isim çakışması) docstring+system prompt ile düzeltildi
- [x] Bakım aracı eklendi — Predictive Maintenance modeli tool olarak çağrılıyor
- [x] SQLite ile kalıcı hafıza — `SqliteSaver` checkpointer, `thread_id` ile konuşma devam ediyor
- [x] Chat arayüzü (frontend) — düz HTML/CSS/JS, FastAPI `/chat` endpoint'i, Arda için ilk frontend deneyimi
- [x] Docker — build + container testi başarılı
- [ ] Deploy
- [ ] Mock mülakat

## Notlar

- Arda'nın frontend deneyimi: (kalibre edilecek)
- Bu proje önceki üçünü (CitePilot, Support Triage Agent, Predictive
  Maintenance API) mimari olarak birleştiriyor, tekrar sıfırdan yazmıyor —
  var olan kodun mantığını yeniden kullanıyoruz.

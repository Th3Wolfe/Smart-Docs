# 📄 SmartDocs

Plataforma inteligente de análise documental com IA utilizando FastAPI, RAG, ChromaDB e modelos locais via Ollama.

---

# 🎯 Objetivo

O SmartDocs permite que usuários façam upload de documentos como:

- PDF  
- DOCX  
- XLSX  
- CSV  

E interajam com eles usando linguagem natural.

O sistema processa os arquivos, divide em chunks, gera embeddings vetoriais e permite consultas inteligentes baseadas no conteúdo dos documentos, tudo executado localmente sem dependência de APIs pagas.

---

# 🚀 Funcionalidades atuais

- Upload de documentos
- Extração de texto de PDFs e arquivos
- Processamento e divisão em chunks
- Geração de embeddings locais via Ollama
- Armazenamento vetorial com ChromaDB
- Busca semântica de contexto (RAG)
- Chat com documentos via `/ask`
- Respostas geradas por LLM local (Qwen3)

---

# 🧠 Arquitetura do projeto

Usuário → FastAPI → Pipeline RAG → ChromaDB (busca vetorial) → Ollama (Qwen3)

---

# 🛠️ Stack do projeto

## Backend
- Python
- FastAPI

## IA e RAG
- Ollama
- Qwen3
- Embeddings locais (nomic-embed-text)

## Vetores
- ChromaDB

## Banco de dados (futuro)
- PostgreSQL

---

# 📁 Estrutura do projeto

```txt
smartdocs/
├── backend/
│   ├── app/
│   │   ├── services/
│   │   ├── uploads/
│   │   ├── chroma_db/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/ (futuro)
├── docs/
├── scripts/
├── README.md
└── .gitignore

---

# 🔄 Fluxo do sistema (RAG)

1. Upload de documentos  
2. Extração de texto  
3. Limpeza e chunking  
4. Geração de embeddings  
5. Armazenamento no ChromaDB  
6. Busca semântica por similaridade  
7. Geração de resposta via Ollama  

---

# 🧪 Endpoints atuais

- GET `/` → health check  
- POST `/upload` → upload de documentos  
- GET `/chat?prompt=` → chat simples  
- GET `/ask?query=` → chat com RAG  
- GET `/debug/chroma` → debug do banco vetorial  

---

# ⚙️ IA local (Ollama)

Instalar Ollama:
https://ollama.com

Modelo principal:
ollama pull qwen3:8b

Embeddings:
ollama pull nomic-embed-text

Testar:
ollama run qwen3:8b

---

# 🧠 Status do projeto

🚧 MVP funcional em desenvolvimento

✔ Upload funcionando  
✔ Chunking funcionando  
✔ Embeddings funcionando  
✔ ChromaDB funcionando  
✔ RAG básico funcionando  
✔ Chat com contexto funcionando  

---

# 🗺️ Roadmap

## MVP atual
- Backend FastAPI
- Upload de documentos
- Pipeline RAG básico
- ChromaDB
- Ollama local

## Próximos passos
- Melhorar chunking semântico
- Streaming de respostas
- Interface Streamlit (chat estilo ChatGPT)
- Histórico de conversas
- Resumos automáticos
- Cards de insights
- Multi-documentos

---

# 🧪 Como executar

## Backend

cd backend  
python -m venv venv  
.\venv\Scripts\activate  
pip install -r requirements.txt  
uvicorn app.main:app --reload  

---

## Acesso

API: http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs  

---

# 🧠 Objetivo do projeto

- aprendizado prático de IA aplicada  
- RAG (Retrieval-Augmented Generation)  
- engenharia de software com IA  
- sistemas locais com LLMs  
- busca semântica em documentos  
- arquitetura backend moderna  

---

# 👨‍💻 Autor

Iago Martins
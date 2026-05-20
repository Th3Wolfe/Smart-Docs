# SmartDocs

Plataforma inteligente de análise documental com IA utilizando FastAPI, LangChain, ChromaDB e modelos locais via Ollama.

---

## Objetivo

O SmartDocs permite que usuários façam upload de documentos como:

* PDF
* DOCX
* XLSX
* CSV

E interajam com os dados utilizando linguagem natural através de inteligência artificial.

O sistema processa os arquivos, gera embeddings vetoriais e disponibiliza um chat inteligente para consultas contextualizadas, tudo executado localmente sem dependência de APIs pagas.

---

## Funcionalidades planejadas

* Upload de documentos
* Processamento de PDFs, DOCX e planilhas
* Chat inteligente com documentos
* Busca semântica
* Resumos automáticos
* Extração de insights
* Histórico de conversas
* Dashboard inteligente
* Suporte a múltiplos documentos
* Geração automática de cards informativos
* Pipeline local de IA sem custos de API

---

## Arquitetura do projeto

```txt
Usuário
   ↓
Frontend Streamlit
   ↓
FastAPI
   ↓
LangChain
   ↓
ChromaDB
   ↓
Ollama (Qwen3)
```

---

## Stack do projeto

### Backend

* Python
* FastAPI

### IA e RAG

* LangChain
* Ollama
* Qwen3

### Embeddings

* Nomic Embed Text

### Banco vetorial

* ChromaDB

### Banco de dados

* PostgreSQL

### Frontend

* Streamlit

---

## Estrutura do projeto

```bash
smartdocs/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── rag/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── chroma_db/
│   ├── tests/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── pages/
│   ├── components/
│   ├── services/
│   └── app.py
│
├── docs/
├── docker/
├── scripts/
│
├── README.md
├── .gitignore
└── docker-compose.yml
```

---

## Fluxo do sistema

### 1. Upload de documentos

O usuário envia arquivos para análise.

### 2. Processamento

O sistema:

* extrai texto
* limpa conteúdo
* divide em chunks
* gera embeddings vetoriais

### 3. Armazenamento vetorial

Os embeddings são armazenados no ChromaDB.

### 4. Interação inteligente

O usuário pode conversar com os documentos utilizando linguagem natural.

### 5. Insights automáticos

O sistema poderá gerar automaticamente:

* resumos
* tópicos principais
* entidades importantes
* palavras-chave
* insights relevantes

---

## Status do projeto

🚧 Em desenvolvimento

---

## Roadmap

### MVP

* [x] Estrutura inicial do projeto
* [x] Backend FastAPI
* [x] Integração com Ollama
* [x] Endpoint inicial de chat
* [ ] Upload de documentos
* [ ] Processamento de PDF/DOCX
* [ ] Integração com embeddings locais
* [ ] Pipeline RAG
* [ ] Chat contextual com documentos

### Futuras melhorias

* Autenticação de usuários
* OCR para documentos escaneados
* Processamento assíncrono
* Dashboard analítico
* Agentes de IA
* Exportação de relatórios
* Suporte multiusuário
* Comparação entre documentos

---

## Como executar o projeto

### Backend

Acesse a pasta:

```bash
cd backend
```

Crie e ative o ambiente virtual:

#### Windows PowerShell

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o servidor:

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```txt
http://127.0.0.1:8000
```

Documentação automática:

```txt
http://127.0.0.1:8000/docs
```

---

## IA Local

O SmartDocs utiliza modelos locais através do Ollama.

### Instalar Ollama

[https://ollama.com](https://ollama.com)

### Instalar modelo principal

```bash
ollama pull qwen3:8b
```

### Testar modelo

```bash
ollama run qwen3:8b
```

### Instalar modelo de embeddings

```bash
ollama pull nomic-embed-text
```

---

## Endpoints atuais

### Verificar API

```http
GET /
```

### Chat com modelo local

```http
GET /chat?prompt=sua_pergunta
```

---

## Objetivo do projeto

Este projeto foi desenvolvido com foco em:

* aprendizado prático de IA aplicada
* RAG (Retrieval-Augmented Generation)
* processamento documental
* engenharia de software
* arquitetura backend moderna
* aplicações locais de LLMs
* busca semântica
* sistemas inteligentes de documentos

---

## Autor

Iago Martins

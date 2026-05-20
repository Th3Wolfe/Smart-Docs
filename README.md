# SmartDocs

Plataforma inteligente de análise documental com IA utilizando FastAPI, LangChain, ChromaDB e PostgreSQL.

---

## Objetivo

O SmartDocs permite que usuários façam upload de documentos como:

- PDF
- DOCX
- XLSX
- CSV

e interajam com os dados utilizando linguagem natural através de inteligência artificial.

O sistema processa os arquivos, gera embeddings vetoriais e disponibiliza um chat inteligente para consultas contextualizadas.

---

## Funcionalidades planejadas

- Upload de documentos
- Processamento de PDFs, DOCX e planilhas
- Chat com documentos usando IA
- Busca semântica
- Resumos automáticos
- Extração de insights
- Histórico de conversas
- Dashboard inteligente
- Suporte a múltiplos documentos

---

## Stack do projeto

### Backend
- Python
- FastAPI

### IA
- LangChain
- OpenAI API

### Banco vetorial
- ChromaDB

### Banco de dados
- PostgreSQL

### Frontend
- Streamlit

---

## Estrutura do projeto

```bash
smartdocs/
│
├── backend/
│   ├── app/
│   ├── uploads/
│   ├── chroma_db/
│   └── tests/
│
├── frontend/
│   ├── pages/
│   ├── components/
│   └── services/
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

## Status do projeto

🚧 Em desenvolvimento

---

## Futuras melhorias

- Autenticação de usuários
- OCR para documentos escaneados
- Processamento assíncrono
- Deploy em nuvem
- Dashboard analítico
- Agentes de IA
- Exportação de relatórios

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

## Autor

Iago Martins
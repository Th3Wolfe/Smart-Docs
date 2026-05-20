import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(prompt: str, context: str = ""):
    full_prompt = f"""
Você é um assistente que responde SOMENTE com base no contexto abaixo.

Se a resposta não estiver no contexto, diga que não encontrou informação.

---

CONTEXTO:
{context}

---

PERGUNTA:
{prompt}

---

RESPOSTA:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3:8b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]
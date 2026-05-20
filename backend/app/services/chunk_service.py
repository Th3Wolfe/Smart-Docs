import re

def create_chunks(text: str, chunk_size: int = 800):

    # normaliza espaços
    text = re.sub(r'\s+', ' ', text).strip()

    sentences = re.split(r'(?<=[.!?]) +', text)

    chunks = []
    current = ""

    for s in sentences:
        if len(current) + len(s) < chunk_size:
            current += " " + s
        else:
            chunks.append(current.strip())
            current = s

    if current:
        chunks.append(current.strip())

    return chunks
import re


def clean_text(text: str):

    # Remove espaços excessivos
    text = re.sub(r"\s+", " ", text)

    # Corrige palavras separadas letra por letra
    text = re.sub(r"(\b\w\s){3,}\w\b", lambda m: m.group().replace(" ", ""), text)

    # Remove espaços duplicados novamente
    text = re.sub(r"\s+", " ", text)

    return text.strip()
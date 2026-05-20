import re


def fix_spaced_words(text: str):

    pattern = r'\b(?:[A-ZÀ-Úa-zà-ú]\s+){2,}[A-ZÀ-Úa-zà-ú]\b'

    matches = re.findall(pattern, text)

    for match in matches:

        corrected = match.replace(" ", "")

        text = text.replace(match, corrected)

    return text


def restore_sentence_spacing(text: str):

    # separa palavras coladas por maiúsculas
    text = re.sub(
        r'([a-zà-ú])([A-ZÀ-Ú])',
        r'\1 \2',
        text
    )

    # separa palavras longas coladas
    text = re.sub(
        r'(?<=[a-zà-ú])(?=[A-ZÀ-Ú][a-zà-ú])',
        ' ',
        text
    )

    return text


def clean_text(text: str):

    # Corrige palavras espaçadas
    text = fix_spaced_words(text)

    # Restaura espaços entre palavras coladas
    text = restore_sentence_spacing(text)

    # Remove múltiplos espaços
    text = re.sub(r"\s+", " ", text)

    return text.strip()
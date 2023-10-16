import random

def escolher_palavra():
    palavras = ["musica", "python", "programacao", "jogo", "computador", "teste", "openai"]
    return random.choice(palavras)

def desenhar_forca(erros):
    forca = [
        "----------",
        "|        |",
        "|",
        "|",
        "|",
        "|",
    ]

    if erros > 0:
        forca[2] = "|        @"
        if erros > 1:
            forca[3] = "|        |"
        if erros > 2:
            forca[3] = "|       /|"
        if erros > 3:
            forca[3] = "|       /|\\"
        if erros > 4:
            forca[4] = "|        /"
        if erros > 5:
            forca[4] = "|        /\\"

    return forca

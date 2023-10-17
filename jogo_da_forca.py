from funcoes_forca import escolher_palavra, desenhar_forca

def jogar_forca():
    palavra = escolher_palavra()
    letras_user = []
    chances = 6
    letras_usadas = []
    erros = 0

    while True:
        for linha in desenhar_forca(erros):
            print(linha)

        for letra in palavra:
            if letra.lower() in letras_user:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print(f"\nVocê ainda tem {chances - erros} chances.")
        tentativa = input("Advinhe uma letra: ").lower()
        letras_usadas.append(tentativa)

        if tentativa in letras_user:
            print("Você já tentou essa letra.")
        else:
            letras_user.append(tentativa)
            if tentativa not in palavra:
                erros += 1

        print('Você usou: ' + ',' .join(letras_usadas))
        if erros == chances:
            break

        if set(letras_user) == set(palavra):
            break

    for linha in desenhar_forca(erros):
        print(linha)

    if set(letras_user) == set(palavra):
        print(f"Parabéns! Você acertou a palavra '{palavra}'.")
    else:
        print(f"Você perdeu. A palavra era '{palavra}'.")

if __name__ == "__main__":
    jogar_forca()

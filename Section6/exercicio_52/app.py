text = input("Digite um texto: ")

def text_length(text):
    if len(text) > 20:
        return "O texto é longo"
    if len(text) < 20:
        return "O texto é curto"
    return "O texto é igual a 20"

print(text_length(text))
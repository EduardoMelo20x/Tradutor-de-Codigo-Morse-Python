#Tradutor de codigo morse

import os

while True:    
    print("""\n\n ----------------------- TRADUTOR DE CODIGO MORSE -----------------------\n
        Com esse sistema voce poderá traduzir palavras para o Codigo morse e tambem o inverso,
        Para continuar digite "INICIAR" ou se desejar sair do sistema digite "SAIR" \n""")

    exit_or_start = input("Digite: ").strip().lower()
           
    if exit_or_start == 'iniciar':
        iniciar = True
        break
    
    elif exit_or_start == 'sair':
        iniciar = False
        break
           
    else: 
        os.system('cls')
        print("Entrada inválida! Por favor, digite 'iniciar' para começar ou 'sair' para encerrar. \n")

while iniciar == True:
    print("""\nQual o tipo de conversão que deseja realizar?
          
    1 - MORSE / PORTUGUES
    2 - PORTUGUES / MORSE""")
    
    choice_convert = input("\nDigite: ")

    if choice_convert == '1':
        start_convert = True
        break
        
    elif choice_convert == '2':    
        start_convert = False            
        break
    
    else:
        os.system('cls')
        print("Entrada inválida! Por favor insira uma das opções apresentadas.\n")
        

# Dicionário para texto -> código Morse
texto_para_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
    'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

# Dicionário para código Morse -> texto
morse_para_texto = {value: key for key, value in texto_para_morse.items()}

def texto_para_codigo_morse(texto):
    morse = ""
    for char in texto.lower():
        if char in texto_para_morse:
            morse += texto_para_morse[char] + " "
        else:
            morse += "? "  # Simbolo para caracteres não reconhecidos
    return morse.strip()

def codigo_morse_para_texto(morse):
    texto = ""
    palavras = morse.split(" / ")
    for palavra in palavras:
        letras = palavra.split()
        for letra in letras:
            if letra in morse_para_texto:
                texto += morse_para_texto[letra]
            else:
                texto += "?"  # Simbolo para códigos não reconhecidos
        texto += " "
    return texto.strip()

# Loop principal do programa
while True:
    os.system('cls')  # Limpa o console
    print("""\n\n ----------------------- TRADUTOR DE CODIGO MORSE -----------------------\n
        Com esse sistema voce poderá traduzir palavras para o Codigo morse e tambem o inverso,
        Para continuar digite "INICIAR" ou se desejar sair do sistema digite "SAIR" \n""")

    exit_or_start = input("Digite: ").strip().lower()

    if exit_or_start == 'iniciar':
        while True:
            os.system('cls')
            escolha = input("Digite '1' para texto -> código Morse ou '2' para código Morse -> texto (ou 'sair' para sair): ").strip().lower()

            if escolha == '1':
                texto = input("Digite o texto a ser traduzido para código Morse: ")
                resultado = texto_para_codigo_morse(texto)
                print(f"Código Morse: {resultado}")
                input("\nPressione Enter para continuar...")

            elif escolha == '2':
                morse = input("Digite o código Morse a ser traduzido para texto (use espaço entre as letras e '/' entre as palavras): ")
                resultado = codigo_morse_para_texto(morse)
                print(f"Texto: {resultado}")
                input("\nPressione Enter para continuar...")

            elif escolha == 'sair':
                iniciar = False
                break
            else:
                print("Opção inválida, tente novamente.")
                input("\nPressione Enter para continuar...")

    elif exit_or_start == 'sair':
        iniciar = False
        break

    else: 
        os.system('cls')
        print("Entrada inválida. Por favor, digite 'iniciar' para começar ou 'sair' para encerrar. \n")

print("Programa encerrado.")



#Tradutor de codigo morse

import os

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

#funcao para traducao de Morse para Texto
def texto_para_codigo_morse(texto):
    morse = ""
    for char in texto.lower():
        if char in texto_para_morse:
            morse += texto_para_morse[char] + " "
        else:
            morse += "? "  # Simbolo para caracteres não reconhecidos
    return morse.strip()

#funcao para traducao de Texto para Morse
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

#-------------------------------------------------------------------------------------------------------------------------------------

loop_tela_inicial = True
loop_escolha_conversao = False
start_convert_1 = False
start_convert_2 = False

while loop_tela_inicial == True: #Tela Inicial com escolha de iniciar ou encerrar o programa
    os.system('cls')
    print("""\n\n ----------------------- TRADUTOR DE CODIGO MORSE -----------------------\n
        Com esse sistema voce poderá traduzir palavras para o Codigo morse e tambem o inverso,
        Para continuar digite "INICIAR" ou se desejar sair do sistema digite "ENCERRAR" \n""")

    exit_or_start = input("Digite: ").strip().lower()
           
    if exit_or_start == 'iniciar':
        loop_escolha_conversao = True
    
    
    elif exit_or_start == 'encerrar':
        print("\nObrigado por usar nosso programa!")
        break
        
           
    else: 
        print("\nEntrada inválida! Por favor insira uma das opções apresentadas.\n")
        input("Digite ENTER para continuar...")

    while loop_escolha_conversao == True: # Tela de escolha do tipo da conversao
        os.system('cls')
        print("""\nQual o tipo de tradução que deseja realizar?
            
        1 - MORSE / PORTUGUES
        2 - PORTUGUES / MORSE""")
        
        choice_convert = input("\nDigite o numero da opção desejada: ")

        if choice_convert == '1':
            start_convert_1 = True
            break
            
        elif choice_convert == '2':    
            start_convert_2 = True            
            break
        
        else:
            print("\nEntrada inválida! Por favor insira uma das opções apresentadas.")
            input("\nDigite ENTER para continuar...")
        
        while start_convert_1 == True:
            os.system('cls')
            texto = input("Insira o Codigo Morese para a tradução: ").strip().lower()
            resultado = texto_para_codigo_morse(texto)
            print(f"Código Morse: {resultado}")
            input("\nPressione Enter para continuar...")

            while True:
                os.system('cls')
                back_or_not = input("""Deseja realizar esta função novamente?
                            \nOpções: (SIM/NAO/ENCERRAR/INICIO)
                            \n Digite a opção desejada: """).strip().lower()

                if back_or_not == 'sim':
                    break
                
                elif back_or_not == 'nao':
                    start_convert_1 = False
                    break

                elif back_or_not == 'encerrar':
                    start_convert_1 = False
                    loop_escolha_conversao = False
                    loop_tela_inicial = False
                    print("\nObrigado por usar nosso programa!")
                    break
                
                elif back_or_not == 'inicio':
                    start_convert_1 = False
                    loop_escolha_conversao = False
                    break
                
                else: 
                    print("\nEntrada inválida! Por favor insira uma das opções apresentadas.\n")
                    input("\nDigite ENTER para continuar...")

        

        while start_convert_2 == True:
            os.system('cls')
            morse = input("Insira o Texto para a tradução (use espaço entre as letras e '/' entre as palavras): ").strip().lower()
            resultado = codigo_morse_para_texto(morse)
            print(f"Texto: {resultado}")
            input("\nPressione Enter para continuar...")

            while True:
                back_or_not = input("""\nDeseja realizar esta função novamente?
                            \nOpções: (SIM/NAO/ENCERRAR/INICIO)
                            \n Digite a opção desejada: """).strip().lower()

                if back_or_not == 'sim':
                    break
                
                elif back_or_not == 'nao':
                    start_convert_2 = False
                    break

                elif back_or_not == 'encerrar':
                    start_convert_2 = False
                    loop_escolha_conversao = False
                    loop_tela_inicial = False
                    print("\nObrigado por usar nosso programa!")
                    break
                
                elif back_or_not == 'inicio':
                    start_convert_2 = False
                    loop_escolha_conversao = False
                    break
                
                else: 
                    print("\nEntrada inválida! Por favor insira uma das opções apresentadas.\n")
                    input("\nDigite ENTER para continuar...")
            


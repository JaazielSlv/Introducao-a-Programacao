#Esse codigo foi feito por mim quando estava aprendendo a Introdução a programação não tinha conhecimentto de class e Orientação de objetos. 
#E tambem pouco conhecimentos em funções. 

import os 
import random
dispositivo = "power_on"
while dispositivo != "power_off":
    print("<< MENU >>")
    print()
    print("[1] CALCULADORA", "[2] JOGOS", "[0] DESLIGAR", sep="\n")
    menu = input("ESCOLHA UMA OPÇÂO: ")
    os.system("cls")
    if menu == "1":
        while True:
            print()
            print("QUAL TIPO DE CALCULADORA DESEJA USAR?", "[1] BASICA", "[2] AVANÇADA", "[0] VOLTAR", sep="\n")
            menu2 = input("ESCOLHA UMA OPÇÂO: ")
            os.system("cls")
            if menu2 == "1":
                    while True:
                        print()
                        print("QUAL TIPO DE CALCULO DESEJA EXECUTAR?", "[1] SOMA", "[2] SUBTRAÇÂO", "[3] DIVISÂO", "[4] MULTIPLICAÇÂO", "[0] VOLTAR", sep="\n")
                        menu3 = input("ESCOLHA UMA OPÇÂO: ")
                        os.system("cls")
                        if menu3 == "1":
                            while True:
                                print()
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA SOMAR? "))
                                if quantidade > 0:
                                    numeros = [0]*quantidade
                                    for i in range(quantidade):
                                        print()
                                        print("DGIGITE O {} NUMERO DA SOMA:".format((i+1)), end=" ")
                                        numeros[i] = float(input())
                                    calculo = 0
                                    for i in range(quantidade):
                                        calculo += numeros[i]
                                        os.system("cls")
                                    print()
                                    print("O RESULTADO DA SOMA É: {}".format(calculo))
                                    print()
                                    print("Deseja Somar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                    option = input("ESCOLHA UMA OPÇÂO: ")
                                    if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                    else:
                                        os.system("cls")
                                        print("OPÇÂO INVALIDA!")
                                        print()
                                else:
                                     os.system("cls")
                                     print("DIGITE UM NUMERO A CIMA DE 0")
                                     print()
                        elif menu3 == "2":
                            while True:
                                print()
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA SUBTRAIR? "))
                                if quantidade > 0:
                                    numeros = [0]*quantidade
                                    for i in range(quantidade):
                                        print("DGIGITE O {} NUMERO DA SUBTRAÇÂO:".format((i+1)), end=" ")
                                        numeros[i] = float(input())
                                    calculo = numeros[0]
                                    for i in range(1, quantidade):
                                        calculo -= numeros[i]
                                        os.system("cls")
                                    print()
                                    print("O RESULTADO DA SUBTRAÇÂO É: {}".format(calculo))
                                    print()
                                    print("Deseja Subitrair novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                    option = input("ESCOLHA UMA OPÇÂO: ")
                                    if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                    else:
                                        os.system("cls")
                                        print("OPÇÂO INVALIDA!")
                                        print()
                                else:
                                     os.system("cls")
                                     print()
                                     print("DIGITE UM NUMERO A CIMA DE 0")
                                     print()    
                        elif menu3 == "3":
                            while True:
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA DIVIDIR? "))
                                if quantidade > 0:
                                    numeros = [0]*quantidade
                                    for i in range(quantidade):
                                        print()
                                        print("DGIGITE O {} NUMERO DA DIVISÂO:".format((i+1)), end=" ")
                                        numeros[i] = float(input())
                                    calculo = numeros[0]
                                    for i in range(1, quantidade):
                                        calculo = calculo / numeros[i]
                                        os.system("cls")
                                    print()
                                    print("O RESULTADO DA DIVISÂO É: {}".format(calculo))
                                    print()
                                    print("Deseja Dividir novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                    option = input("ESCOLHA UMA OPÇÂO: ")
                                    if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                    else:
                                        os.system("cls")
                                        print("OPÇÂO INVALIDA!")
                                        print()
                                else:
                                     os.system("cls")
                                     print()
                                     print("DIGITE UM NUMERO A CIMA DE 0")
                                     print() 
                        elif menu3 == "4":
                            while True:
                                print()
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA MULTIPLICAR? "))
                                if quantidade > 0:
                                    numeros = [0]*quantidade
                                    for i in range(quantidade):
                                        print("DGIGITE O {} NUMERO DA MULTIPLICAÇÂO:".format((i+1)), end=" ")
                                        numeros[i] = float(input())
                                    calculo = numeros[0]
                                    for i in range(1, quantidade):
                                        calculo = calculo * numeros[i]
                                        os.system("cls")
                                    print("O RESULTADO DA MULTIPLICAÇÂO É: {}".format(calculo))
                                    print()
                                    print("Deseja Multiplicar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                    option = input("ESCOLHA UMA OPÇÂO: ")
                                    if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                    else:
                                        os.system("cls")
                                        print("OPÇÂO INVALIDA!")
                                        print()
                                else:
                                     os.system("cls")
                                     print("DIGITE UM NUMERO A CIMA DE 0")
                                     print() 
                        elif menu3 == "0":
                            os.system("cls")  
                            break
                        else:
                            os.system("cls")
                            print("OPÇÂO INVALIDA!")
                            print()
            elif menu2 == "2":
                 while True:
                        print("QUAL TIPO DE CALCULO DESEJA EXECUTAR?", "[1] MEDIA", "[2] AREA DE UM CIRCULO", "[3] PERIMETRO DE UM TRIANGULO", "[4] SABER O TIPO DE UM TRIANGULO", "[0] VOLTAR", sep="\n")
                        menu3 = input("ESCOLHA UMA OPÇÂO: ")
                        if menu3 == "1":
                            os.system("cls")
                            while True:
                                quantidade = int(input("DE QUANTOS NUMEROS VOCE DESEJA SABER A MEDIA? "))
                                if quantidade > 0:
                                    numeros = [0]*quantidade
                                    for i in range(quantidade):
                                        print("DGIGITE O {} NUMERO:".format((i+1)), end=" ")
                                        numeros[i] = float(input())
                                    calculo = 0
                                    for i in range(quantidade):
                                        calculo += numeros[i]
                                        os.system("cls")
                                    media = calculo / quantidade
                                    print("O RESULTADO DA MEDIA É: {}".format(media))
                                    print()
                                    print("Deseja Calcular novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                    option = input("ESCOLHA UMA OPÇÂO: ")
                                    if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                    else:
                                        os.system("cls")
                                        print("OPÇÂO INVALIDA!")
                                        print()
                                else:
                                     os.system("cls")
                                     print("DIGITE UM NUMERO A CIMA DE 0")
                                     print()           
                        elif menu3 == "2":
                            os.system("cls")
                            while True:
                                r = float(input("INFORME O RAIO: "))
                                n = 3.14
                                a = n * (r ** 2)
                                print("A AREA DO CIRCULO È: {:.1f}".format(a))
                                print()
                                print("Deseja Calcular novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                option = input("ESCOLHA UMA OPÇÂO: ")
                                if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                else:
                                    os.system("cls")
                                    print("OPÇÂO INVALIDA!")
                                    print()
                        elif menu3 == "3":
                            while True:
                                os.system("cls")
                                print("PARA SABER O PERIMETRO DE UM TRIANGULO É NECESSARIO INFORMAR 3 VALORES")
                                print("'Lembrando que um de seus lados deve ser maior que o valor absoluto da diferença dos outros dois lados e menor que a soma dos outros dois lados'")
                                a = float(input("INFORME O 1° VALOR: "))
                                b = float(input("INFORME O 2° VALOR: "))
                                c = float(input("INFORME O 3° VALOR: "))
                                os.system("cls")
                                if (a < (b + c) and b < (a + c) and c < (a + b)):
                                    print("PERIMETRO = {:.1f}".format(a+b+c))
                                else:
                                    print("ESSES VALORES NÂO FORMA UM TRIANGULO")
                                print()
                                print("Deseja Calcular novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                option = input("ESCOLHA UMA OPÇÂO: ")
                                if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                else:
                                    os.system("cls")
                                    print("OPÇÂO INVALIDA!")
                                    print()

                        elif menu3 == "4":
                            os.system("cls")
                            while True:
                                print("PARA SABER O TIPO DE UM TRIANGULO É NECESSARIO INFORMAR 3 VALORES")
                                a = float(input("INFORME O 1° VALOR: "))
                                b = float(input("INFORME O 2° VALOR: "))
                                c = float(input("INFORME O 3° VALOR: "))
                                os.system("cls")
                                if (a > b) and (a > c):
                                    if (b > c):
                                        a, b, c = a, b, c
                                    else:
                                        a, b, c = a, c, b
                                elif (b > c):
                                    if (a > c):
                                        a, b, c = b, a, c
                                    else:
                                        a, b, c = b, c, a
                                else:
                                    if (a > b):
                                        a, b, c = c, a, b
                                    else:
                                        a, b, c = c, b, a
                                if (a >= b + c):
                                    print('NAO FORMA TRIANGULO')
                                else:
                                    if (a ** 2 == b ** 2 + c ** 2):
                                        print('TRIANGULO RETANGULO')
                                    elif (a ** 2 > b ** 2 + c ** 2):
                                        print('TRIANGULO OBTUSANGULO')
                                    else:
                                        print('TRIANGULO ACUTANGULO')
                                    if (a == b) and (a == c):
                                        print('TRIANGULO EQUILATERO')
                                    elif (a == b) or (a == c) or (b == c):
                                        print('TRIANGULO ISOSCELES')
                                    print()
                                    print("Deseja Calcular novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                    option = input("ESCOLHA UMA OPÇÂO: ")
                                    if option == "2" or option == "não":
                                        os.system("cls")
                                        break
                                    else:
                                        os.system("cls")
                                        print("OPÇÂO INVALIDA!")
                                        print()
                        elif menu3 == "0":
                             os.system("cls")
                             break
                        else:
                             os.system("cls")
                             print("OPÇÂO INVALIDA!")
                             print()
            elif menu2 == "0":
                    break
            else:
                print("OPÇÂO INVALIDA!")
                print()
    if menu == "2":
        while True:
            print("QUAL JOGO DESEJA JOGAR?", "[1] ADIVINHE O NUMERO", "[2] TABUADA", "[3] JOGO DA VELHA", "[0] VOLTAR", sep="\n")
            menu2 = input("ESCOLHA UMA OPÇÂO: ")
            os.system("cls")
            if menu2 == "1":
                while True:
                    print("<< ADIVINHE O NUMERO >>", "EM QUAL DIFICULDADE DESEJA JOGAR?", "[1] FACIL (1 - 25)", "[2] MEDIO (1 - 50)", "[3] DIFICIL (1 - 100)" , "[0] VOLTAR", sep="\n")
                    menu3 = input("ESCOLHA UMA OPÇÂO: ")
                    os.system("cls")
                    if menu3 == "1":
                        while True:
                            numeros = random.randint(1, 25)
                            for i in range(5, -1, -1):
                                if i == 0:
                                    os.system("cls")
                                    print("SUAS TENTAIVAS ACABARAM")
                                    print("A RESPOSTA CERTA ERA", numeros)
                                    break
                                print("Você possui {} Tentativas".format(i))
                                print()
                                resposta = int(input("DIGITE UM NUMERO: "))
                                if resposta == numeros:
                                    os.system("cls")
                                    print("PARABENS  ACERTOU ", numeros)
                                    print()
                                    break
                                elif resposta > numeros:
                                    os.system("cls")
                                    print(resposta, "É MAIOR QUE O NUMERO")
                                    print()
                                elif resposta < numeros:
                                    os.system("cls")
                                    print(resposta, "É MENOR QUE O NUMERO")
                                    print()
                            print()
                            print("Deseja jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break
                    elif menu3 == "2":
                        while True:
                            numeros = random.randint(1, 50)
                            for i in range(6, -1, -1):
                                if i == 0:
                                    os.system("cls")
                                    print("SUAS TENTAIVAS ACABARAM")
                                    print("A RESPOSTA CERTA ERA", numeros)
                                    break
                                print(" possui {} Tentativas".format(i))
                                print()
                                resposta = int(input("DIGITE UM NUMERO: "))
                                if resposta == numeros:
                                    os.system("cls")
                                    print("PARABENS VOCÊ ACERTOU ", numeros)
                                    print()
                                    break
                                elif resposta > numeros:
                                    os.system("cls")
                                    print(resposta, "É MAIOR QUE O NUMERO")
                                    print()
                                elif resposta < numeros:
                                    os.system("cls")
                                    print(resposta, "É MENOR QUE O NUMERO")
                                    print()
                            print()
                            print("Deseja jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break
                    elif menu3 == "3":
                        while True:
                            numeros = random.randint(1, 100)
                            for i in range(7, -1, -1):
                                if i == 0:
                                    os.system("cls")
                                    print("SUAS TENTAIVAS ACABARAM")
                                    print("A RESPOSTA CERTA ERA", numeros)
                                    break
                                print("Você possui {} Tentativas".format(i))
                                print()
                                resposta = int(input("DIGITE UM NUMERO: "))
                                if resposta == numeros:
                                    os.system("cls")
                                    print("PARABENS VOCÊ ACERTOU ", numeros)
                                    print()
                                    break
                                elif resposta > numeros:
                                    os.system("cls")
                                    print(resposta, "É MAIOR QUE O NUMERO")
                                    print()
                                elif resposta < numeros:
                                    os.system("cls")
                                    print(resposta, "É MENOR QUE O NUMERO")
                                    print()
                            print()
                            print("Deseja jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break
                    elif menu3 == "0":
                        os.system("cls")
                        break
            elif menu2 == "2":
                while True:
                    print("<< TABUADA >>", "EM QUAL DIFICULDADE DESEJA JOGAR?", "[1] FACIL (SOMA)", "[2] MEDIO (SUBTRAÇÃO)", "[3] DIFICIL (MULTIPLICAÇÃO)" , "[0] VOLTAR", sep="\n")
                    menu3 = input("ESCOLHA UMA OPÇÂO: ")
                    os.system("cls")
                    if menu3 == "1":
                        while True:
                            acertos = 0
                            for i in range(1, 7):
                                if i == 6:
                                    print("PARABENS VOCÊ VENCEU!")
                                    print()
                                    break
                                numero1 = random.randint(25, 99)
                                numero2 = random.randint(25, 99)
                                numeros = numero1 + numero2
                                print("JOGADAS", i, "/ 5")
                                print()
                                print(numero1, "+", numero2, "= ", end="")
                                resposta = int(input())
                                os.system("cls")
                                if resposta != numeros:
                                    print("VOCÊ ERROU A RESPOSTA CERTA É: ", numeros)
                                    print()
                                    break
                            print("Deseja jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break
                    elif menu3 == "2":
                        while True:
                            acertos = 0
                            for i in range(1, 7):
                                if i == 6:
                                    print("PARABENS VOCÊ VENCEU!")
                                    print()
                                    break
                                numero1 = random.randint(25, 99)
                                numero2 = random.randint(25, 99)
                                numeros = numero1 - numero2
                                print("JOGADAS", i, "/ 5")
                                print()
                                print(numero1, "-", numero2, "= ", end="")
                                resposta = float(input())
                                os.system("cls")
                                if resposta != numeros:
                                    print("VOCÊ ERROU A RESPOSTA CERTA É: ", numeros)
                                    print()
                                    break
                            print("Deseja jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break
                    elif menu3 == "3":
                        while True:
                            acertos = 0
                            for i in range(1, 7):
                                if i == 6:
                                    print("PARABENS VOCÊ VENCEU!")
                                    print()
                                    break
                                numero1 = random.randint(25, 99)
                                numero2 = random.randint(25, 99)
                                numeros = numero1 * numero2
                                print("JOGADAS", i, "/ 5")
                                print()
                                print(numero1, "*", numero2, "= ", end="")
                                resposta = int(input())
                                os.system("cls")
                                if resposta != numeros:
                                    print("VOCÊ ERROU A RESPOSTA CERTA É: ", numeros)
                                    print()
                                    break
                            print("Deseja jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break
                    elif menu3 == "0":
                        os.system("cls")
                        break
                    else:
                            os.system("cls")
                            print("OPÇÂO INVALIDA!")
                            print()
            elif menu2 == "3":
                while True:
                    print("<< JOGO DA VELHA >>", "PARA JOGAR ESSE JOGO É NECESSARIO 2 JOGADORES", sep="\n")
                    print()
                    print("DESEJA PROSSEGUIR?", "[1] SIM", "[2] NÂO", sep="\n")
                    print()
                    option = input("ESCOLHA UMA OPÇÂO: ")
                    if option == "1":
                        os.system("cls")
                        while True:
                            ta = [[" "," "," "],[" "," "," "],[" "," "," "]]
                            for i in range(5):
                                print("<< JOGO DA VELHA >>")
                                print()
                                print("    ", " 0 ", " 1 ", " 2 ")
                                print()
                                print(" 0 ", end="   ")
                                print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                print("     -----------")
                                print(" 1 ", end="   ")
                                print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                print("     -----------")
                                print(" 2 ", end="   ")
                                print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                
                                print()
                                print("JOGADOR 1 = X")
                                while True:
                                    while True:
                                        linha = int(input("ESCOLHA A LINHA: "))
                                        if linha == 0 or linha == 1 or linha == 2:
                                            break
                                        else:
                                            print("LINHA INVALIDA ESCOLHA ENTRE 0 E 2")
                                    while True:
                                        coluna = int(input("ESCOLHA A COLUNA: "))
                                        if coluna == 0 or coluna == 1 or coluna == 2:
                                            break
                                        else:
                                            print("COLUNA INVALIDA INVALIDA ESCOLHA ENTRE 0 E 2")
                                    if ta[linha][coluna] == "X" or ta[linha][coluna] == "O":
                                        print("LOCAL JA ESCOLHIDO!")
                                        print("ESCOLHA NOVAMENTE")
                                    else:
                                        ta[linha][coluna] = "X"
                                        break 
                                    
                                os.system("cls")
                                if ta[0][0] == "X" and ta[0][1] == "X" and ta[0][2] == "X" or ta[1][0] == "X" and ta[1][1] == "X" and ta[1][2] == "X" or ta[2][0] == "X" and ta[2][1] == "X" and ta[2][2] == "X":
                                    os.system("cls")
                                    print("JOGADOR 1 GANHOU!!")
                                    print()
                                    print("    ", " 0 ", " 1 ", " 2 ")
                                    print()
                                    print(" 0 ", end="   ")
                                    print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                    print("     -----------")
                                    print(" 1 ", end="   ")
                                    print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                    print("     -----------")
                                    print(" 2 ", end="   ")
                                    print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                    break
                                elif ta[0][0] == "X" and ta[1][0] == "X" and ta[2][0] == "X" or ta[0][1] == "X" and ta[1][1] == "X" and ta[2][1] == "X" or ta[0][2] == "X" and ta[1][2] == "X" and ta[2][2] == "X":
                                    os.system("cls")
                                    print("JOGADOR 1 GANHOU!!")
                                    print()
                                    print("    ", " 0 ", " 1 ", " 2 ")
                                    print()
                                    print(" 0 ", end="   ")
                                    print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                    print("     -----------")
                                    print(" 1 ", end="   ")
                                    print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                    print("     -----------")
                                    print(" 2 ", end="   ")
                                    print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                    break
                                elif ta[0][0] == "X" and ta[1][1] == "X" and ta[2][2] =="X" or ta[0][2] == "X" and ta[1][1] == "X" and ta[2][0] == "X":
                                    os.system("cls")
                                    print("JOGADOR 1 GANHOU!!")
                                    print()
                                    print("    ", " 0 ", " 1 ", " 2 ")
                                    print()
                                    print(" 0 ", end="   ")
                                    print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                    print("     -----------")
                                    print(" 1 ", end="   ")
                                    print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                    print("     -----------")
                                    print(" 2 ", end="   ")
                                    print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                    break
                                print("<< JOGO DA VELHA >>")
                                print()
                                print("    ", " 0 ", " 1 ", " 2 ")
                                print()
                                print(" 0 ", end="   ")
                                print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                print("     -----------")
                                print(" 1 ", end="   ")
                                print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                print("     -----------")
                                print(" 2 ", end="   ")
                                print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                if i == 4:
                                    print()
                                    print("EMPATE")
                                    break
                                print()
                                print("JOGADOR 2 = O")
                                while True:
                                    while True:
                                        linha = int(input("ESCOLHA A LINHA: "))
                                        if linha == 0 or linha == 1 or linha == 2:
                                            break
                                        else:
                                            print("LINHA INVALIDA ESCOLHA ENTRE 0 E 2")
                                    while True:
                                        coluna = int(input("ESCOLHA A COLUNA: "))
                                        if coluna == 0 or coluna == 1 or coluna == 2:
                                            break
                                        else:
                                            print("COLUNA INVALIDA INVALIDA ESCOLHA ENTRE 0 E 2")
                                    if ta[linha][coluna] == "X" or ta[linha][coluna] == "O":
                                        print("LOCAL JA ESCOLHIDO!")
                                        print("ESCOLHA NOVAMENTE")
                                    else:
                                        ta[linha][coluna] = "O"
                                        break
                                           
                                os.system("cls")
                                if ta[0][0] == "O" and ta[0][1] == "O" and ta[0][2] == "O" or ta[1][0] == "O" and ta[1][1] == "O" and ta[1][2] == "O" or ta[2][0] == "O" and ta[2][1] == "O" and ta[2][2] == "O":
                                    os.system("cls")
                                    print("JOGADOR 2 GANHOU!!")
                                    print()
                                    print("    ", " 0 ", " 1 ", " 2 ")
                                    print()
                                    print(" 0 ", end="   ")
                                    print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                    print("     -----------")
                                    print(" 1 ", end="   ")
                                    print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                    print("     -----------")
                                    print(" 2 ", end="   ")
                                    print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                    break
                                elif ta[0][0] == "O" and ta[1][0] == "O" and ta[2][0] == "O" or ta[0][1] == "O" and ta[1][1] == "O" and ta[2][1] == "O" or ta[0][2] == "O" and ta[1][2] == "O" and ta[2][2] == "O":
                                    os.system("cls")
                                    print("JOGADOR 2 GANHOU!!")
                                    print()
                                    print("    ", " 0 ", " 1 ", " 2 ")
                                    print()
                                    print(" 0 ", end="   ")
                                    print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                    print("     -----------")
                                    print(" 1 ", end="   ")
                                    print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                    print("     -----------")
                                    print(" 2 ", end="   ")
                                    print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                    break
                                elif ta[0][0] == "O" and ta[1][1] == "O" and ta[2][2] =="O" or ta[0][2] == "O" and ta[1][1] == "O" and ta[2][0] == "O":
                                    os.system("cls")
                                    print("JOGADOR 2 GANHOU!!")
                                    print()
                                    print("    ", " 0 ", " 1 ", " 2 ")
                                    print()
                                    print(" 0 ", end="   ")
                                    print(ta[0][0],ta[0][1],ta[0][2],sep=" | ")
                                    print("     -----------")
                                    print(" 1 ", end="   ")
                                    print(ta[1][0],ta[1][1],ta[1][2],sep=" | ")
                                    print("     -----------")
                                    print(" 2 ", end="   ")
                                    print(ta[2][0],ta[2][1],ta[2][2],sep=" | ")
                                    break
                            print()
                            print("Deseja jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break
                    elif option == "2":
                        os.system("cls")
                        break
            elif menu2 == "0":
                os.system("cls")
                break
            else:
                print("OPÇÂO INVALIDA!")
                print()
    if menu == "0":
            dispositivo = "power_off"
print("DISPOSITIVO DESLIGADO REINICIE O CODIGO PARA LIGAR")
print("Obrigado por testar!")



        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                    

import os 
import random
dispositivo = "power_on"
while dispositivo != "power_off":
    print("MENU","[2] CALCULADORA", "[3] JOGOS", "[0] DESLIGAR", sep="\n")
    menu = input("ESCOLHA UMA OPÇÂO: ")
    os.system("cls")
    if menu == "2":
        while True:
            print("QUAL TIPO DE CALCULADORA DESEJA USAR?", "[1] BASICA", "[2] AVANÇADA", "[0] VOLTAR", sep="\n")
            menu2 = input("ESCOLHA UMA OPÇÂO: ")
            os.system("cls")
            if menu2 == "1":
                    while True:
                        print("QUAL TIPO DE CALCULO DESEJA EXECUTAR?", "[1] SOMA", "[2] SUBTRAÇÂO", "[3] DIVISÂO", "[4] MULTIPLICAÇÂO", "[0] VOLTAR", sep="\n")
                        menu3 = input("ESCOLHA UMA OPÇÂO: ")
                        os.system("cls")
                        if menu3 == "1":
                            while True:
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA SOMAR? "))
                                if quantidade > 0:
                                    numeros = [0]*quantidade
                                    for i in range(quantidade):
                                        print("DGIGITE O {} NUMERO DA SOMA:".format((i+1)), end=" ")
                                        numeros[i] = float(input())
                                    calculo = 0
                                    for i in range(quantidade):
                                        calculo += numeros[i]
                                        os.system("cls")
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
                                     print("DIGITE UM NUMERO A CIMA DE 0")
                                     print()    
                        elif menu3 == "3":
                            while True:
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA DIVIDIR? "))
                                if quantidade > 0:
                                    numeros = [0]*quantidade
                                    for i in range(quantidade):
                                        print("DGIGITE O {} NUMERO DA DIVISÂO:".format((i+1)), end=" ")
                                        numeros[i] = float(input())
                                    calculo = numeros[0]
                                    for i in range(1, quantidade):
                                        calculo = calculo / numeros[i]
                                        os.system("cls")
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
                                     print("DIGITE UM NUMERO A CIMA DE 0")
                                     print() 
                        elif menu3 == "4":
                            while True:
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
    if menu == "3":
        while True:
            print("QUAL JOGO DESEJA JOGAR?", "[1] ADIVINHE O NUMERO", "[2] TABUADA", "[3] JOGO DA VELHA", "[0] VOLTAR", sep="\n")
            menu2 = input("ESCOLHA UMA OPÇÂO: ")
            os.system("cls")
            if menu2 == "1":
                while True:
                    print("<< ADIVINHE O NUMERO >>", "EM QUAL DIFICULDADE DESEJA JOGAR?", "[1] FACIL (1 - 25)", "[2] MEDIO (1 - 50)", "[3] DIFICIL (1 - 100)" , "[0] VOLTAR", sep="\n")
                    menu2 = input("ESCOLHA UMA OPÇÂO: ")
                    os.system("cls")
                    if menu2 == "1":
                        while True:
                            numeros = random.randint(1, 25)
                            for i in range(5, -1, -1):
                                if i == 0:
                                    os.system("cls")
                                    print("SUAS TENTAIVAS ACABARAM")
                                    print("A RESPOSTA CERTA ERA", numeros)
                                    break
                                print("Voçe possue {} Tentativas".format(i))
                                print()
                                resposta = int(input("DIGITE UM NUMERO: "))
                                if resposta == numeros:
                                    os.system("cls")
                                    print("PARABENS VOÇE ACERTOU ", numeros)
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
                            print("Deseja Jogar novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                            option = input("ESCOLHA UMA OPÇÂO: ")
                            if option == "1":
                                os.system("cls")
                            elif option == "2" or option == "não":
                                    os.system("cls")
                                    break





                    
    if menu == "0":
            dispositivo = "power_off"
print("DISPOSITIVO DESLIGADO REINICIE O CODIGO PARA LIGAR")



        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                    

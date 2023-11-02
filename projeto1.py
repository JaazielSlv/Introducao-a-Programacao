import os 
import random
dispositivo = "power_on"
while dispositivo != "power_off":
    print("MENU","[1] CALCULADORA", "[2] JOGOS", "[0] DESLIGAR", sep="\n")
    menu = input("ESCOLHA UMA OPÇÂO: ")
    os.system("cls")
    if menu == "1":
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
                                os.system("cls")
                        elif menu3 == "2":
                            while True:
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA SUBTRAIR? "))
                                numeros = [0]*quantidade
                                for i in range(quantidade):
                                    print("DGIGITE O {} NUMERO DA SUBTRAÇÂO:".format((i+1)), end=" ")
                                    numeros[i] = float(input())
                                calculo = 0
                                for i in range(quantidade):
                                    calculo -= numeros[i]
                                    os.system("cls")
                                print("O RESULTADO DA SUBTRAÇÂO É: {}".format(calculo))
                                print()
                                print("Deseja Subitrair novamente? ","[1] SIM", "[2] NÂO", sep="\n")
                                option = input("ESCOLHA UMA OPÇÂO: ")
                                if option == "2" or option == "não":
                                    os.system("cls")
                                    break
                                os.system("cls")    
                        elif menu3 == "3":
                            while True:
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA DIVIDIR? "))
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
                                os.system("cls")
                        elif menu3 == "4":
                            while True:
                                quantidade = int(input("QUANTOS NUMEROS VOCE DESEJA MULTIPLICAR? "))
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
                                os.system("cls")
                        elif menu3 == "0":
                            os.system("cls")  
                            break
                        else:
                            os.system("cls")
                            print("OPÇÂO INVALIDA!")
                            print()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            elif menu2 == "2":
                    os.system("cls")
                    print("NÂO PRONTO")
            elif menu2 == "0":
                    break
            else:
                print("OPÇÂO INVALIDA!")
                print()

                    
    if menu == "0":
            dispositivo = "power_off"
print("DISPOSITIVO DESLIGADO REINICIE O CODIGO PARA LIGAR")



        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                    
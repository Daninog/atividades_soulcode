try:
    numero1 = int(input("Digite um valor: "))
    numero2 = int(input("Digite um valor: "))
    numero3 = int(input("Digite um valor: "))
    numero4 = int(input("Digite um valor: "))

    if numero1 == 1 and numero2 == 2 and numero3 == 3 and numero4 == 4:
        print("Parabéns!!!")
    else:
        print("Não foi dessa vez que você acertou :(")



except Exception as e:
    print("Erro: ", str(e))
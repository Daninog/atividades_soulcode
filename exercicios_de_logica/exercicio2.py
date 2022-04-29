try:
    
    print("*****CADASTRO DE NOME*****")
    print("**PARA ENCERRAR DIGITE SAIR**")
    
    nomes = []

    while True:

        entrada_nomes = input("Digite o nome: ")

        if entrada_nomes == "sair" or entrada_nomes == "SAIR": 
            break
        else:
            nomes.append(entrada_nomes)                      

    print(nomes)

except Exception as e:
     print("Erro: ", str(e))
 

try:

    print("****PREENCHA A LISTA ABAIXO****")

    listagem = []
    

    while True:
        produto = input("Nome do produto: "), input("Descrição: "), float(input("Preço: ")), float(input("Quantidade em estoque: "))
        saida = input("Deseja sair? S/N: ")

        listagem.append(produto)  

        if saida.upper() == "S":
            break
    
    print(listagem)

except Exception as e:
    print("Erro: ", str(e))
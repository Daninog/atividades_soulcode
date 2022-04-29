try:
    
    base = float((input("Entre com a base: ")))
    expoente = float((input("Entre com o expoente: ")))
    
    resultado = base ** expoente
    print("O resultado da exponenciação é: ", resultado)
    

except Exception as e:
    print("Erro: ", str(e))


import datetime


try:
    # PRESSÃO DA TECLA
    aperto = input("Aperte qualquer tecla: ")
    tempo1 = datetime.datetime.now()
    

    #SOLTURA DA TECLA
    soltura = input("Aperte qualquer tecla: ")
    tempo2 = datetime.datetime.now()
     
    tempo = tempo2 - tempo1
    print("O tempo representativo de pressão foi de: ", tempo)

except Exception as e:
    print("Erro: ", e)
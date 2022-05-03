#Criando a classe
class vendedor:
    pass
    nome_vendedora = ""
    cliente = ""
    atendimento = ""
    venda = 0
    comissao = 0

    #Construtor da classe
    def __init__(self, nome_vendedora, cliente, venda):

        try:
            self.vendedora = nome_vendedora
            self.cliente = cliente
            self.venda = venda
        
        except Exception as e:
            print("Erro: ", str(e))

    #Definição dos métodos da classe
    def calc_comissao(self):
    
        try: 
            calculo = self.venda * 0.2
            return "Comissão dessa venda: " + "R$" + str(calculo)

        except Exception as e:
            print("Erro: ", str(e))
    
    def set_nome_vendedora(self, nome_vendedora):
            self.nome_vendedora = nome_vendedora
    
    def get_nome_vendedora(self):
        return self.nome_vendedora 

    def set_cliente(self, cliente):
            self.cliente = cliente
            
    def get_cliente(self):
        return self.cliente

    def set_atendimento(self, atendimento):
        self.atendimento = atendimento

    def get_atendimento(self):
        return self.atendimento

    def set_venda(self, venda):
        self.venda = venda

    def get_venda(self):
        return self.venda 

    def set_comissao(self, comissao):
        self.comissao = comissao

    def get_comissao(self):
        return self.comissao

    
#Inicializando o codigo
if __name__ == "__main__":

    try:

        #Instanciando a classe vendedor
        daniele = vendedor("Maria Bethânia", "Gal Costa", 100000) 

        #Chammando o metodo da classe definindo o nome da vendedora
        daniele.set_nome_vendedora("Maria Rita")

        #Chamando o metodo da classe que retorna o nome da vendedora
        print("Nome da vendedora: ", daniele.get_nome_vendedora())
        
        #Chammando o metodo da classe definindo a cliente
        daniele.set_cliente("Gal Costa")

        #Chamando o metodo da classe que retorna a cliente
        print("Cliente da venda: ", daniele.get_cliente())

        #Chamando um método da classe definindo a comissão da venda
        comissao = daniele.calc_comissao()
        print(comissao)

        #Chamando um metodo da classe vendedor definindo o atendimento
        daniele.set_atendimento("Deixe sua avaliação sobre o antendimento: Oxi essa vendedora é arretada demais!!!")

        #Chamando um metodo da classe que retorna como foi o atendimento
        print(daniele.get_atendimento())

    except Exception as e:
        print("Erro: ", str(e))

        

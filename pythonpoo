class Veiculo:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
    
    def buzina(self):
        return f"Este veículo faz um som genérico de buzina"
    
class Carro(Veiculo):
    def __init__(self, velocidade_maxima):
        super().__init__(velocidade_maxima)
        
    def buzina(self):
        return f"O Carro tem a buzina mais alta. A velocidade máxima é {self.velocidade_maxima} km/h."

class Moto(Veiculo):
    def __init__(self, velocidade_maxima):
        super().__init__(velocidade_maxima)
    
    def buzina(self):
        return f"A moto tem a buzina mais baixa e aguda. A velocidade máxima é {self.velocidade_maxima} km/h." 
    
veiculo = Veiculo(100)
carro = Carro(220) 
moto = Moto(112)   
        
print(veiculo.buzina())
print(carro.buzina())
print(moto.buzina())

            

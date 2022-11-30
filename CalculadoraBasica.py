class CalculadoraBasica():
    def __init__(self):
        self.resultado = 0
        self.valor1 = 0
        self.valor2 = 0
    
    def sumar(self):
        self.resultado = self.valor1 + self.valor2
    
    def restar(self):
        self.resultado = self.valor1 - self.valor2
    
    def multiplicar(self):
        self.resultado = self.valor1 * self.valor2
    
    def dividir(self):
        self.resultado = self.valor1 / self.valor2
    def Cuadrado(self):
        self.resultado = self.valor2**2 
    def MostrarResultado(self):
        return self.resultado
    
    
    
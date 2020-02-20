import math 
def area (raio):
    area = math.pi*(raio**2)
    return area 
def comprimento (raio):
    comprimento = 2* (math.pi*raio)
    return comprimento
raio = float(input ('Raio: '))
print (area (raio))
print (comprimento(raio))


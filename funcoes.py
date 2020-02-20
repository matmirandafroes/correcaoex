
valor1 =  float(input ('Digite o primeiro numero: '))
valor2 = float(input ('Digite o segundo numero: '))
def somar (valor1 , valor2):
    return valor1 + valor2 

resultado = somar(valor1, valor2)

if resultado > 40:
    print (resultado)
else:
    print('não retorno menores que 40')
    
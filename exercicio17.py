#Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula: F = C × 1.8 + 32

temperatura = int(input("digite a temperatura em graus celsios: "))
 
Fahrenheit = temperatura * 1.8 + 32

if Fahrenheit:
    print("sua temperatura em celsios é:" , Fahrenheit)
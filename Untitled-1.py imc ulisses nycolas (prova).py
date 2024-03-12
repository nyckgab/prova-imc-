def calcular_imc(peso, altura): 
    return peso / (altura*2)

def classificar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif 18.5 <= imc < 25:
        return "peso normal"
    elif 25 <= imc < 30: 
        return "sobrepeso"
    elif 30 <= imc < 35: 
        return "obessidade grau 1"
    elif 35 <= imc < 40:
        return "obessidade grau 2 (severa)"
    else:
        return "obessidade grau 3 (morbida)"
    

peso = float(input("digite seu peso em Kg:"))
altura = float(input("digite sua altura em metros"))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print("seu imc:", imc)
print("classificacao:", classificacao)

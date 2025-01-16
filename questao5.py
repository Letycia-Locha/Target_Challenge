def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida

texto = input("Digite a string a ser invertida: ")
resultado = inverter_string(texto)
print(f"String invertida: {resultado}")

import json

# Carregar os dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Filtrar valores válidos (dias com faturamento > 0)
valores = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Cálculos
menor_valor = min(valores)
maior_valor = max(valores)
media = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media)

# Resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
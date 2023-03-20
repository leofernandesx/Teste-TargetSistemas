import json

# Lendo o arquivo JSON com os dados do faturamento diário
with open('dados.json', 'r') as f:
    faturamento_diario = json.load(f)

# Calculando o menor valor de faturamento ocorrido em um dia do mês
menor_valor = min(faturamento_diario)

# Calculando o maior valor de faturamento ocorrido em um dia do mês
maior_valor = max(faturamento_diario)

# Calculando a média mensal do faturamento, excluindo os dias sem faturamento
media = sum([valor for valor in faturamento_diario if valor != 0]) / len(faturamento_diario)

# Calculando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum([1 for valor in faturamento_diario if valor > media])

# Imprimindo os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias acima da média: {dias_acima_da_media}")
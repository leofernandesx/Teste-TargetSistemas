# Define o faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o valor total mensal da distribuidora
total = sum(faturamento.values())

# Calcula e imprime o percentual de representação de cada estado
for estado, valor in faturamento.items():
    percentual = valor / total * 100
    print(f'{estado}: {percentual:.2f}%')
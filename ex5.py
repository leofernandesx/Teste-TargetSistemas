string = input("Digite uma string: ")  # entrada da string

string_invertida = ""  # variável para armazenar a string invertida

# percorre a string de trás para frente, adicionando cada caractere à variável "string_invertida"
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("A string invertida é:", string_invertida)  # exibe a string invertida na tela
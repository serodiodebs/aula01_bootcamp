# Variáveis à serem utilizadas
nome = input("Qual seu nome? ")
salario = float(input("Informe seu salário: "))
perc_bonus = float(input("Qual o seu percentual de bônus? "))

resultado = 1000 + (salario * perc_bonus)

# Minha versão - esqueci de usar o padrão Python: f
print("Olá " + nome + "!" + " o total que você receberá após o bônus é de: " + str(resultado))

print(f"Olá {nome}! o total que você receberá após o bônus é de: {resultado}")

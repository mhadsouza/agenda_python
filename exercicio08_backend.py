"""
Programa que realize a leitura de nome e salario, a cada iteração deverá perguntar ao usuário se ele deseja continuar. 
No final deverá apresentar o número de funcionários lidos e o somatório dos salários.
"""
numeroFuncionarios = 0
somaSalario = 0.0

while True:
    nome = str(input("Informe o nome:"))
    salario = float (input("Informe o salario:"))
    
    numeroFuncionarios = numeroFuncionarios + 1
    somaSalario = somaSalario + salario

    opcao = input("Deseja continuar (s/n)?")
    if opcao.lower() == 'n':
        break
print (f"O total de funcionários são: {numeroFuncionarios}, e o total dos salários são R$ {somaSalario:.2f}.")





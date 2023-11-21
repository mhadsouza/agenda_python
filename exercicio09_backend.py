"""
Lanchonete

Escrever um programa que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche.
A cada interação deve perguntar se o usuário deseja continuar, se a resposta for igual a 'n', o programa encerrará a execução.
No final, deverá ser apresentado o valor total.

Especificação     código   Preço
Cachorro quente    100      1,20
Bauru simples      101      1,30
Bauru com ovo      102      1,50
Hambúrguer         103      1,20 
Cheeseburguer      104      1,30
Refrigerante       105      1,00 
"""
valor = 0.0
while True:
 codigo = int(input("Informe o código do pedido: "))
 quantidade = int(input("Informe a quantidade: "))

 if codigo == 100:
    preco = 1.2
 elif codigo == 101:
    preco = 1.3
 elif codigo == 102:
    preco = 1.5
 elif codigo == 103:
    preco = 1.2 
 elif codigo == 104:
    preco = 1.3
 elif codigo == 105:
    preco = 1.0
 else:
    preco = 0
 print ("Código Inválido.")       

 valor = valor + (preco * quantidade)
    
 opcao = input("Deseja continuar (s/n)?")
 if opcao.lower() == 'n':
    break

print(f"O valor total a ser pago é: R$ {valor:.2f}.")
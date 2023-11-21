"""
Faça um programa que realiza o cadastro de contatos de uma agenda. 
Cada contato possui os seguintes atributos: nome telefone, e-mail.

Desenvolva funcionalidades que:

1 - Cadastre os registros
2 - Faça a pesquisa pelo nome
3 - Listar todos os registros 
4 - Altere o registro
5 - Excluir o registro

Faça um menu e a condição de saída é o outro usuário digitar 'n' e a cada ação do programa.
"""

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

agenda = []

def cadastrar_contato(nome, telefone, email):
    contato = Contato(nome, telefone, email)
    agenda.append(contato)

def pesquisar_contato(nome):
    for contato in agenda:
        if contato.nome == nome:
            return contato
    return None

def listar_contatos():
    for contato in agenda:
        print(f'Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}')

def alterar_contato(nome, novo_nome, novo_telefone, novo_email):
    contato = pesquisar_contato(nome)
    if contato:
        contato.nome = novo_nome
        contato.telefone = novo_telefone
        contato.email = novo_email

def excluir_contato(nome):
    contato = pesquisar_contato(nome)
    if contato:
        agenda.remove(contato)

while True:
    opcao = input("Digite 'n' para sair ou qualquer outra tecla para continuar: ")
    if opcao.lower() == 'n':
        break
    acao = input("Escolha uma opção (cadastrar, pesquisar, listar, alterar, excluir): ")
    if acao.lower() == 'cadastrar':
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        cadastrar_contato(nome, telefone, email)
    elif acao.lower() == 'pesquisar':
        nome = input("Digite o nome: ")
        contato = pesquisar_contato(nome)
        if contato:
            print(f'Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}')
        else:
            print("Contato não encontrado.")
    elif acao.lower() == 'listar':
        listar_contatos()
    elif acao.lower() == 'alterar':
        nome = input("Digite o nome do contato que deseja alterar: ")
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_email = input("Digite o novo email: ")
        alterar_contato(nome, novo_nome, novo_telefone, novo_email)
    elif acao.lower() == 'excluir':
        nome = input("Digite o nome do contato que deseja excluir: ")
        excluir_contato(nome)
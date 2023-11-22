from funcoes import incluir, pesquisar

def menu():
    print("1 - Cadastrar")
    print("2 - Pesquisar pelo nome")
    print("3 - Listar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("9 - Sair")
    
agenda = []

while True:
    menu()
    opcao = int(input('Informe a opcao:'))

    if opcao == 1:
        incluir (agenda)

    elif opcao == 2:
        nomeBusca = input('Informe o nome para busca: ')
        indice = pesquisar(agenda,nomeBusca)
        if indice != -1: 
            print(f"""{agenda[indice]['nome']} - {agenda[indice]['e-mail']} - {agenda[indice]['telefone']}""")
        else:
            print('Contato nao encontrado')        
    elif opcao == 3:
        for elemento in agenda:
            print(f"""{elemento['nome']}\t
                      {elemento['e-mail']}\t
                      {elemento['telefone']}""")


    elif opcao == 4:
        nomeBusca = input('Informe o nome para busca: ')
        posicao = -1
        for elemento in agenda:
            posicao = posicao+1
            if elemento ['nome'].lower() == nomeBusca.lower():
                break
        if posicao != -1:
            agenda[posicao]['nome'] = input('Informe o nome: ')
            agenda[posicao]['e-mail'] = input('Informe o e-mail: ')
            agenda[posicao]['telefone'] = input('Informe o telefone: ')        

    elif opcao == 5:
       nomeBusca = input('Informe o nome para busca: ')
       posicao = -1
       for elemento in agenda:
            posicao = posicao+1
            if elemento ['nome'].lower() == nomeBusca.lower():
                break

            if posicao != -1:
                agenda.pop(posicao)

    elif opcao == 9:
        break        
    else:
        print ("Opção Inválida.")
        
    # if opcao.lower() == 'n':
    #    break

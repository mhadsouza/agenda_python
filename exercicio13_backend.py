pessoa1 = {}

pessoa1 ['nome'] = "Renato"
pessoa1 ['e-mail'] = 'renato@teste.com'
pessoa1 ['telefone'] = '2020-1010'

pessoa2 = {}

pessoa2 ['nome'] = "Luis"
pessoa2 ['e-mail'] = 'luis@teste.com'
pessoa2 ['telefone'] = '9999-1010'

pessoa3 = {}

pessoa3 ['nome'] = input("Informe o nome:")
pessoa3 ['e-mail'] = input("Informe o e-mail:")
pessoa3 ['telefone'] = input("Informe o telefone:")


agenda = []

agenda.append (pessoa1)
agenda.append (pessoa2)
agenda.append (pessoa3)

for contato in agenda:
    print (contato['nome'])


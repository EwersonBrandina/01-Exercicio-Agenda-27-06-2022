from class_agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()
        while True:
            entrada=input(('1 - Novo Cadastro\n2 - Listar Contatos\n0 - Sair\n:'))
            if entrada == '1':
                agenda.salvar_contatos()
                pass
            elif entrada == '2':
                agenda.listar_contatos()
                pass
            elif entrada == '0':
                break
            else:
                print('Opção Invalida!!!')
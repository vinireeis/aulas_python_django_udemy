tasks = []
temp = []
while True:
    try:
        resp = int(input(
            "\nDigite o número referente a opção desejada\nAdicionar uma tarefa [1]\nListar tarefas [2]\nDesfazer última tarefa [3]\nRefazer última tarefa [4]\nSair [5]\n\n "))
        if resp in [1, 2, 3, 4, 5]:
            if resp == 1:
                tasks.append(input('\nEscreva a tarefa: '))
                temp.clear()
                temp.append(tasks[-1])
            elif resp == 2:
                if len(tasks) > 0:
                    print(f'\nEssas são as tarefas adicionadas {tasks}')
                else:
                    print('\nSua lista de tarefas está vazia')
            elif resp == 3:
                if len(tasks) <= 0:
                    print("\nnão há nada para remover")
                else:
                    temp = [tasks[-1]]
                    tasks.remove(tasks[-1])
            elif resp == 4:
                if len(temp) <= 0:
                    print('\nNão há nada para refazer')
                else:
                    tasks.append(temp[0])
            elif resp == 5:
                print(f'\nEssa é sua lista de tarefas {tasks}')
                print('\nFim do programa')
                break
    except ValueError:
        print('\nOPÇÃO INVALIDA\nTENTE NOVAMENTE\n')

def fala_oi():
    print('oi')


variavel = fala_oi
variavel()
print(type(variavel))  # transformou variavel em function

# exemplo


def master():
    def slave():
        print('OOII')
    return slave


variavel1 = master()  # colocando a funcao em uma variável
variavel1()  # fazendo a variável que é uma funcao master executar a slave


def master1(funcao):
    # criando uma funcao, que tem uma funcao slave e "manda a slave" executar uma terceira funcao "fala_oi"
    def slave1():
        funcao()
    return slave1


def fala_oi():
    print('Vai printar a fala_oi')


var = master1(fala_oi)
var()
# @master - decorador

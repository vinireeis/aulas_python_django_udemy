from pessoa import Pessoa

p1 = Pessoa('Vinicius', 27)
p1.comer('Melancia')  # começou a comer algum alimento
p1.comer('Melancia')  # informou que já está comendo
p1.parar_comer()  # fez parar de comer
p1.parar_comer()  # informou que já não está comendo nada
p1.comer('maça')  # começa a comer novamente
p1.falar('Futebol brasileiro')  # nao pode falar comendo
p1.parar_comer()  # parou de comer novamente
p1.falar('Futebol brasileiro')  # agora sim pode falar
p1.comer('uva')  # nao pode comer pois está falando
p2 = Pessoa('João', 32)
p2.comer('morango')  # cada objeto é independente

p1.get_ano_nascimento()
# esse é um atributo da classe, por isso n preciso instanciar
print(Pessoa.ano_atual)


# outra forma de criar uma pessoa pelo ano de nascimento
p3 = Pessoa.por_ano_nascimento('Cintia', 44)
#  e não pela idade ( como foi feito anteriormente)
print(p3.nome, p3.idade)
print()
print('-=' * 20)

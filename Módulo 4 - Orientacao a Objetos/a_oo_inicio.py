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

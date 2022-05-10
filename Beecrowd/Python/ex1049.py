def classificar_animal(a, b, c):
    if a == 'vertebrado' and b == 'ave' and c == 'carnivoro': return 'aguia'
    if a == 'vertebrado' and b == 'ave' and c == 'onivoro': return 'pomba'
    if a == 'vertebrado' and b == 'mamifero' and c == 'onivoro': return 'homem'
    if a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro': return 'vaca'
    if a == 'invertebrado' and b == 'inseto' and c == 'hematofago': return 'pulga'
    if a == 'invertebrado' and b == 'inseto' and c == 'herbivoro': return 'lagarta'
    if a == 'invertebrado' and b == 'anelideo' and c == 'hematofago': return 'sanguessuga'
    if a == 'invertebrado' and b == 'anelideo' and c == 'onivoro': return 'minhoca'


c1, c2, c3 = input(), input(), input()
print(classificar_animal(c1, c2, c3))

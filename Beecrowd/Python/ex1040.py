N1, N2, N3, N4 = [float(num) for num in input().split()]
media = (2*N1+3*N2+4*N3+N4)/10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame}')
    media = (media + exame) / 2
    if media >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media}')

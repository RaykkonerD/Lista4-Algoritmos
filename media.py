m1 = float(input())
m2 = float(input())
m3 = float(input())
media = (m1+m2+m3)/3

print(media)

if media >= 7.0:
  print("Aluno aprovado.")
elif media >= 4.0:
  print("Aluno deve fazer prova final.")
else:
  print("Aluno reprovado.")
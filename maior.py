n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= n2:
  if n3 > n1:
    print(n3)
  else:
    print(n1)
else:
  if n3 > n2:
    print(n3)
  else:
    print(n2)

'''
n1 = int(input())
n2 = int(input())
n3 = int(input())

print(max(n1, n2, n3))

# outro método

lista = list(map(lambda a: int(a), input().split()))
print(max(lista))
'''
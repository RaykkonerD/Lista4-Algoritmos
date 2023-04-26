a = int(input())

if a:
  b = int(input())
  c = int(input())
  delta = b**2 -4*a*c
  
  if delta < 0:
    print("A equação não tem raízes reais!")
  elif delta == 0:
    print(f"A equação possui uma única raiz: {-b/(2*a)}")
  else:
    print("A equação possui duas raízes:")
    print(f"x': {(-b+(delta**(1/2)))/(2*a)}")
    print(f"x'': {(-b-(delta**(1/2)))/(2*a)}")
      
else:
    print("O elemento A = 0. Impossível calcular as raízes. (Não tem raízes reais)")
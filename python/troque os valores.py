#troque os valores

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

print("Os valores são: A: |", a," B: |", b," C: |", c)

temp = a
a = b
b = c
c = temp

print("Os valores trocados são: A: |", a," B: |", b," C: |", c)

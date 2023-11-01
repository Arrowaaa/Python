#colete 3 numeros do usuario, e apos isso os ordenem em ordem CRESENTE.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print("Os números em ordem crescente são: ", a,"| ", b,"| ", c)

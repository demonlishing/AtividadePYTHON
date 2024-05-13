n = True
v1 = int(input("Digite o valor 1 inteiro: "))
v2 = int(input("Digite o valor 2 inteiro: "))
v3 = int(input("Digite o valor 3 inteiro: "))

if v1 != v2 and v1 != v3 and v2 != v3:
    n = False
else:
    print("Os valores devem ser diferentes")

if v1 < v2 and v1 < v3:
    ordem1 = v1
    if v2 < v3:
        ordem2 = v2
        ordem3 = v3
    else:
        ordem2 = v3
        ordem3 = v2
elif v2 < v1 and v2 < v3:
    ordem1 = v2
    if v1 < v3:
        ordem2 = v1
        ordem3 = v3
    else:
        ordem2 = v3
        ordem3 = v1
else:
    ordem1 = v3
    if v1 < v2:
        ordem2 = v1
        ordem3 = v2
    else:
        ordem2 = v2
        ordem3 = v1

print("Números em ordem crescente:", ordem1,"-", ordem2,"-", ordem3)

from random import randint
len_v     = int(input("Digite o tamanho do vetor: "))
var_v     = []
for i in range(len_v):
    var_v.append(randint(0, 9))
heel_size = int(input("Digite o tamanho do salto: "))
print(var_v)
i = 0
for _ in range(len_v // heel_size):
    for _ in range(heel_size):
        print(var_v[i], end = " ")
        i += 1
    print()
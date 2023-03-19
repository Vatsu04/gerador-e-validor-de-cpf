# EXEMPLO DE CPF VÁLIDO: 268.386.800-68
#
# 2     6     8     3     8     6     8     0     0
# 10    9     8     7     6     5     4     3     2
# ---------------------------------------------------
# 20    54    64    21    48    30    32    0     0   --> 269
#
# 11 - (269 % 11) = 6
#
#
# 2     6     8     3     8     6     8     0     0     6
# 11    10    9     8     7     6     5     4     3     2
# ---------------------------------------------------------
# 22    60    72    24    56    36    40    0     0     12   --> 322
#
# 11 - (322 % 11) = 8

#
# Se qualquer um dos dígitos for maior que 9, o mesmo se torna 0

from random import randint

cpf = ''
for a in range(9):
    cpf += str(randint (0,9))
print(cpf)
novo_cpf = cpf

soma = 0
rev = 10
for i in range(9):
    soma = soma + int(novo_cpf[i]) * rev
    rev -= 1
d1 = (11 - (soma % 11))
if d1 > 9:
    d1 = 0
novo_cpf += str(d1)
print(novo_cpf)

soma = 0
rev = 11
for i in range(10):
    soma = soma + int(novo_cpf[i]) * rev
    rev -= 1
d2 = 11 - (soma % 11)
if d2 > 9:
    d2 = 0
novo_cpf += str(d2)

print(novo_cpf)


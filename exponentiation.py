from itertools import product


def exponentiate(base_number, exponent):
  if exponent == 0:
    return 1
  else:
    return base_number * exponentiate(base_number, exponent-1)

print(exponentiate(2, 3))
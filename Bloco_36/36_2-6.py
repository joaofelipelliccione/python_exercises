"""
  Escreva um algoritmo recursivo para encontrar o máximo divisor comum (mdc)
  de dois inteiros.
"""


def mdc_recursive(int_a, int_b):
    if int_b == 0:
        return int_a
    else:
        return mdc_recursive(int_b, int_a % int_b)


print(mdc_recursive(20, 24))

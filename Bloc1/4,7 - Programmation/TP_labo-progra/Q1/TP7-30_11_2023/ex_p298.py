# Exercice 1
# Quel est le résultat attendu du code suivant ?
try:
    print(1 / 0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

# Exercice 2
# Quel est le résultat attendu du code suivant ?
try:
    print(1 / 0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")


# Exercice 3
# Quel est le résultat attendu du code suivant ?
def foo(x):
    assert x
    return 1 / x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")

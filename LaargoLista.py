def LargoLista(Secuencia):
    if isinstance(Secuencia,list):
        return LargoAux(Secuencia)
    else:
        return "Error"

def LargoAux(lista):
    if lista == [ ]:
        return 0
    else:
        return 1 + LargoAux(lista[1:])

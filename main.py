# j'ai tout d'abord creer mes fonctions (+ ; - ;* ; /) 
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro est impossible") # j'ai preciser que une divison par 0 est impossible
    return a / b

# dans ma calculatrice j'ai definit mes variables a , b et l'operation qui comporte les signes (+;-;*;/) 
def calculatrice(): 
    try:
        a = float(input("Entrez le premier nombre : "))
        operation = input("Entrez le type d'opération (+, -, *, /) : ")
        b = float(input("Entrez le deuxième nombre : "))

        if operation in {'*', '/'}:
            a = multiplication(a, b) if operation == '*' else division(a, b)
        elif operation in {'+', '-'}:
            a = addition(a, b) if operation == '+' else soustraction(a, b)
        else:
            raise ValueError("Opération non valide") # sa nous permet d'afficher s'il y a une erreur dans nos calcule

        print(f"Le résultat de {a} {operation} {b} est : {a}")

    except ValueError as e: # s'il y a une erreur in inattendue 
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
calculatrice()
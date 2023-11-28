def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro est impossible")
    return a / b

def afficher_historique(historique):
    print("Historique des opérations :")
    for operation in historique:
        print(operation)

def calculatrice():
    historique = []
    
    while True:
        try:
            user_input = input("Entrez le premier nombre (ou 'q' pour quitter) : ")
            
            if user_input.lower() == 'q':
                break
            
            a = float(user_input)
            
            operation = input("Entrez le type d'opération (+, -, *, /) : ")
            
            if operation not in {'+', '-', '*', '/'}:
                print("Opération non valide. Veuillez réessayer.")
                continue
            
            b = float(input("Entrez le deuxième nombre : "))

            if operation == '+':
                resultat = addition(a, b)
            elif operation == '-':
                resultat = soustraction(a, b)
            elif operation == '*':
                resultat = multiplication(a, b)
            elif operation == '/':
                resultat = division(a, b)
            
            historique.append(f"{a} {operation} {b} = {resultat}")
            print(f"Le résultat de {a} {operation} {b} est : {resultat}")

        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

    afficher_historique(historique)

calculatrice()
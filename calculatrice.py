import os


def add_historique(num1,operator,num2,result):
    hist_add = f"{num1} {operator} {num2} = {result}\n"
    with open('calc_history.txt', 'a') as file:
        file.write(hist_add)

def calculatrice(num1 , operator , num2):
    erreur = False
    if operator == "/" or operator == "%":
        if num2 == 0:
            print("On ne peut pas diviser par 0")
            erreur = True
    if type(num1) !=int and type(num1) != float:
        print("Le premier nombre n'est pas valide")
        erreur = True
    if type(num2) !=int and type(num2) != float:
        print("Le second nombre n'est pas valide")
        erreur = True
    if erreur == False:
        if operator == "+":
            result = num1 + num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
            add_historique(num1,operator,num2,result)
        elif operator == "-":
            result = num1 - num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
            add_historique(num1,operator,num2,result)
        elif operator == "*":
            result = num1 * num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
            add_historique(num1,operator,num2,result)
        elif operator == "/":
            result = num1 / num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
            add_historique(num1,operator,num2,result)
        elif operator == "%":
            result = num1 % num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
            add_historique(num1,operator,num2,result)
        else:
            print("L'operateur n'est pas valide")

def vide_historique():
    os.remove("calc_history.txt")
    
def view_historique():
    f = open("calc_history.txt", "r")
    print(f.read())

vide_historique()
calculatrice(10,"*",10)
calculatrice(25,"+",19)
calculatrice(25,"-",19)
calculatrice(46,"/",15)
view_historique()
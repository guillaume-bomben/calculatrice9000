def calculatrice(num1 , operator , num2):
    if operator == "/" or operator == "%" and num2 == 0 :
        print("On ne peut pas diviser par 0")
    elif type(num1) !=int and type(num1) != float:
        print("Le premier nombre n'est pas valide")
    elif type(num2) !=int and type(num2) != float:
        print("Le second nombre n'est pas valide")
    else:
        if operator == "+":
            result = num1 + num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
        elif operator == "/":
            result = num1 / num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
        elif operator == "%":
            result = num1 % num2
            print(f"La resultat de {num1} {operator} {num2} est {result}")
        else:
            print("L'operateur n'est pas valide")



calculatrice(10,"*",10)
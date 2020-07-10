print("\nDivision de 2 nombres\n")

Error = True
while Error:

    Number1 = input("Entre le 1er nombre : ")
    Number2 = input("Entre le 2ème nombre : ")

    try:
        Result = int(Number1) // int(Number2)
        print (f"\n{Number1} / {Number2} = {Result}\n")
        Error = False
    except ZeroDivisionError:
        print("\nErreur, je ne peux pas calculer une division par 0 !\n")
    except ValueError:
        print("\nErreur, tu dois saisir uniquement des nombres entiers !\n")

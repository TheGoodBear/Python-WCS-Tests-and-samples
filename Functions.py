Number = 13

def Increment(NewNumber, MinRange = 1, MaxRange = 2):
    for Value in range(MinRange, MaxRange):
        NewNumber = NewNumber + Value
        print("NewNumber = " + str(NewNumber))
        EvenOrOdd(NewNumber, "NewNumber")
    return NewNumber

def EvenOrOdd(NumberToCheck, VariableName = "Number"):
    if NumberToCheck % 2 == 0:
        print(VariableName + " est pair (" + str(NumberToCheck) + ")")
    else:
        print(VariableName + " est impair (" + str(NumberToCheck) + ")")
    print("Parité calculée")


print("Number = " + str(Number))

Number = Number + 5
SecondNumber = int(input("Entrez un nombre : "))
Number = Number + SecondNumber * 2
print("Number = " + str(Number))

Number = Increment(Number, MaxRange=5)

while Number > 10:
    Number = Number // 2
    EvenOrOdd(Number)

print("On continue")

Number = Increment(Number, 1, 10)

print("Terminé")
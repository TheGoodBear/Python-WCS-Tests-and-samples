a = 13
print("A = " + str(a))

a = a + 5
b = int(input("Entrez un nombre : "))
a = a + b * 2
print("A = " + str(a))

for c in range(1, 11):
    a = a + c
    print("A = " + str(a))

while a > 10:
    a = a // 2

    if a % 2 == 0:
        print("A est pair (" + str(a) + ")")
    else:
        print("A est impair (" + str(a) + ")")

print("Terminé")

print (15/7)
print (15//7)
print (19/7)
print (19//7)
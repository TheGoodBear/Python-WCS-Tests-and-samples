# coding: utf-8 

MyList = [
    "Chat",
    "Lapin",
    "Phacochère",
    "Mulot",
    "Thon"]

print()

# print list by item
for Element in MyList:
    print(Element)
print()

# print with string join
print(" ".join(MyList))
print()

# print with while and len
Counter = 0
while Counter < len(MyList):
    print(f"{Counter} - {MyList[Counter]}")
    Counter += 1
print()

# print with for and .index()
for Element in MyList:
    print(f"{MyList.index(Element)} - {Element}")
print()

# print with for and range
for Index in range(len(MyList)):
    print(f"{Index} - {MyList[Index]}")
print()

# print with for and enumerate
for Index, Element in enumerate(MyList):
    print(f"{Index} - {Element}")
print()

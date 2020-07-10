MyDict = {
    "Alex" : [27, 1992, "Balance/Scorpion"], 
    "Guillaume" : [32, 1988, "Vierge"],
    "Javier" : [45, 1974, "Cancer"] ,
    "Hadrien" : [25, 1995, "Verseau"], 
    "Laura" : [25, 1995, "Verseau"],
    "Alexandre" : [29, 1990, "Cancer"],
    "Wilfried" : [23, 1997, "Verseau"],
    "Aurélia" : [38, 1982, "Cancer"],
    "Mélanie" : [29, 1990, "Balance"],
    "Alain" : [53, 1967, "Poissons"]
    }

# for MyKey in MyDict.keys():
#     print(f"{MyKey}")
# print()

# for MyValue in MyDict.values():
#     print(f"{MyValue}")
# print()

for MyKey, MyValue in MyDict.items():
    if MyValue[2] == "Cancer":
        print(f"{MyKey} a {MyValue[0]} ans (né(e) en {MyValue[1]} du signe {MyValue[2]})")
print()

MyDict["Raoul"] = [None, None, None]

for MyKey, MyValue in MyDict.items():
    print(f"{MyKey} a {MyValue[0]} ans (né(e) en {MyValue[1]} du signe {MyValue[2]})")
print()

del MyDict["Alain"]

for MyKey, MyValue in MyDict.items():
    print(f"{MyKey} a {MyValue[0]} ans (né(e) en {MyValue[1]} du signe {MyValue[2]})")
print()


MyDict["Georges"] = MyDict.pop("Alexandre")

for MyKey, MyValue in MyDict.items():
    print(f"{MyKey} a {MyValue[0]} ans (né(e) en {MyValue[1]} du signe {MyValue[2]})")
print()

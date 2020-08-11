# coding: utf-8

# publicObject
# _privateObject_
# __protectedObject__

# imports
from Vehicle import Vehicle


# Variables
# List of vehicles
Vehicles = []


# functions
def Race(RaceLength):
    """
        Race on specified distance (km)
    """
    print()
    # Race !!!
    ThereIsAWinner = False
    print(f"Qui sera le premier sur une course de {RaceLength}km ?\n")
    for MyVehicle in Vehicles:
        MyVehicle.Position = 0
        MyVehicle.Start(Status = True, ShowMessage = False)
    while not ThereIsAWinner:   
        for MyVehicle in Vehicles:
            MyVehicle.Move(1/60, False)
            if MyVehicle.Position >= RaceLength * 1000:
                ThereIsAWinner = True
        if ThereIsAWinner:
            break
    # print race result
    for MyVehicle in Vehicles:
        if MyVehicle.Position >= RaceLength * 1000:
            print(f"{MyVehicle.Name} a GAGNÉ ({MyVehicle.GetPosition()}km de parcourus)")
        else:
            print(f"{MyVehicle.Name} a parcouru {MyVehicle.GetPosition()}km")
    print()

def Main():
    """
        Application start
    """

    print()

    # Create vehicle
    Vehicle1 = Vehicle()
    Vehicle1.Name = "Voiture d'Alex"
    Vehicle1.Color = "Bleu"
    Vehicle1.MaxSpeed = 150
    Vehicle1.TimeToStart = 10
    Vehicles.append(Vehicle1)
    print(f"Mon véhicule numéro 1 ({Vehicle1.Name}) est de couleur {Vehicle1.Color} et peux se déplacer à {Vehicle1.MaxSpeed}km/h")

    Vehicle2 = Vehicle()
    Vehicle2.Name = "Voiture de Laura"
    Vehicle2.Color = "Rose"
    Vehicle2.MaxSpeed = 200
    Vehicle2.TimeToStart = 10
    Vehicles.append(Vehicle2)
    print(f"Mon véhicule numéro 2 ({Vehicle2.Name}) est de couleur {Vehicle2.Color} et peux se déplacer à {Vehicle2.MaxSpeed}km/h")

    # create vehicles from list
    NewVehicles = [
        ("Voiture d'Hadrien", "Vert", 42, 10),
        ("Moto d'Alexandre", "Noire", 300, 15),
        ("Avion d'Aurélia", "Doré", 700, 60),
        ("Scooter de Guillaume", "Jaune fluo", 15, 0)
    ]
    for NewVehicle in NewVehicles:
        MyNewVehicle = Vehicle()
        MyNewVehicle.Name = NewVehicle[0]
        MyNewVehicle.Color = NewVehicle[1]
        MyNewVehicle.MaxSpeed = NewVehicle[2]
        MyNewVehicle.TimeToStart = NewVehicle[3]
        Vehicles.append(MyNewVehicle)

    # add new vehicles with constructor
    Vehicles.append(Vehicle("Moto de Mélanie", "Violette", 320, 15))
    Vehicles.append(Vehicle("Aéroglisseur de Wilfried", "Chrome", 120, 20))

    print()
    # print all vehicles
    for MyVehicle in Vehicles:
        print(f"Le véhicule {MyVehicle.Name} est de couleur {MyVehicle.Color} et peux se déplacer à {MyVehicle.MaxSpeed}km/h")

    print()
    # do actions with a vehicle
    TravelTime = 0.5
    V1Distance = Vehicle1.Move(TravelTime)
    if V1Distance != None:
        print(f"{Vehicle1.Name} se déplace de {V1Distance}km en {TravelTime} heures et se trouve maintenant à {Vehicle1.GetPosition()}km du point de départ.")
    else:
        print(f"{Vehicle1.Name} ne s'est pas déplacé.")
    Vehicle1.Start()
    TravelTime = 1
    V1Distance = Vehicle1.Move(TravelTime)
    if V1Distance != None:
        print(f"{Vehicle1.Name} se déplace de {V1Distance}km en {TravelTime} heures et se trouve maintenant à {Vehicle1.GetPosition()}km du point de départ.")
    else:
        print(f"{Vehicle1.Name} ne s'est pas déplacé.")
    TravelTime = 0.2
    V1Distance = Vehicle1.Move(TravelTime)
    if V1Distance != None:
        print(f"{Vehicle1.Name} se déplace de {V1Distance}km en {TravelTime} heures et se trouve maintenant à {Vehicle1.GetPosition()}km du point de départ.")
    else:
        print(f"{Vehicle1.Name} ne s'est pas déplacé.")
    Vehicle1.Start(False)
    Vehicle1.Position = 0

    # Race
    Race(2000)
    Race(10)
    Race(10000)


# Application entry
if __name__ == "__main__":
    Main()
# coding: utf-8

class Vehicle():
    """
        Generic class to manage vehicles
    """
    
    # Properties
    Name = ""
    Color = ""
    MaxSpeed = 0
    Position = 0        # in meters
    TimeToStart = 0     # in min
    TimeBeforeMoving = 0
    HasStarted = False


    # Methods
    def __init__(self, 
        Name = "", 
        Color = "", 
        MaxSpeed = 0, 
        TimeToStart = 0):
        """
            Vehicle constructor
        """
        self.Name = Name
        self.Color = Color
        self.MaxSpeed = MaxSpeed
        self.TimeToStart = TimeToStart  


    def GetPosition(self):
        """
            Get vehicle position in km
        """
        return self.Position / 1000


    def Start(self,
        Status = True,
        ShowMessage = True):
        """
            Start ot stop vehicle
        """
        self.HasStarted = Status
        if self.HasStarted:
            if ShowMessage:
                print(f"{self.Name} démarre.")
            self.TimeBeforeMoving = self.TimeToStart
        else:
            if ShowMessage:
                print(f"{self.Name} s'arrête.")


    def Move(self,
        TravelTime,
        ShowMessage = True):
        """
            Do move action on current vehicle (instance)

            Move during a specified time (in hour)
        """
        if ShowMessage:
            print(f"{self.Name} veut se déplacer durant {TravelTime} heures.")

        if self.HasStarted:
            if self.TimeToStart <= 0: 
                # calculate traveled distance
                Distance = round(self.MaxSpeed * TravelTime, 2)
                # give new position
                self.Position += Distance * 1000
                # return travel time
                return Distance
            else:
                self.TimeToStart -= TravelTime
        else:
            print(f"{self.Name} doit d'abord démarrer.")
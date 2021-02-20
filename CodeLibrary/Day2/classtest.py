#As python is not exclusively Object-orientated, classes do not need
# to be in separate files. A single pythong file is called a module and
# shouldbe named in all lowercase letters (whoops).

class Car:
    #the first parameter in a method will always refer to the current 
    #  instance of the class, or rather, the class itself.
    #  If you try to call manufacturer before self, self will be named
    #  'manufacturer' and you will probably mess up the rest of the parameters.

    #__init__ acts as a constructor in OOP
    def __init__(self, manufacturer, rNum, colour, owner):
        self.manufacturer = manufacturer
        self.rNum = rNum
        self.colour = colour
        self.owner = owner

    #Getters
    def getManufacturer(self):
        return self.manufacturer
    
    def getRNum(self):
        return self.rNum
    
    def getColour(self):
        return self.colour

    def getOwner(self):
        return self.owner
    
    #__str__ is python's toString() in OOP
    def __str__(self):
        carStr = self.getManufacturer() + ',' + str(self.getRNum()) + ',' + self.getColour() + ' owned by ' + self.owner.getFName() + ' ' + self.owner.getLName()
        return carStr

class Owner:
    #Constructor
    def __init__(self, fName, lName, age, phoneNum, lNum):
        self.fName = fName
        self.lName = lName
        self.age = age
        self.phoneNum = phoneNum
        self.lNum = lNum
    
    #Getters
    def getFName(self):
        return self.fName
    
    def getLName(self):
        return self.lName
    
    def getAge(self):
        return self.age
    
    #Phone Num really should be a String, but for the sake of variety it will remain int
    def getPhoneNum(self):
        return self.phoneNum
    
    def getLNum(self):
        return self.lNum

    #to string
    def __str__(self):
        ownerStr = self.getFName() + ' ' + self.getLName() + ', Age: ' + str(self.getAge()) + ', Ph#' + str(self.getPhoneNum()) + ', L#' + str(self.getLNum())
        return ownerStr

#class Garage:

patSmith = Owner('Patrick', 'Smith', 38, 12345678, 123456)
fastCar = Car('Ford', 123456, 'Blue', patSmith)
print()
print(fastCar)
print(patSmith)
print()

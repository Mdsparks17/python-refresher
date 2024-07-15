class Car: 
    # Attributes
    isDriving = False

    # Constructor
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Methods
    def drive(self):
        isDriving = True
        print(self.make+ " is driving")

    def stop(self):
        isDriving = False
        print(self.make + " is stopped")
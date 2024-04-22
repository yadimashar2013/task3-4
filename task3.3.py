class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eg__(self, buildingType):
        return self.numberOfFloors and buildingType


numberOfFloors = Buiding(10, 'aaaa')
buildingType = Buiding(10, 'aaaa')
print(numberOfFloors == buildingType)

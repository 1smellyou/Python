from time import time


class FarmingEstimator:
    # Plant farming Properties
    PlantArea = 0
    PlantGrowingRate = 0 #charge per sqft
    PlantAreaLength = 0
    PlantAreaWidth = 0
    Plantwater = 0
    Plantfeterlizer = 0
    PlantPicking = 0

    # Animal farming
    AnimalArea = 0
    AnimalGrowingRate = 0
    AnimalAreaLength = 0
    AnimalAreaWidth = 0
    AnimalFeeding = 0
    AnimalsKilledrate = 0

    # Products sold
    ProductCost = 0 #Light Cost + Rate/Light
    #QuantityLights = 0

    def __init__(this, plantGrowingRate, animalGrowingRate, productCost):
        this.PlantGrowingRate = plantGrowingRate
        this.AnimalGrowingRate = animalGrowingRate
        this.ProductCost = productCost

    def GetPlantGrowingCost(this, area = 0, length = 0, width = 0):
        if area > 0:
            cost = time * this.PlantGrowingRate
            return cost
        if area <= 0:
            plantGrowingTime = length * width
            cost = plantGrowingTime * this.PlantGrowingRate
            return cost
    
    def GetAnimalGrowingCost(this, length = 0, width = 0):
        calculatedArea = (length * 2) + (width * 2)
        cost = calculatedArea * this.AnimalGrowingRate
        return cost
    
    def GetProductCost(this, Products):
        return Products * this.ProductCost



stevesFarmingEstimator = FarmingEstimator(20, 69, 54)
plantEstimate = stevesFarmingEstimator.GetPlantGrowingCost(0, 76, 89)
animalEstimate = stevesFarmingEstimator.GetAnimalGrowingCost(98, 291)
productEstimate = stevesFarmingEstimator.GetProductCost(108)


print(plantEstimate)
print(animalEstimate)
print(productEstimate)
FarmingTotal = plantEstimate + animalEstimate + productEstimate

print(FarmingTotal)

alexsFarmingEstimator = FarmingEstimator(78.9, 90, 46)
class BMI:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.calcBMI()

    def calcBMI(self):
        h = self.height / 100
        self.bmi = self.weight / (h ** 2)

    def printJudge(self):
        print("---")
        print(self.name + "さん")
        print("BMI=", self.bmi)
        b = self.bmi
        if (b < 18.5):
           print("瘦せ型")
        elif (b < 25):
            print("標準")
        else:
            print("肥満")


preson1 = BMI(name="白石", weight=65, height=170)
preson1.printJudge()
preson2 = BMI(name="北白川", weight=76, height=165)
preson2.printJudge()
preson3 = BMI(name="福島", weight=50, height=180)
preson3.printJudge()

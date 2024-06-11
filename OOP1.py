class car:
    manufacturer = "TATA"
    model = 2022
    number = 1254
    def details(self):
        print("Manufacturer:",self.manufacturer)
        print("Model:",self.model)

tata = car()
print(tata.model)
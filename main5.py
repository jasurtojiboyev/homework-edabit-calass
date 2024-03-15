class Country:
    def __init__(self, country, area, population_density):
        self.country = country
        self.area = area
        self.population_density = population_density
    def math(self):
        if obj.area > obj1.area:
            print(f"{obj.country}.is_big ➞ True")
        if obj.area < obj1.area:
            print(f"{obj1.country}.is_big ➞ True")


obj = Country("Australia", 23545235145500, 7692024)
obj1 = Country("Andorra", 760935233458, 468)
obj.math()
class FoodItem:
    def __init__(self, name="None", fat=0.0, carb=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carb = carb
        self.protein = protein
    def get_calories(self, servings):
        calories = ((self.fat * 9) + (self.carb * 4) + (self.protein * 4)) * servings;
        return calories
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carb))
        print('   Protein: {:.2f} g'.format(self.protein))
if __name__ == "__main__":
    food1 = FoodItem()
    item = input()
    fatamt = float(input())
    carbamt = float(input())
    proteinamt = float(input())
    item2 = FoodItem(item, fatamt, carbamt, proteinamt)
    servings = float(input())
    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, food1.get_calories(servings)))

    print()
    item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings,                                                                   item2.get_calories(servings)))
    item2.get_calories(servings)
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = "product.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        all_products = file.read()
        file.close()
        return all_products

    def add(self, *product):
        for c in product:
            if self.find_product(c.name):
                print(f'Продукт {c.name} уже есть в магазине')
            else:
                file = open(self._Shop__file_name, 'a')
                file.write(f'{c}\n')
                file.close()

    def find_product(self, product):
        all_products = self.get_products()
        if product.upper()+',' in all_products.upper():
            return True
        else:
            return False

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

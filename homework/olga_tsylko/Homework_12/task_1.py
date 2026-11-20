class Flowers():
    def __init__(self, name, color, stem_len, freshness, price, life_time):
        self.name = name
        self.color = color
        self.stem_len = stem_len
        self.freshness = freshness
        self.price = price
        self.life_time = life_time

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.color}, свежесть: {self.freshness}, "
            f"стебель: {self.stem_len} м, цена: {self.price} руб., время жизни: {self.life_time}"
        )


class Rose(Flowers):
    def __init__(self, name, color, stem_len, freshness, price, life_time, thorns=True):
        super().__init__(name, color, stem_len, freshness, price, life_time)
        self.thorns = thorns


class Chrysanthemums(Flowers):
    def __init__(self, name, color, stem_len, freshness, price, life_time, number_of_blooms):
        super().__init__(name, color, stem_len, freshness, price, life_time)
        self.number_of_blooms = number_of_blooms


class Bouquet:
    def __init__(self, *flowers):
        self.flowers = list(flowers)

    def bouquet_price(self):
        b_price = 0
        for flower in self.flowers:
            b_price += flower.price
        return b_price

    def vase_life(self):
        if not self.flowers:
            return 0
        common_life_time = 0
        for flower in self.flowers:
            common_life_time += flower.life_time
        bouquet_life = common_life_time / len(self.flowers)
        return round(bouquet_life, 1)

    def sort_by_color(self, reverse=False):
        self.flowers.sort(
            key=lambda flower: flower.color.lower(), reverse=reverse
        )

    def sort_by_stem_len(self, reverse=False):
        self.flowers.sort(
            key=lambda flower: flower.stem_len, reverse=reverse
        )

    def sort_by_price(self, reverse=False):
        self.flowers.sort(
            key=lambda flower: flower.price, reverse=reverse
        )

    def find_by_color(self, color):
        flowers_by_color = []
        for flower in self.flowers:
            if flower.color.lower() == color.lower():
                flowers_by_color.append(str(flower))
        if not flowers_by_color:
            return f"Цвет '{color}' не найден."
        return "\n".join(flowers_by_color)

    def find_by_life_time(self, life_time):
        flowers_by_life_time = []
        for flower in self.flowers:
            if flower.life_time == life_time:
                flowers_by_life_time.append(str(flower))
        if not flowers_by_life_time:
            return f"Нет цветов с продолжительностью жизни {life_time}"
        return "\n".join(flowers_by_life_time)

    def __str__(self):
        if not self.flowers:
            return "Букет пуст."
        all_flowers = ""
        for flower in self.flowers:
            all_flowers = all_flowers + str(flower) + '\n'
        return all_flowers.strip()


red_rose = Rose('Red Rose', 'red', 1, 1, 10, 5.5)
white_rose = Rose('White Rose', 'white', 1.2, 1, 12, 5)
pink_rose = Rose('Pink Rose', 'pink', 1.5, 1, 11, 6)
white_chrysanthemums = Chrysanthemums(
    'White Chrysanthemums', 'white', 0.8, 1, 15, 10, 5
)
blue_chrysanthemums = Chrysanthemums(
    'Blue Chrysanthemums', 'blue', 1, 1, 16, 15, 7
)
bouquet = Bouquet(red_rose, white_chrysanthemums, white_rose, blue_chrysanthemums, pink_rose)
print(bouquet.bouquet_price())
print(bouquet.vase_life())
print("*** До сортировки ***")
print(bouquet)
bouquet.sort_by_color()
print("*** После сортировки по цвету ***")
print(bouquet)
bouquet.sort_by_stem_len()
print("*** После сортировки по длине стебля ***")
print(bouquet)
bouquet.sort_by_price(reverse=True)
print("*** После сортировки по цене ***")
print(bouquet)
print('Поиск цветов по определенному цвету: ', bouquet.find_by_color('white'))
print('Поиск цветов по продолжительности жизни: ', bouquet.find_by_life_time(5.5))

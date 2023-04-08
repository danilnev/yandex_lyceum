from itertools import cycle


class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.hp > 0:
            s = ((actor.pos_x - target.pos_x) ** 2 + (actor.pos_y - target.pos_y) ** 2) ** 0.5
            if s > self.range:
                print(f'Враг слишком далеко для оружия {self.name}')
            else:
                target.hp -= self.damage
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
        else:
            print('Враг уже повержен')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapon = None
        self.weapons = []
        self.weapon_iter = cycle(self.weapons)

    def hit(self, target):
        if self.weapon:
            if isinstance(target, BaseEnemy):
                self.weapon.hit(self, target)
            else:
                print('Могу ударить только Врага')
        else:
            print('Я безоружен')

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapons.append(weapon)
            if len(self.weapons) == 1:
                self.weapon = next(self.weapon_iter)
            print(f'Подобрал {weapon}')
        else:
            print('Это не оружие')

    def next_weapon(self):
        if len(self.weapons) == 0:
            print('Я безоружен')
        elif len(self.weapons) == 1:
            print('У меня только одно оружие')
        else:
            self.weapon = next(self.weapon_iter)
            print(f'Сменил оружие на {self.weapon}')

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f'Полечился, теперь здоровья {self.hp}')


weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)

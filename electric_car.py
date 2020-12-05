from car import Car

"""Набор классов для представления электромобилей."""


class Battery:
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Апгрейдит батарею, если это возможно"""
        if self.battery_size != 100:
            print(f"Battery size is {self.battery_size}kWh "
                  f"now we will upgrade it to 100kWh.")
            self.battery_size = 100
        else:
            print("Battery already upgraded to 100kWh")


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
    Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")

class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed=max_speed, efficiency=efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        return super().get_trip_cost(distance=distance, food_price=food_price) + (
            self.load_weight * 0.01
        )

    def get_cargo_volume(self):
        return 2 * self.bed_area


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed=max_speed, efficiency=efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume

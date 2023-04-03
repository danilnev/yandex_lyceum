class Vehicle:
    pass


class WaterVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    pass


class EarchVehicle(Vehicle):
    pass


class SpaceVehicle(Vehicle):
    pass


class RiverVehicle(WaterVehicle):
    pass


class SeaVehicle(WaterVehicle):
    pass


class Plane(AirVehicle):
    pass


class Helicopter(AirVehicle):
    pass


class WithEngineVehicle(EarchVehicle):
    pass


class WithoutEngineVehicle(EarchVehicle):
    pass


class Car(WithEngineVehicle):
    pass


class Train(WithEngineVehicle):
    pass


class Bicycle(WithoutEngineVehicle):
    pass


class Skateboard(WithoutEngineVehicle):
    pass


class OrbitalVehicle(SpaceVehicle):
    pass


class InterplanetaryVehicle(SpaceVehicle):
    pass


class OnPlanetVehicle(SpaceVehicle):
    pass



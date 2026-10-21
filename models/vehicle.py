from abc import ABC
from enum import Enum


class VehicleType(Enum):
    BIKE = "bike"
    CAR = "car"
    TRUCK = "truck"


class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        if not license_plate.strip():
            raise ValueError("License plate cannot be empty")

        self.license_plate = license_plate
        self.vehicle_type = vehicle_type


class Bike(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.BIKE)


class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)

from models.vehicle import Vehicle, VehicleType


class ParkingSpot:
    def __init__(self, spot_id: str, supported_type: VehicleType):
        self.spot_id = spot_id
        self.supported_type = supported_type
        self.vehicle = None

    @property
    def is_available(self) -> bool:
        return self.vehicle is None

    def can_park(self, vehicle: Vehicle) -> bool:
        return (
            self.is_available
            and self.supported_type == vehicle.vehicle_type
        )

    def park(self, vehicle: Vehicle) -> None:
        if not self.can_park(vehicle):
            raise ValueError("Spot unavailable or incompatible")

        self.vehicle = vehicle

    def remove_vehicle(self) -> Vehicle:
        if self.is_available:
            raise ValueError("Parking spot is already empty")

        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

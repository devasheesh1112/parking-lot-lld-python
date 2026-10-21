
import math
from datetime import datetime

from models.vehicle import Vehicle, VehicleType


class PricingStrategy:
    HOURLY_RATES = {
        VehicleType.BIKE: 10,
        VehicleType.CAR: 30,
        VehicleType.TRUCK: 50,
    }

    def calculate_fee(
        self,
        vehicle: Vehicle,
        entry_time: datetime,
        exit_time: datetime,
    ) -> float:
        duration_seconds = (
            exit_time - entry_time
        ).total_seconds()

        hours = max(1, math.ceil(duration_seconds / 3600))
        hourly_rate = self.HOURLY_RATES[vehicle.vehicle_type]

        return float(hours * hourly_rate)

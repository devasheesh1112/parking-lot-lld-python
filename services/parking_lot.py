
from datetime import datetime

from models.vehicle import Vehicle
from models.parking_spot import ParkingSpot
from models.ticket import ParkingTicket
from strategies.pricing_strategy import PricingStrategy


class ParkingLot:
    def __init__(self, spots: list[ParkingSpot]):
        self.spots = spots
        self.active_tickets = {}
        self.ticket_counter = 1
        self.pricing_strategy = PricingStrategy()

    def park_vehicle(self, vehicle: Vehicle) -> ParkingTicket:
        for spot in self.spots:
            if spot.can_park(vehicle):
                spot.park(vehicle)

                ticket_id = f"T{self.ticket_counter:04d}"
                self.ticket_counter += 1

                ticket = ParkingTicket(
                    ticket_id=ticket_id,
                    vehicle=vehicle,
                    spot_id=spot.spot_id,
                )

                self.active_tickets[ticket_id] = ticket
                return ticket

        raise ValueError(
            f"No available spot for vehicle type: "
            f"{vehicle.vehicle_type.value}"
        )

    def unpark_vehicle(self, ticket_id: str) -> ParkingTicket:
        ticket = self.active_tickets.get(ticket_id)

        if ticket is None:
            raise ValueError("Invalid or inactive ticket")

        spot = next(
            (
                spot
                for spot in self.spots
                if spot.spot_id == ticket.spot_id
            ),
            None,
        )

        if spot is None:
            raise ValueError("Parking spot not found")

        exit_time = datetime.now()

        fee = self.pricing_strategy.calculate_fee(
            ticket.vehicle,
            ticket.entry_time,
            exit_time,
        )

        spot.remove_vehicle()
        ticket.close_ticket(fee, exit_time)
        del self.active_tickets[ticket_id]

        return ticket

        
    def show_status(self) -> None:
        print("\n--- PARKING LOT STATUS ---")

        for spot in self.spots:
            status = "Available" if spot.is_available else "Occupied"
            vehicle_number = (
                spot.vehicle.license_plate
                if spot.vehicle is not None
                else "-"
            )

            print(
                f"Spot: {spot.spot_id} | "
                f"Type: {spot.supported_type.value} | "
                f"Status: {status} | "
                f"Vehicle: {vehicle_number}"
            )


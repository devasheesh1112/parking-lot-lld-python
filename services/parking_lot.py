
from models.vehicle import Vehicle, VehicleType
from models.parking_spot import ParkingSpot
from models.ticket import ParkingTicket


class ParkingLot:
    def __init__(self, spots: list[ParkingSpot]):
        self.spots = spots
        self.active_tickets = {}
        self.ticket_counter = 1

    def park_vehicle(self, vehicle: Vehicle) -> ParkingTicket:
        # Find the first compatible available spot
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
            f"No available spot for vehicle type: {vehicle.vehicle_type.value}"
        )

    def unpark_vehicle(self, ticket_id: str) -> ParkingTicket:
        ticket = self.active_tickets.get(ticket_id)

        if ticket is None:
            raise ValueError("Invalid or inactive ticket")

        for spot in self.spots:
            if spot.spot_id == ticket.spot_id:
                spot.remove_vehicle()
                break

        ticket.close_ticket(fee=0.0)
        del self.active_tickets[ticket_id]

        return ticket

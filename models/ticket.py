
from datetime import datetime
from models.vehicle import Vehicle


class ParkingTicket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot_id: str):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot_id = spot_id
        self.entry_time = datetime.now()
        self.exit_time = None
        self.fee = 0.0

    def close_ticket(self, fee: float) -> None:
        self.exit_time = datetime.now()
        self.fee = fee

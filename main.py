
from models.vehicle import Car, Bike, Truck, VehicleType
from models.parking_spot import ParkingSpot
from services.parking_lot import ParkingLot


def main():
    # Create parking spots
    spots = [
        ParkingSpot("B1", VehicleType.BIKE),
        ParkingSpot("B2", VehicleType.BIKE),
        ParkingSpot("C1", VehicleType.CAR),
        ParkingSpot("C2", VehicleType.CAR),
        ParkingSpot("T1", VehicleType.TRUCK),
    ]

    # Create parking lot
    parking_lot = ParkingLot(spots)

    # Park a car
    car = Car("MP04AB1234")
    ticket = parking_lot.park_vehicle(car)

    print("\n--- VEHICLE PARKED ---")
    print(f"Vehicle: {ticket.vehicle.license_plate}")
    print(f"Ticket ID: {ticket.ticket_id}")
    print(f"Parking Spot: {ticket.spot_id}")
    print(f"Entry Time: {ticket.entry_time}")

    # Exit the car
    completed_ticket = parking_lot.unpark_vehicle(ticket.ticket_id)

    print("\n--- VEHICLE EXITED ---")
    print(f"Ticket ID: {completed_ticket.ticket_id}")
    print(f"Exit Time: {completed_ticket.exit_time}")
    print(f"Parking Fee: ₹{completed_ticket.fee:.2f}")


if __name__ == "__main__":
    main()

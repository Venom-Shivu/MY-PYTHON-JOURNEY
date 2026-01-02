''' Write a class Train which has methods to book a ticket, get status (no. of seats) and get fare
information of train under Indian Railways'''

#1.  PASSANGER DETAILS (data model)

class Passenger:
    """
    Represents a passenger booking a ticket.
    """

    def __init__(self, name, boarding, destination):
        # Initialize passenger details
        self.name = name
        self.boarding = boarding
        self.destination = destination


#2. TICKET (Result of Booking)

class Ticket:
    """
    Represents a booked ticket.
    """

    def __init__(self, passenger, train_no, seat_no, fare, status):
        # Initialize ticket details
        self.passenger = passenger
        self.train_no = train_no
        self.seat_no = seat_no
        self.fare = fare
        self.status = status

    def display(self):
        # Print ticket information nicely
        print("\n========== TICKET DETAILS ==========")
        print(f"Passenger Name : {self.passenger.name}")
        print(f"Train Number   : {self.train_no}")
        print(f"Route          : {self.passenger.boarding} ➝ {self.passenger.destination}")
        # Show 'N/A' if seat or fare is not assigned (e.g., cancelled ticket)
        print(f"Seat Number    : {self.seat_no if self.seat_no else 'N/A'}")
        print(f"Fare           : {f'₹{self.fare}' if self.fare else 'N/A'}")
        print(f"Status         : {self.status}")
        print("===================================")


# TRAIN (Fair and Status of Booking)

from random import randint

class Train:
    """
    Handles seat management and booking logic.
    """

    def __init__(self, train_no, total_seats):
        self.train_no = train_no
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.bookings = []  # List to store all booked Ticket objects

    def book_ticket(self, passenger):
        """
        Books a ticket if seats are available.
        Returns a Ticket object.
        """

        # Check if seats are available
        if self.available_seats <= 0:
            # Create a CANCELLED ticket if no seats left
            ticket = Ticket(
                passenger=passenger,
                train_no=self.train_no,
                seat_no=None, # No seat assigned
                fare=None,    # No fare charged
                status="CANCELLED"
            )
            self.bookings.append(ticket)
            return ticket

        # If seats are available, confirm the booking
        self.available_seats -= 1 # Reduce available seat count
        seat_no = self.total_seats - self.available_seats # Calculate seat number
        fare = randint(300, 6000) # Generate random fare

        # Create a CONFIRMED ticket
        ticket = Ticket(
            passenger=passenger,
            train_no=self.train_no,
            seat_no=seat_no,
            fare=fare,
            status="CONFIRMED"
        )

        self.bookings.append(ticket)
        return ticket

    def cancel_ticket(self, ticket):
        """Cancels a confirmed ticket and frees the seat."""
        if ticket not in self.bookings:
            return "ERROR: Ticket not found"

        if ticket.status != "CONFIRMED":
            return "ERROR: Ticket already cancelled"

    # Free the seat
        self.available_seats += 1

    # RESET ticket state (this is what you missed)
        ticket.status = "CANCELLED"
        ticket.seat_no = None
        ticket.fare = 0

        return "SUCCESS"


    def get_status(self):
        return {
            "train_no": self.train_no,
            "available_seats": self.available_seats
        }


#4. USER INTERACTION 


def main():
    # Create a Train object with a specific train number and total seats
    train = Train(train_no=12549, total_seats=2)

    # Take input from the user
    name = input("Enter passenger name: ")
    boarding = input("Enter boarding station: ")
    destination = input("Enter destination station: ")

    # Create a Passenger object with the input data
    passenger = Passenger(name, boarding, destination)

    # Attempt to book a ticket for this passenger
    ticket = train.book_ticket(passenger)
    ticket.display()

    # Check and display the remaining seats
    status = train.get_status()
    print(f"\nSeats left in Train {status['train_no']}: {status['available_seats']}")

    # Cancel the ticket
    train.cancel_ticket(ticket)

    # Show updated ticket details and seat count
    ticket.display()
    status = train.get_status()
    print(f"\nSeats left after cancellation: {status['available_seats']}")


if __name__ == "__main__":
    main()

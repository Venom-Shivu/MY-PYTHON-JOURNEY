''' Write a class Train which has methods to book a ticket, get status (no. of seats) and get fare
information of train under Indian Railways'''

from random import randint

class Train:
    """
    Represents a Train under Indian Railways.
    Handles ticket booking, seat availability, and fare calculation.
    """

    def __init__(self, train_no, total_seats):
        # Unique train number
        self.train_no = train_no
        
        # Total seats available in the train
        self.total_seats = total_seats
        
        # Seats currently available
        self.available_seats = total_seats

    # --------------------------------------------------
    # BOOK A TICKET
    # --------------------------------------------------
    def book_ticket(self, passenger_name, train_from, train_to):
        """
        Attempts to book a ticket for the passenger.
        Confirms booking only if seats are available.
        """
        print(f"\nBooking Request for {passenger_name}")
        print(f"Train No: {self.train_no}")
        print(f"Route: {train_from} ➝ {train_to}")

        if self.available_seats > 0:
            # Seat is available → confirm booking
            self.available_seats -= 1
            print("Status : ✅ CONFIRMED")
            print(f"Seat No: {self.total_seats - self.available_seats}")
        else:
            # No seats left → booking cancelled
            print("Status : ❌ CANCELLED")
            print("Reason : No seats available")

    # --------------------------------------------------
    # CHECK TRAIN & SEAT STATUS
    # --------------------------------------------------
    def get_status(self):
        """
        Displays the current running status and seat availability.
        """
        print(f"\nTrain No {self.train_no} Status")
        print("Running Status : On Time")
        print(f"Available Seats: {self.available_seats}")

    # --------------------------------------------------
    # GET TICKET FARE
    # --------------------------------------------------
    def get_fare(self, train_from, train_to):
        """
        Displays ticket fare between two stations.
        """
        fare = randint(300, 6000)
        print(f"\nFare Information")
        print(f"Train No: {self.train_no}")
        print(f"Route: {train_from} ➝ {train_to}")
        print(f"Ticket Fare: ₹{fare}")


# ======================================================
# DRIVER CODE (USER INTERACTION)
# ======================================================

# Creating a train with limited seats
t2 = Train(train_no =23718, total_seats=5)

#Booking tickets
t2.book_ticket("David Thomson", "Lucknow", "Bangluru")
t2.book_ticket("Shivansh Yadav", "Lucknow", "Bangluru")
t2.book_ticket("Sakshi Yadav", "Lucknow", "Bangluru")
t2.book_ticket("Anushka Singh", "Lucknow", "Bangluru")
t2.book_ticket("Aman Singh", "Lucknow", "Bangluru")

# Checking train status
t2.get_status()

# Getting Fare Details
t2.get_fare("Lucknow", "Bangluru")


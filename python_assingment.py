class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

    def get_details(self):
        return f"Flight ID: {self.flight_id}\nSource: {self.source}\nDestination: {self.destination}\nPrice: {self.price}\n"

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def find_flights(self, key, value):
        found_flights = [flight.get_details() for flight in self.flights if getattr(flight, key) == value]
        return "\n".join(found_flights) if found_flights else f"No flights found with the given {key}."

flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

user_input = input("Enter Flight ID, source city, or destination city: ")

if(len(user_input) == 3):
    a = int(input("1 for source , 2 for destination: "))

if user_input in ["AI161E90","BR161F91","AI161F99","VS171E20","AS171G30","AI131F49"]:
    result = flight_table.find_flights('flight_id', user_input)
elif user_input in ["BLR", "BOM", "BBI", "HYD", "JLR"] and a == 1:
    result = flight_table.find_flights('source', user_input)
elif user_input in ["BLR", "BOM", "BBI", "HYD", "JLR"] and a == 2:
    result = flight_table.find_flights('destination', user_input)
else:
    result = "Invalid input. Please enter Flight ID, source city, or destination city."

print(result)

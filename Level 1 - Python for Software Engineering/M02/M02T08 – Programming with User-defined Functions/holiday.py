def hotel_cost(num_nights):
    """Calculate total hotel cost based on $120/night."""
    nightly_rate = 120
    return num_nights * nightly_rate


def plane_cost(city_flight):
    """Return flight cost based on the destination city using if/elif/else statements."""
    city = city_flight.lower().strip()
    
    if city == "london":
        return 500
    elif city == "paris":
        return 400
    elif city == "tokyo":
        return 800
    elif city == "new york":
        return 600
    else:
        return 350  # Default rate for other cities


def car_rental(rental_days):
    """Calculate total car rental cost based on $50/day."""
    daily_rate = 50
    return rental_days * daily_rate


def holiday_cost(num_nights, city_flight, rental_days):
    """Calculate overall holiday cost by calling individual cost functions."""
    total_hotel = hotel_cost(num_nights)
    total_flight = plane_cost(city_flight)
    total_car = car_rental(rental_days)
    
    return total_hotel + total_flight + total_car


# Main program execution
if __name__ == "__main__":
    print("=== Holiday Cost Calculator ===")
    
    # Get user inputs
    city_flight = input("Enter the city you are flying to (e.g., London, Paris, Tokyo, New York): ")
    num_nights = int(input("Enter the number of nights you will stay at the hotel: "))
    rental_days = int(input("Enter the number of days you will rent a car: "))
    
    # Compute individual and total costs
    flight_price = plane_cost(city_flight)
    hotel_price = hotel_cost(num_nights)
    car_price = car_rental(rental_days)
    total_price = holiday_cost(num_nights, city_flight, rental_days)
    
    # Print readable details
    print("\n----------------------------------------")
    print("           HOLIDAY DETAILS              ")
    print("----------------------------------------")
    print(f"Destination City  : {city_flight.title()}")
    print(f"Flight Cost       : ${flight_price:.2f}")
    print(f"Hotel Stay ({num_nights} nights): ${hotel_price:.2f}")
    print(f"Car Rental ({rental_days} days): ${car_price:.2f}")
    print("----------------------------------------")
    print(f"Total Holiday Cost: ${total_price:.2f}")
    print("----------------------------------------")
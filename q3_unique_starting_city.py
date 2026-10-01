def find_starting_city(city_distances, fuel, mpg):
    # Initialize total and current fuel tank levels
    total_tank = 0  # Tracks fuel balance across all cities
    current_tank = 0  # Tracks fuel balance for current starting city
    starting_city = 0  # City index to start from

    # Loop through all cities
    for i in range(len(city_distances)):
        # Calculate fuel gain from city[i]'s gas station
        fuel_gain = fuel[i] * mpg
        
        # Calculate fuel required to travel from city[i] to city[i+1]
        fuel_required = city_distances[i]
        
        # Update total fuel balance (all cities considered)
        total_tank += fuel_gain - fuel_required
        
        # Update current fuel balance (starting from the current starting city)
        current_tank += fuel_gain - fuel_required
        
        # If we can't reach the next city, change starting city
        if current_tank < 0:
            starting_city = i + 1  # Move starting point to the next city
            current_tank = 0  # Reset current tank for the new start

    # If the total fuel balance is non-negative, return the valid starting city
    # Otherwise, return -1 (indicating no solution, but this won't happen due to the problem constraints)
    return starting_city if total_tank >= 0 else -1
# Example input
city_distances = [5, 25, 15, 10, 15]
fuel = [1,2,1,0,3]
mpg = 10

# Output the preferred starting city
print("Preferred starting city:", find_starting_city(city_distances, fuel, mpg)) 

#DONE BY ROSZHAN RAJ MEENAKSHI SUNDHRESAN, PARASTOO TOOSIE, DEEPTHIMAYI PEASALA
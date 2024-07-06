# Hardcoded water footprint data (in liters per kilogram)
water_footprint_data = {
    "Beef": 15415,
    "Chicken": 4325,
    "Rice": 2375,
    "Apples": 822,
    "Bananas": 790,
}

def calculate_water_footprint(food_item, quantity):
    if food_item in water_footprint_data:
        water_footprint_per_kg = water_footprint_data[food_item]
        total_water_usage = water_footprint_per_kg * (quantity / 1000)  # Convert quantity to kilograms
        return total_water_usage
    else:
        return None

def main():
    print("Water Footprint Calculator")
    food_item = input("Enter the name of the food item: ")
    quantity = float(input("Enter the quantity (in grams): "))

    water_footprint = calculate_water_footprint(food_item, quantity)

    if water_footprint is not None:
        print(f"The water footprint of {quantity} grams of {food_item} is {water_footprint} liters.")
    else:
        print("Sorry, we don't have data for this food item in our database.")

if __name__ == "__main__":
    main()

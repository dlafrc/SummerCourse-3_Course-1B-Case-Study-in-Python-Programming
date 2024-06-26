def main():
    total_gallons = 0.0
    total_miles = 0.0

    while True:
        gallons = float(input("Enter the gallons used (-1 to end): "))
        if gallons == -1:  # loop that terminates at -1
            break
        miles = float(input("Enter the miles driven: "))

        miles_per_gallon = miles / gallons
        print(f"The miles/gallon for this tank was {miles_per_gallon:.6f}")

        total_gallons += gallons
        total_miles += miles

    if total_gallons > 0:  # Avoid division by zero
        combined_miles_per_gallon = total_miles / total_gallons
        print(f"The combined miles/gallon for all tankfuls was {combined_miles_per_gallon:.6f}")
    else:
        print("No data to calculate combined miles/gallon.")

if __name__ == "__main__":
    main()

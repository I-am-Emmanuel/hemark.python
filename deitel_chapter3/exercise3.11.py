import decimal

print("Miles per fuel gallon calculator")
count = 0
distance_per_tank = 0
new_miles = 0

miles_driven = decimal.Decimal(input("Enter the distance you covered: "))
fuel_per_gallon = decimal.Decimal(input("Enter the gallon of your fuel used(Press -1 to end): "))

while fuel_per_gallon != -1:

    new_miles = miles_driven / fuel_per_gallon
    print(f'The amount of fuel in miles/gallon for this tank was {new_miles:.5}')
    if new_miles == 0:
        count -= 1
        print("No amount of distance was recorded for this tank")
    count += 1
    distance_per_tank += new_miles

    miles_driven = decimal.Decimal(input("Enter the distance you covered: "))
    fuel_per_gallon = decimal.Decimal(input("Enter the gallon of your fuel used(Press -1 to end): "))

    if fuel_per_gallon == -1:
        overall_average_per_gallon = distance_per_tank / count
        print(f'The overall average miles/gallon was {overall_average_per_gallon}')
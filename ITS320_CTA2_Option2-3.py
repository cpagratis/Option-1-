car_brand = input('Please enter vehicle brand? ')
car_model = input('Please enter a vehicle model? ')
car_year = int(input('Please enter the year of the vehicle? '))
car_odometer_low = float(input('What is the lowest odometer reading? '))
car_odemeter_high = float (input('What is the highest odometer reading? '))
car_mpg = float(input('How many miles per gallon do you get? '))

car = {
    "Brand" : car_brand,
    "Model" : car_model,
    "Year" : car_year,
    "Lowest odometer reading" : car_odometer_low,
    "Highest odometer reading" : car_odemeter_high,
    "Miles Per Gallon" : car_mpg
}

for x, y in car.items():
    print(f"{x}: {y}")
input("Please hit enter to exit: ")


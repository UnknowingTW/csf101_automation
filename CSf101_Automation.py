def calculate_bmi(weight_kg, height_m):
    
    #Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    #Formula: BMI = weight (kg) / (height (m)  2)
    
    if weight_kg <= 0 or height_m <= 0:
        return None  # Invalid input

    bmi = weight_kg / (height_m  2)
    return bmi
def interpret_bmi(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"

def main():
    try:
        name = input(" Enter your name :")
        print(" Welcome",name)
        print("Fill up the details to check your BMI")
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    bmi = calculate_bmi(weight_kg, height_m)
    condition = interpret_bmi(bmi)

    if bmi is not None:
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Condition: {condition}")

if name == "main":
    main()
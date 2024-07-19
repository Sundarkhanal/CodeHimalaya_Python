def calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    print("Your BMI is", bmi)
    
    if bmi < 16:
        return f"Your BMI is {bmi:.2f}, you are extremely underweight."
    elif 16 <= bmi < 18.5:
        return f"Your BMI is {bmi:.2f}, you are underweight."
    elif 18.5 <= bmi < 25:
        return f"Your BMI is {bmi:.2f}, you are normal weight."
    elif 25 <= bmi < 30:
        return f"Your BMI is {bmi:.2f}, you are overweight."
    elif bmi >= 30:
        return f"Your BMI is {bmi:.2f}, you are obese."
    else:
        return f"Your BMI is {bmi:.2f}, invalid BMI range."

print(calc_bmi(30, 5.6))


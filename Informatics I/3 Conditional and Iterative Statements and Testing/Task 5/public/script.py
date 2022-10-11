#!/usr/bin/env python3

# Height in M
height = 10
# Weight in KG
weight = 10

# Determine the BMI. Change the function below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value. 
# You must use the variables defined above.

def get_bmi_category():

    # You need to change the following part of the function to determine the BMI and return the correct category.
    # The BMI formula is given by BMI = weight / height^2 where weight is in kilograms and height is in meters.

    # For unreasonable inputs (a.k.a heights/weights below 0) simply return "N/A" -.-
    if height <= 0 or weight < 0: 
        return "N/A"

    bmi = weight / pow(height, 2) # Calulcate the BMI index (attention division by zero avoided with above statement "height <= 0", thanks Jan)
    bmi_category = "" # This string will hold the bmi category

    # Assign a category according to the bmi index
    if bmi >= 0 and bmi <= 18.5: # [0, 18.5]	Underweight
        bmi_category = "Underweight"
    elif bmi > 18.5 and bmi <= 25: # (18.5, 25]	Normal weight
        bmi_category = "Normal weight"
    elif bmi > 25 and bmi <= 30: # (25, 30]	Pre-obesity
        bmi_category = "Pre-obesity"
    elif bmi > 30 and bmi <= 35: # (30, 35]	Obesity class I
        bmi_category = "Obesity class I"
    elif bmi > 35 and bmi <= 40: # (35, 40]	Obesity class II
        bmi_category = "Obesity class II"
    elif bmi > 40: # (40, inf)	Obesity class III
        bmi_category = "Obesity class III"
    else: # Everything that does not correspond with the chart
        return "N/A"
    
    # Compose string like: "BMI: 26.12, Category: Normal weight".
    bmi_output = "BMI: " + f"{bmi:.2f}" + ", Category: " + bmi_category
    
    # Return the BMI values and the correct category after you have calculated the BMI.
    return bmi_output

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())
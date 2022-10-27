#!/usr/bin/env python3

# Height in M
height = 10
# Weight in KG
weight = 10


# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.


def get_bmi_category():
    # You need to change the following part of the function
    # to determine the BMI and return the correct category.

    bmi = weight / (height * height)
    bmi_category = ""
    answer = ""

    if height < 0 or weight < 0:
        return "N/A"

    if 0 <= bmi <= 18.5:
        bmi_category = "Underweight"
    elif 18.5 < bmi <= 25:
        bmi_category = "Normal weight"
    elif 25 < bmi <= 30:
        bmi_category = "Pre-obesity"
    elif 30 < bmi <= 35:
        bmi_category = "Obesity class I"
    elif 35 < bmi <= 40:
        bmi_category = "Obesity class II"
    elif bmi > 40:
        bmi_category = "Obesity class III"
    else:
        return "N/A"
    bmi = round(bmi, 2)

    answer = f"BMI: {bmi}, Category: {bmi_category}"

    return answer


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())

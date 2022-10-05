# Body Mass index (BMI) Calculator

The following table contains information on the body mass index (BMI) for adults from the [WHO website](https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations)
. The intervals are defined in mathematical notation, "()" meaning "non-inclusive" and "\[]" meaning inclusive.

The BMI formula is given by
BMI = weight / height^2
where weight is in kilograms and height is in meters.

| BMI (kg/m^2) | Category |
| ------------ | -------- |
| \[0, 18.5]   | Underweight |
| (18.5, 25]   | Normal weight |
| (25, 30]     | Pre-obesity |
| (30, 35]     | Obesity class I |
| (35, 40]     | Obesity class II |
| (40, ♾️)     | Obesity class III |

Write a program that determines the right BMI catergory for a given height and weight. The height in metres and weight in kg are provided in a `float` variables called `height` and `weight`, respectively. The BMI category is calculated by a function called `get_bmi_category` and your task is to complete the function.

Please make sure that your solution is self-contained within the `get_bmi_category` function. That is, only change the body of the function, not the code outside the function. Your function is expected to return the right category in a string and the BMI to 2 decimal places. For example, if the height is 1.75 and the weight is 80, the function should return the string "BMI: {26.12}, Category: Pre-obesity". If the user enters a negative height or weight, the function should return the string "N/A".

```python

You can format the BMI to 2 decimal places using the following code:

```python

bmi = 26.123456789
print("BMI: {:.2f}".format(bmi))

```

 
For invalid categories (i.e., measures outside the limits stated in the table), return `"N/A"` as the category.

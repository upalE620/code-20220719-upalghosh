# Importing necessary packages
import numpy as np
import pandas as pd
import json

# Opening and Loading the JSON dataset
with open("data.json", "r+") as f:
    data = json.load(f)

# Incorporating the data into a python dataset
df = pd.json_normalize(data)

# Adding new columns
df["HeightM"] = df["HeightCm"] / 100
df["BMI"] = df.WeightKg / (df["HeightM"] ** 2)

# create a list of our conditions
conditions = [
    (df.BMI < 18.5),
    (df.BMI >= 18.5) & (df.BMI < 25),
    (df.BMI >= 25) & (df.BMI < 30),
    (df.BMI >= 30) & (df.BMI < 35),
    (df.BMI >= 35) & (df.BMI < 40),
    (df.BMI >= 40)
    ]

# create a list of the values we want to assign for each condition
values1 = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 'Severely obese', 'Very severely obese']
values2 = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']

# create a new column and use np.select to assign values to it using our lists as arguments
df['BMI Category'] = np.select(conditions, values1)
df['Health Risk'] = np.select(conditions, values2)

# Modifying the dataframe
df = df[["Gender", "HeightM", "WeightKg", "BMI", "BMI Category", "Health Risk"]]

# New Dataframe
print(df)

# Displaying the total number of overweight people
print("The total no. of overweight people is", str(df[df["BMI Category"] == "Overweight"].shape[0]))

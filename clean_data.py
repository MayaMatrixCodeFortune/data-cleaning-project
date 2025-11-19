import pandas as pd

# Load data
df = pd.read_csv("raw_data.csv")

# Remove empty rows
df = df.dropna()

# Capitalize city names
df["city"] = df["city"].str.title()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning complete! File saved as cleaned_data.csv")

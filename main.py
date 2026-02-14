from preprocess_data import clean_data

# Load cleaned data
df = clean_data("data.csv")

# Create User-Item Matrix
matrix = df.pivot_table(
    index="User's ID",
    columns="ProdID",
    values="Rating",
    fill_value=0
)

# Display matrix
print("\nUser–Item Matrix Preview:\n")
print(matrix.head())

import pandas as pd

# Load data from the specified file path
data_file = r"data\Competitor Pricing Tier Percept.csv"  # Use your provided file path
df = pd.read_csv(data_file)

# Inspect the data (optional)
print(df.head())

# Define a function to categorize pricing tier relative to Haldiram
def categorize_pricing(row, haldiram_price_per_100g):
    price_per_100g = row['Price per 100g (INR)']
    
    if price_per_100g >= 1.5 * haldiram_price_per_100g:
        return 'Premium'
    elif 0.75 * haldiram_price_per_100g <= price_per_100g < 1.5 * haldiram_price_per_100g:
        return 'Mid-Range'
    else:
        return 'Economy'

# Ensure 'Price per 100g (INR)' is numeric, handling any non-numeric values
df['Price per 100g (INR)'] = pd.to_numeric(df['Price per 100g (INR)'], errors='coerce')

# Set Haldiram's price per 100g (you may need to extract from the dataset or hardcode)
haldiram_row = df[df['Brand'] == "Haldiram's"]
if not haldiram_row.empty:
    haldiram_price_per_100g = haldiram_row['Price per 100g (INR)'].iloc[0]
else:
    print("Error: Haldiram's data not found in the dataset.")
    exit()

# Print Haldiram's price per 100g in a safe way, avoiding encoding issues
try:
    print("Haldiram's Price per 100g: {:.2f} INR".format(haldiram_price_per_100g))

except ValueError as e:
    print(f"Error formatting Haldiram's price: {e}")

# Apply the categorization function to all competitors
df['Pricing Tier'] = df.apply(categorize_pricing, axis=1, haldiram_price_per_100g=haldiram_price_per_100g)

# Create the final table to display competitor pricing tiers
final_table = df[['Brand', 'Product', 'Size', 'Price (INR)', 'Price per 100g (INR)', 'E-commerce Platform', 'Pricing Tier']]

# Display the table (optional)
print(final_table)

# Save to a new CSV file (optional)
output_file = r"data\pricing_tiers_output.csv"
final_table.to_csv(output_file, index=False)

print(f"Output saved to {output_file}")

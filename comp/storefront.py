import pandas as pd

# Load data from the specified file path
data_file = r"data\Competitor Online Storefront Pr.csv"  # Use your provided file path
df = pd.read_csv(data_file)

# Inspect the data (optional)
print(df.head())

# Set the procedure as a function to check DTC Website and E-commerce Functionality
def check_online_storefront(row):
    # Check the presence of DTC website and e-commerce functionality
    if row['DTC Website'] == 'Yes' and row['E-commerce Functionality'] == 'Yes':
        return 'Yes'
    else:
        return 'No'

# Apply the check to the DataFrame (optional)
df['Online Storefront Presence'] = df.apply(check_online_storefront, axis=1)

# Final table representation for Competitor Online Storefront Presence
final_table = df[['Brand', 'DTC Website', 'E-commerce Functionality', 'Online Storefront Presence']]

# Optional: Format the output for a cleaner, more readable display
final_table.columns = ['Brand Name', 'Has DTC Website', 'Has E-commerce Functionality', 'Has Online Storefront']
final_table = final_table.sort_values(by='Brand Name')

# Display the formatted table (optional)
print(final_table)

# Save the nicely formatted table to a new CSV file
output_file = r"data\competitor_online_storefront_output.csv"
final_table.to_csv(output_file, index=False)

print(f"Formatted output saved to {output_file}")

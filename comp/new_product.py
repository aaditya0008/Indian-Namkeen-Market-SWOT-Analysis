import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
file_path = "data\Competitor New Product Launches.csv"
df_product_launches = pd.read_csv(file_path)

# Step 2: Clean up the data (remove extra spaces, ensure all data is in the correct format)
df_product_launches.columns = df_product_launches.columns.str.strip()

# Step 3: Display the dataframe to inspect the data
print(df_product_launches)

# Step 4: Create a simple bar chart to visualize the frequency of new product launches by competitor
plt.figure(figsize=(10, 6))
plt.bar(df_product_launches['Brand'], df_product_launches['Number of New Products'], color='skyblue')

# Step 5: Customize the plot (titles, labels, etc.)
plt.title('Number of New Product Launches by Competitor', fontsize=16)
plt.xlabel('Brand', fontsize=12)
plt.ylabel('Number of New Products', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Step 6: Show the plot
plt.show()

# Step 7: Save the plot to a file if required
output_plot_path = "data\Competitor_New_Product_Launch_Frequency.png"
plt.savefig(output_plot_path)

# Step 8: Save the summarized data to a new CSV
output_file_path = "data\Competitor_New_Product_Launches_Summarized.csv"
df_product_launches.to_csv(output_file_path, index=False)

print(f"Competitor new product launches summarized and chart saved to: {output_file_path}")

import pandas as pd

# Step 1: Load the CSV file
file_path = "data\Competitor Marketing Campaign I.csv"
df_campaigns = pd.read_csv(file_path)

# Step 2: Inspect the data structure and ensure no empty or invalid rows
df_campaigns.dropna(subset=['Competitor', 'Identified Marketing Campaigns'], inplace=True)

# Step 3: Grouping campaigns by Competitor (excluding the date column)
competitor_campaigns = df_campaigns.groupby('Competitor').agg({
    'Identified Marketing Campaigns': lambda x: ', '.join(x)
}).reset_index()

# Step 4: Ensure full text display for long text columns
pd.set_option('display.max_colwidth', None)  # Disable truncation of columns

# Step 5: Display the results
print("\nCompetitor Marketing Campaigns:")
print(competitor_campaigns)

# Step 6: Save the summarized data to a new CSV if desired
output_file_path = "data\Competitor_Summarized_Campaigns_NoDate.csv"
competitor_campaigns.to_csv(output_file_path, index=False)

print(f"Competitor marketing campaigns summarized and saved to: {output_file_path}")

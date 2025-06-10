import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Read the file
file_path = r"data\news n mentions + sentiment.csv"
df = pd.read_csv(file_path)

# Step 2: Clean column names
df.columns = df.columns.str.strip()

# Step 3: Verify required columns
if not {'Brand', 'Sentiment'}.issubset(df.columns):
    raise ValueError(f"Missing required columns. Found: {df.columns.tolist()}")

# Step 4: Get unique brands
brands = df['Brand'].unique()

# Step 5: Set colors
sentiment_colors = {
    'Positive': '#4CAF50',
    'Neutral': '#FF9800',
    'Negative': '#F44336'
}

# Step 6: Plot one pie chart per brand
for brand in brands:
    brand_df = df[df['Brand'] == brand]
    sentiment_counts = brand_df['Sentiment'].value_counts()

    # Plot pie chart
    plt.figure(figsize=(6, 5))
    sentiment_counts.plot(
        kind='pie',
        colors=[sentiment_colors.get(s, '#999999') for s in sentiment_counts.index],
        autopct='%1.1f%%',
        startangle=140
    )

    plt.title(f'Sentiment Breakdown - {brand}')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

def analyze_product_issues():
    # Step 1: Load the CSV File
    file_path = "data/competitor product issue.csv"
    df = pd.read_csv(file_path)

    # Step 2: Clean and Preprocess Data
    df['Date Reported / Period'] = pd.to_datetime(df['Date Reported / Period'], errors='coerce')

    # Step 3: Group by Competitor and Type of Incident to Count Frequency
    incident_counts = df.groupby(['Competitor', 'Type of Incident / Complaint Pattern']).size().reset_index(name='Incident Frequency')

    # Step 4: Group by Competitor and Severity to Get Frequency by Severity Level
    severity_counts = df.groupby(['Competitor', 'Severity']).size().reset_index(name='Severity Frequency')

    # Step 5: Plot Timeline of Incidents Over Time
    incident_timeline = df.groupby(df['Date Reported / Period'].dt.to_period('M')).size()

    plt.figure(figsize=(10,6))
    incident_timeline.plot(kind='line')
    plt.title('Competitor Product Quality Issues Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Incidents')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

    # Step 6: Identify High-Impact Industry-Wide Issues (High Severity)
    high_severity_issues = df[df['Severity'] == 'High']
    print("High Severity Incidents (Industry-Wide):")
    print(high_severity_issues)

    # Step 7: Display Results
    print("\nIncident Frequency by Competitor and Type:")
    print(incident_counts)

    print("\nIncident Frequency by Severity:")
    print(severity_counts)

import pandas as pd

def run_analysis():
    # Load the data
    data = pd.read_csv('data/sample.csv')  # Ensure the file path and name are correct

    # Debug: Print column names
    print("Columns in CSV:", data.columns)

    # Remove spaces and standardize column names
    data.columns = data.columns.str.strip()

    # Perform analysis (e.g., calculate mean of "Total Spent")
    mean_value = data['Total Spent'].mean()

    # Return the result
    return {'mean_total_spent': mean_value}

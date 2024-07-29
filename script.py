import os
import pandas as pd

# Specify the folder containing the CSV files
folder_path = 'C:/PyTest'

# List to hold DataFrames
dataframes = []

# Loop through all the files in the folder
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Concatenate all DataFrames
combined_df = pd.concat(dataframes, ignore_index=True)

# Specify the output Excel file path
output_excel_path = 'C:/PyTest/output.xlsx'

# Write the combined DataFrame to an Excel file
combined_df.to_excel(output_excel_path, index=False)
